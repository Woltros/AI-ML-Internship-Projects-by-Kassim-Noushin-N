import pandas as pd
from sklearn.model_selection import train_test_split

# Load dataset
data = pd.read_csv("student_scores.csv")

# Input and Output
X = data[["Hours"]]
y = data["Score"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training Data")
print(X_train)

print("\nTesting Data")
print(X_test)