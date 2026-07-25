import pandas as pd

data = pd.read_csv(r"C:\Users\Windows 11 Pro\noushin\project\internship\student_scores.csv")

print("First Five Rows")
print(data.head())

print("\nLast Five Rows")
print(data.tail())
