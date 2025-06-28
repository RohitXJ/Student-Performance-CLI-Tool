import pandas as pd

def top_5(df):
    df['Total Score'] = df['math score'] + df['reading score'] + df['writing score']

    top_5_scores = df.sort_values(by='Total Score', ascending=False)['Total Score'].head(5).tolist()

    print(f"Top 5 Students by Total Score : {top_5_scores}")

#top_5(pd.read_csv(r"data\StudentsPerformance.csv"))