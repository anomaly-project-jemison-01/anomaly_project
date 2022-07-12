#stephen fitzsimon
#anomaly project wrangle functions
import os

import pandas as pd

import env

def get_curriculum_data(query_sql = False):
    #filename constants
    filename = 'curriculum_logs.csv'
    query = """SELECT l.*, c.*, (CASE 
		WHEN c.program_id = 1 THEN "full_stack_php"
		WHEN c.program_id = 2 THEN "full_stack_java"
		WHEN c.program_id = 3 THEN "data_science"
		WHEN c.program_id = 4 THEN "front_end"
		ELSE "unknown_program"
		END) AS program_name
	FROM logs AS l
	LEFT JOIN cohorts AS c ON c.id = l.cohort_id;"""
    #check for file existence
    if os.path.isfile(filename) and not query_sql:
        #return dataframe from file
        print('Returning saved csv files.')
        #return files
        df = pd.read_csv(filename).drop(columns = ['Unnamed: 0'])
        return df
    else:
        #get data from url
        print('Getting data from database...')
        df = pd.read_sql_query(query, env.get_db_url('curriculum_logs'))
        print('Saving to .csv files...')
        #save data to csv.
        df.to_csv(filename)
        print('Returned dataframes.')
        #return to user
        return df

def prepare_datetime_col(df):
    df['timestamp'] = df['date'] + ' ' + df['time']
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df.drop(columns = ['date', 'time', 'program_id'])

def q5_wrangle(old_df):
    df5 = old_df.copy()
    #drop staff access
    df5 = df5[df5.name != 'Staff']
    #drop unknown cohorts
    df5 = df5[~df5.name.isna()]
    #convert date to datetime format
    df5['date'] = pd.to_datetime(df5['date'],format='%Y-%m-%d')
    df5['end_date'] = pd.to_datetime(df5['end_date'],format='%Y-%m-%d')
    #only look at currently active students
    df5 = df5[df5['date'] <= df5['end_date']]
    return df5

def q6_wrangle(old_df):
    df = old_df.copy()
    #Convert these columns to datetimes
    df['date'] = pd.to_datetime(df['date'],format='%Y-%m-%d')
    df['start_date'] = pd.to_datetime(df['start_date'],format='%Y-%m-%d')
    df['end_date'] = pd.to_datetime(df['end_date'],format='%Y-%m-%d')
    #filter dataset down to just post-graduation visits
    df = df[df.date > df.end_date]
    #get a days after graduation column
    df['days_post_grad'] = (df['date'] - df['end_date']).astype('timedelta64[D]')
    #drop entry points ('/','index.html' and 'search/search_index.json')
    df = df[(df.path != '/') & (df.path != 'search/search_index.json') & (df.path != 'index.html')]
    #also drop images
    df = df[~(df.path.str.endswith('.jpg')) & ~(df.path.str.endswith('.jpeg')) & ~(df.path.str.endswith('.svg'))]
    return df