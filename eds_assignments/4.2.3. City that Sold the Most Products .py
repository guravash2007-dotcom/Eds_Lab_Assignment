import pandas as pd

# Prompt the user for the file name
file_name = input()

# Load the data
df = pd.read_csv(file_name)
product_city = df.groupby("City")["Quantity"].sum()
best_city = product_city.idxmax()
# Display the result
print(f"City sold the most products: {best_city}")
