import pandas as pd
import argparse
from summary_stats.avg import avg_scores,avg_scores_gender
from summary_stats.summary import summary
from summary_stats.top_scores import top_5
from evaluations.pass_fail import eval
from evaluations.prep_impact import impact
from analytics.correlation import correlation

df = pd.read_csv(r"data\StudentsPerformance.csv")

# ---- CLI setup ----
parser = argparse.ArgumentParser(description="📊 Student Performance CLI Tool")
parser.add_argument('--option', type=str, help="Choose an option. Use --help to see available options.")

args = parser.parse_args()

# ---- Option handling ----
if args.option == 'summary':
    summary(df)

elif args.option == 'avg_scores':
    avg_scores(df)

elif args.option == 'by_gender':
    avg_scores_gender(df)

elif args.option == 'top_5':
    top_5(df)

elif args.option == 'pass_stats':
    eval(df)

elif args.option == 'prep_impact':
    impact(df)

elif args.option == 'correlation':
    correlation(df)

else:
    print("❌ Invalid option. Available options are:\n"
          "  --option summary\n"
          "  --option avg_scores\n"
          "  --option by_gender\n"
          "  --option top_5\n"
          "  --option pass_stats\n"
          "  --option prep_impact\n"
          "  --option correlation")