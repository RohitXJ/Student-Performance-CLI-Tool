def summary(df):
    print(f"Rows : {df.shape[0]} Columns : {df.shape[1]}")
    print(f"Column names : {df.columns.tolist()}")
    print(f"Sample\n{df.head()}")
    print(f"Null Count :\n{df.isnull().sum()}")

import pandas as pd
#summary(pd.read_csv(f'data/StudentsPerformance.csv'))