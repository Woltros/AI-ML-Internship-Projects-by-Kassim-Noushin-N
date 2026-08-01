import pandas as pd
from sklearn.linear_model import LinearRegression

# Load dataset
data = pd.read_csv("student_scores.csv")

X = data[["Hours"]]
y = data["Score"]

# Train model
model = LinearRegression()
model.fit(X, y)

while True:
    hours = float(input("Enter Study Hours: "))

    new_data = pd.DataFrame({"Hours": [hours]})
    prediction = model.predict(new_data)

    print("Predicted Score:", round(prediction[0], 2))

    choice = input("\nDo you want to predict again? (y/n): ").lower()

    if choice != "y":
        print("Thank you!")
        break