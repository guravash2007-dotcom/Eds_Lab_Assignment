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
# Create the scatter plot for Age vs Fare 
plt.scatter(data['Age'], data['Fare']) 
# Add title and labels 
plt.title("Age vs. Fare") 
plt.xlabel("Age") 
plt.ylabel("Fare") 
# Display the plot 
plt.show()