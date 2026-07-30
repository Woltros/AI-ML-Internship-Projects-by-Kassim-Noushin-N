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

model = LinearRegression()
model.fit(X_train, y_train)

# User input
hours = float(input("Enter study hours: "))

prediction = model.predict([[hours]])

print(f"Predicted Score: {prediction[0]:.2f}")