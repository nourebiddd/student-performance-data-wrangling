import sys
from pathlib import Path

import pandas as pd

# Dataset laden
# Quelle: https://www.kaggle.com/datasets/spscientist/students-performance-in-exams
DATA_FILE = Path(__file__).parent / "StudentsPerformance.csv"
OUTPUT_DIR = Path(__file__).parent / "output"

if not DATA_FILE.exists():
    sys.exit(
        f"{DATA_FILE.name} nicht gefunden. Bitte von Kaggle herunterladen "
        "(siehe README) und neben dieses Skript legen."
    )

df = pd.read_csv(DATA_FILE)

# -------------------------
# Missing Values Handling
# Leere Werte entfernen
# -------------------------
df = df.dropna().reset_index(drop=True)

# -------------------------
# Add Student ID
# -------------------------
df["student_id"] = df.index + 1

# -------------------------
# Transformation
# Durchschnitt berechnen
# -------------------------
df["average"] = (
    df["math score"] +
    df["reading score"] +
    df["writing score"]
) / 3

# Round average to 2 decimals (astype(int) would cut off, e.g. 89.99 -> 89)
df["average"] = df["average"].round(2)

# -------------------------
# Pivoting (Wide -> Long)
# -------------------------
scores_long = df.melt(
    id_vars=["student_id"],
    value_vars=["math score", "reading score", "writing score"],
    var_name="subject",
    value_name="score"
)

# -------------------------
# Normalization
# Tabellen aufteilen
# -------------------------
students = df[[
    "student_id",
    "gender",
    "race/ethnicity",
    "parental level of education",
    "lunch"
]]

scores = df[[
    "student_id",
    "test preparation course",
    "math score",
    "reading score",
    "writing score",
    "average"
]]

# -------------------------
# Merging Tables
# -------------------------
merged = pd.merge(
    students,
    scores,
    on="student_id",
    how="inner"
)

# -------------------------
# Output
# -------------------------
print("Students Table:")
print(students.head())

print("\nScores Table:")
print(scores.head())

print("\nLong Format Scores:")
print(scores_long.head())

print("\nMerged Table:")
print(merged.head())

# -------------------------
# Save results
# -------------------------
OUTPUT_DIR.mkdir(exist_ok=True)
students.to_csv(OUTPUT_DIR / "students.csv", index=False)
scores.to_csv(OUTPUT_DIR / "scores.csv", index=False)
scores_long.to_csv(OUTPUT_DIR / "scores_long.csv", index=False)
merged.to_csv(OUTPUT_DIR / "merged.csv", index=False)
print(f"\nErgebnisse gespeichert in: {OUTPUT_DIR}")
