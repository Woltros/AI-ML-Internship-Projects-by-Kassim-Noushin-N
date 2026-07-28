import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load dataset
data = pd.read_csv("student_scores.csv")

# Input and Output
X = data[["Hours"]]
y = data["Score"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Predict score for 7 hours of study
prediction = model.predict([[7]])

print("Predicted Score for 7 Hours of Study:")
print("Predicted Score:", prediction[0])
