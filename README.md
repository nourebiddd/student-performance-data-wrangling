# Student Performance Data Wrangling

![Python](https://img.shields.io/badge/Python-3-3776AB?logo=python&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-2.x-150458?logo=pandas&logoColor=white)

This project demonstrates data wrangling techniques using Python and pandas: it takes one flat exam-results table and turns it into clean, normalized tables plus a long-format table ready for plotting or a database.

## Pipeline
```
StudentsPerformance.csv
   → drop missing values, add student_id
   → feature: average score per student
   → wide → long (one row per student × subject)
   → normalize into students + scores tables
   → merge back and verify
   → output/*.csv
```

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
