# Student Performance Data Wrangling

This project demonstrates data wrangling techniques using Python and pandas.

## Techniques Used
- Handling missing values
- Data transformation (average score per student)
- Pivoting (Wide → Long)
- Normalization (splitting into a students table and a scores table)
- Merging datasets

## Dataset
[Students Performance in Exams](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams) (Kaggle).
Download `StudentsPerformance.csv` and place it next to the script.

## Run
```bash
pip install -r requirements.txt
python data_wrangling_students.py
```

The script prints a preview of each table and saves them as CSV files in `output/`.
