import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load dataset
data = pd.read_csv("student_scores.csv")

X = data[["Hours"]]
y = data["Score"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict score
hours = [[7]]

prediction = model.predict(hours)

print("Study Hours:", hours[0][0])
print("Predicted Score:", round(prediction[0], 2))