import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load dataset
data = pd.read_csv("student_scores.csv")

# Features and target
X = data[["Hours"]]
y = data["Score"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict scores for different study hours
study_hours = [[3], [5], [7], [9]]

predictions = model.predict(study_hours)

print("Study Hours\tPredicted Score")
for hour, score in zip(study_hours, predictions):
    print(f"{hour[0]}\t\t{score:.2f}")
