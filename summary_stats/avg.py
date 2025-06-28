def avg_scores(df):
    print(f"Avg Math Score : {df["math score"].mean():.2f}")
    print(f"Avg Reading Score : {df["reading score"].mean():.2f}")
    print(f"Avg Writing Score : {df["writing score"].mean():.2f}")

def avg_scores_gender(df):
    male_scores = df[df["gender"] == "male"][["math score","reading score","writing score"]]
    female_scores = df[df["gender"] ==  "female"][["math score","reading score","writing score"]]
    print(f"Avg Male Math Score : {male_scores["math score"].mean():.2f}")
    print(f"Avg Male Reading Score : {male_scores["reading score"].mean():.2f}")
    print(f"Avg Male Writing Score : {male_scores["writing score"].mean():.2f}")
    print(f"Avg Female Math Score : {female_scores["math score"].mean():.2f}")
    print(f"Avg Female Reading Score : {female_scores["reading score"].mean():.2f}")
    print(f"Avg Female Writing Score : {female_scores["writing score"].mean():.2f}")

import pandas as pd
#avg_scores(pd.read_csv(f"data\StudentsPerformance.csv"))
avg_scores_gender(pd.read_csv(f"data\StudentsPerformance.csv"))