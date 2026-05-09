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
# Prepare the data. Group by Sex and Survived, then count the size of 
each group and unstack to get columns for 0 and 1 
survival_gender = data.groupby(['Sex', 'Survived']).size().unstack() 
# Create the stacked bar chart 
ax = survival_gender.plot(kind='bar', stacked=True) 
# Add title and labels 
plt.title("Survival by Gender") 
plt.xlabel("Gender") 
plt.ylabel("Count") 
# Customize Legend 
plt.legend(["Not Survived", "Survived"]) 
# Display the plot 
plt.show() 