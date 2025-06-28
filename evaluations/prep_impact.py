def impact(df):
    prep_df = df[df['test preparation course'] == 'completed'][["math score","reading score","writing score"]]
    no_prep_df = df[df['test preparation course'] == 'none'][["math score","reading score","writing score"]]

    prep = prep_df.sum(axis='columns')
    no_prep = no_prep_df.sum(axis='columns')

    prep_mean = prep.mean()
    no_prep_mean = no_prep.mean()
    print(f"Avg Score with Preperation : {prep_mean:.2f}")
    print(f"Avg Score without Preparation : {no_prep_mean:.2f}")

import pandas as pd
impact(pd.read_csv(r"data\StudentsPerformance.csv"))