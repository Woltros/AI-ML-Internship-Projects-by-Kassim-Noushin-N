import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("student_scores.csv")

# Create line chart
plt.plot(data["Name"], data["Math"], marker="o")

# Add title and labels
plt.title("Math Scores")
plt.xlabel("Students")
plt.ylabel("Marks")

# Display chart
plt.show()
