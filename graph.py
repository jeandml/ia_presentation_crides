import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Ask user for the file name
file_name = input("Enter the name of the .csv file (including the .csv extension): ")

# Step 1: Read the Data
try:
    data = pd.read_csv(file_name)
except FileNotFoundError:
    print(f"File '{file_name}' not found. Please check the file name and try again.")
    exit()

# Step 2: Count the Values
value_counts = data['automated_detection'].value_counts()

# Step 3: Create the Bar Chart
sns.set(style="whitegrid")
plt.figure(figsize=(8, 6))
bar_plot = sns.barplot(x=value_counts.index, y=value_counts.values)

plt.title('Automated Detection Counts')
plt.xlabel('Automated Detection')
plt.ylabel('Count')
plt.xticks(rotation=45)  # Rotates the labels on the X-axis for clarity

# Display the plot
plt.show()
