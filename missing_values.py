import pandas as pd

data = pd.read_csv(r"C:\Users\Windows 11 Pro\noushin\project\internship\student_scores.csv")

print("Missing Values:")
print(data.isnull())

print("\nNumber of Missing Values:")
print(data.isnull().sum())