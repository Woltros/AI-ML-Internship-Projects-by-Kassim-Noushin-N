import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("student_scores.csv")

# Create scatter plot
plt.scatter(data["Math"], data["Science"])

# Add title and labels
plt.title("Math vs Science Scores")
plt.xlabel("Math Marks")
plt.ylabel("Science Marks")

# Display chart
plt.show()