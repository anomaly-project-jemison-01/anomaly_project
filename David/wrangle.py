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
    return df

