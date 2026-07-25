import pandas as pd

data = pd.read_csv(r"C:\Users\Windows 11 Pro\noushin\project\internship\student_scores.csv")

print("Rows and Columns:")
print(data.shape)

print("\nColumn Names:")
print(data.columns)

print("\nRow Index:")
print(data.index)