import pandas as pd

data = pd.read_csv(r"C:\Users\Windows 11 Pro\noushin\project\internship\student_scores.csv")

print("Original Dataset")
print(data)

data = data.drop_duplicates()

print("\nDataset After Removing Duplicates")
print(data)
