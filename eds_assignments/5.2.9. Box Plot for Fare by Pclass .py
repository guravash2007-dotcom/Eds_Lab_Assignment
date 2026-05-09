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
# Create the boxplot for Fare by Pclass 
data.boxplot(column='Fare', by='Pclass') 
# Customize titles and labels 
plt.title("Fare by Pclass") 
plt.suptitle('') # Removes the default "Boxplot grouped by Pclass" 
subtitle 
plt.xlabel("Pclass") 
plt.ylabel("Fare") 
# Display the plot 
plt.show()