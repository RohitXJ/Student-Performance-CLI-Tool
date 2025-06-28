# 📊 Student Performance CLI Tool

A beginner-friendly command-line tool that performs data analysis on a student performance dataset using Python and Pandas. The tool is modular, easy to extend, and great for learning how to build real-world CLI applications.

---

## 📁 Project Structure

```
student-cli-project/
│
├── base_cli.py                  # Main CLI runner (entry point)
├── data/
│   └── StudentsPerformance.csv  # Dataset file
│
├── summary_stats/              # Basic data summaries
│   ├── summary.py              # Dataset overview
│   ├── averages.py             # Avg scores (overall + gender)
│   └── top_scores.py           # Top 5 total scorers
│
├── evaluations/                # Performance evaluation
│   ├── pass_fail.py            # Pass/fail statistics
│   └── prep_impact.py          # Test prep impact
│
├── analytics/                  # Deeper data analysis
│   ├── correlation.py          # Correlation matrix
│   └── filter.py               # (Optional) Custom filtering
│
└── README.md                   # Project info and usage
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/student-cli-project.git
cd student-cli-project
```

### 2. Install Requirements

Make sure you have Python 3 installed. Then install Pandas:

```bash
pip install pandas
```

### 3. Run the CLI

```bash
python base_cli.py --option <option_name>
```

### 🔧 Available Options

| Option Name   | Description                            |
| ------------- | -------------------------------------- |
| `summary`     | Show dataset summary                   |
| `avg_scores`  | Show average scores by subject         |
| `by_gender`   | Show average scores grouped by gender  |
| `top_5`       | Display top 5 students by total score  |
| `pass_stats`  | Show pass/fail statistics              |
| `prep_impact` | Compare scores based on test prep      |
| `correlation` | Show correlation between score columns |

---

## 📦 Sample Usage

```bash
python base_cli.py --option summary
python base_cli.py --option avg_scores
python base_cli.py --option by_gender
python base_cli.py --option top_5
python base_cli.py --option pass_stats
python base_cli.py --option prep_impact
python base_cli.py --option correlation
```

---

## 🙌 Contributing

This is a beginner-level educational project. Feel free to fork, explore, or build on top of this!

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👨‍💻 Author

**Rohit Gomes**
Computer Science Student, AIML specialization
[LinkedIn](https://www.linkedin.com/in/rohit-gomes-12209620a)
