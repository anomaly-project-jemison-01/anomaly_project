#stephen fitzsimon
#utils for anomaly detection project
import pandas as pd

def make_timedate_columns(df):
    """
    Make all the columns with dates into datetime columns
    """
    df['start_date'] = pd.to_datetime(df['start_date'])
    df['end_date'] = pd.to_datetime(df['end_date'])
    df['created_at'] = pd.to_datetime(df['created_at'])
    df['update_at'] = pd.to_datetime(df['updated_at'])
    return df

def get_students_df(df):
    return df[~(df.name=='Staff')]

def get_active_students(df)
    students_df = get_students_df(df)
    active_students = students_df[(students_df.timestamp > students_df.start_date) & (students_df.timestamp < students_df.end_date)]
    return active_students