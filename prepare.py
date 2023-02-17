
import os
import pandas as pd

from env import username, host, password




def to_datetime(df, col):
    
    '''this function takes in a dataframe, changes the 'sale_date' col
    to datetime and then sets it as the index, then creates day and month
    columns, along with total 'sale_amount' col, and returns the 
    modified dataframe
    '''
    
    # change 'sale_date' to datetime format
    df[col] = pd.to_datetime(df[col])
    
    # setting 'sale_date' as index and sorting it
    df = df.set_index(col).sort_index()
    
    # creating month col
    df['month'] = df.index.month

    # creating day col
    df['day'] = df.index.day
    
    return df



# find the upper- & lower-bounds function

def get_lower_and_upper_bounds(df, col, k = 1.5):
    
    # looking at 25th & 75th quantiles
    q1, q3 = df[col].quantile([0.25, 0.75])

        #spending_score IQR 
    col_iqr = q3 - q1

        # finding upper and lower bounds
    col_lower = q1 - k * col_iqr
    col_upper = q3 + k * col_iqr

    return (f'{col}, Q1 : {q1}, Q3 : {q3}, Column lower bound : {round(col_lower, 4)}, ' +
                 f'Column upper bound : {col_upper}')





# find out of upper & lower bounds function

def find_out_of_upper_lower_bounds(df, col, k = 1.5):
    
    #finding the quantiles for a particular column
    q1, q3 = df[col].quantile([0.25, 0.75])
    
    # make iqr
    iqr = q3 - q1
    
    # set upper outlier boundary
    upper_bound = q3 + k * col_iqr
    
    # set lower outlier boundary
    lower_bound = q1 - k * col_iqr

    return (np.where(df[col] > upper_bound, 1, 0)), (np.where(df[col] < lower_bound, 1, 0))