import pandas as pd
import numpy as np

# Load the Titanic dataset
data = pd.read_csv('Titanic-Dataset.csv')
data['FamilySize'] = data['SibSp'] + data['Parch']
data['IsAlone'] = np.where(data['FamilySize'] > 0, 0, 1)
data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)

# 1. Calculate the survival rate by class
survival_rate = data.groupby("Pclass")["Survived"].mean()
print(survival_rate)

# 2. Calculate the survival rate by embarked location
if "Embarked_S" in data.columns:
	survival_rate_by_embarked_s = data.groupby("Embarked_S")["Survived"].mean()
	print(survival_rate_by_embarked_s)

# 3. Calculate the survival rate by family size
survival_family_size = data.groupby("FamilySize")["Survived"].mean()
print(survival_family_size)

# 4. Calculate the survival rate by being alone
print(data.groupby("IsAlone")["Survived"].mean())

# 5. Get the average fare by class
print(data.groupby("Pclass")["Fare"].mean())

# 6. Get the average age by class
print(data.groupby("Pclass")["Age"].mean())

# 7. Get the average age by survival status
print(data.groupby("Survived")["Age"].mean())

# 8. Get the average fare by survival status
print(data.groupby("Survived")["Fare"].mean())

# 9. Get the number of survivors by class
print(data[data["Survived"] == 1]["Pclass"].value_counts())

# 10. Get the number of non-survivors by class
print(data[data["Survived"]==0]["Pclass"].value_counts())