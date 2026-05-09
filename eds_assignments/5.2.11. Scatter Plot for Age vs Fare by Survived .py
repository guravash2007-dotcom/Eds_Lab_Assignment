import pandas as pd 
import matplotlib.pyplot as plt 
# Load the Titanic dataset 
data = pd.read_csv('Titanic-Dataset.csv') 
# Data Cleaning 
data['Age'].fillna(data['Age'].median(), inplace=True) 
data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True) 
data.drop('Cabin', axis=1, inplace=True) 
# Convert categorical features to numeric 
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1}) 
data = pd.get_dummies(data, columns=['Embarked'], drop_first=True) 
# Create a color mapping: 0 >> 'red', 1 >> 'blue' 
colors = data['Survived'].map({0: 'red', 1: 'blue'}) 
# Create the scatter plot for Age vs Fare using the c argument for 
colors 
plt.scatter(data['Age'], data['Fare'], c=colors) 
# Add title and labels 
plt.title("Age vs. Fare by Survival") 
plt.xlabel("Age") 
plt.ylabel("Fare") 
# Display the plot 
plt.show()