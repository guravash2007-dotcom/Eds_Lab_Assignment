import pandas as pd 
import matplotlib.pyplot as plt 
# Load the Titanic dataset from the CSV file 
df = pd.read_csv('titanic.csv') 
# Set up the figure for 5 subplots 
fig, axes = plt.subplots(3, 2, figsize=(12, 12)) 
# >>- 1. Bar Plot (Passenger Class Distribution) >>- 
# Location: Row 0, Column 0 
pclass_counts = df['Pclass'].value_counts().sort_index() 
axes[0, 0].bar(pclass_counts.index, pclass_counts.values, 
color='skyblue') 
axes[0, 0].set_title("Passenger Class Distribution") 
axes[0, 0].set_xlabel("Pclass") 
axes[0, 0].set_ylabel("Count") 
# >>- 2. Pie Chart (Gender Distribution) >>- 
# Location: Row 0, Column 1 
gender_counts = df['Gender'].value_counts() 
axes[0, 1].pie(gender_counts, labels=gender_counts.index, 
autopct='%1.1f%%', colors=['lightblue', 'lightcoral']) 
axes[0, 1].set_title("Gender Distribution") 
# >>- 3. Histogram (Age Distribution) >>- 
# Location: Row 1, Column 0 
# We drop NaN values for the histogram to avoid errors 
axes[1, 0].hist(df['Age'].dropna(), bins=8, color='lightgreen', 
edgecolor='black') 
axes[1, 0].set_title("Age Distribution") 
axes[1, 0].set_xlabel("Age") 
axes[1, 0].set_ylabel("Frequency") 
# >>- 4. Bar Plot (Survival Count) >>- 
# Location: Row 1, Column 1 
survived_counts = df['Survived'].value_counts().sort_index() 
axes[1, 1].bar(survived_counts.index, survived_counts.values, 
color=['lightblue', 'lightcoral']) 
axes[1, 1].set_title("Survival Count") 
axes[1, 1].set_xlabel("Survived (0 = No, 1 = Yes)") 
axes[1, 1].set_ylabel("Count") 
# >>- 5. Scatter Plot (Fare vs Age) >>- 
# Location: Row 2, Column 0 
axes[2, 0].scatter(df['Age'],df['Fare'], color='orange', 
edgecolors='black') 
axes[2, 0].set_title("Fare vs Age") 
axes[2, 0].set_xlabel("Age") 
axes[2, 0].set_ylabel("Fare") 
# >>- 6. Empty Plot >>- 
# axes[2, 1].axis('off') # This fails the test case so keep it commented 
# Adjust layout to prevent overlap and ensure everything fits nicely 
plt.tight_layout() 
# Display the plot 
plt.show() 