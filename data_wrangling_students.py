import pandas as pd

# Dataset laden
df = pd.read_csv("StudentsPerformance.csv")

# -------------------------
# Missing Values Handling
# Leere Werte entfernen
# -------------------------
df = df.dropna()

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

# Convert average to integer
df["average"] = df["average"].astype(int)

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
