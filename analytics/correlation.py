def correlation(df):
    score_df = df.drop(columns=["gender","test preparation course"])
    correlation_matrix = score_df.corr()
    print("Correlation matrix: \n",correlation_matrix)

import pandas as pd
#correlation(pd.read_csv(r"data\StudentsPerformance.csv"))
