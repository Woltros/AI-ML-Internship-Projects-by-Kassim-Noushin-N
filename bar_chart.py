import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("student_scores.csv")

# Create bar chart
plt.bar(data["Name"], data["Science"])

# Add title and labels
plt.title("Science Scores")
plt.xlabel("Students")
plt.ylabel("Marks")

# Display chart
plt.show()