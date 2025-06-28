def eval(df):
    df['Total Score'] = df['math score'] + df['reading score'] + df['writing score']
    df['Pass/Fail'] = df['Total Score'].apply(lambda x: 'Pass' if x >= 120 else 'Fail')
    pass_fail_counts = df['Pass/Fail'].value_counts().to_dict()

    print(f"Pass/Fail Counts: {pass_fail_counts}")
    print(f"Pass Percentage: {pass_fail_counts['Pass'] / len(df) * 100:.2f}%")
    print(f"Fail Percentage: {pass_fail_counts['Fail'] / len(df) * 100:.2f}%")

import pandas as pd
#eval(pd.read_csv(r"data\StudentsPerformance.csv"))
