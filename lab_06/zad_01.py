import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

"""
how titanic.csv looks like:
"","Class","Sex","Age","Survived"
"1","3rd","Male","Child","No"
"2","3rd","Male","Child","No"
"3","3rd","Male","Child","No"
...
"2199","Crew","Female","Adult","Yes"
"2200","Crew","Female","Adult","Yes"
"2201","Crew","Female","Adult","Yes"
"""

# 1. Run the Apriori algorithm on the dataset with sensible parameters (minimum support 0.005) and find frequent itemsets
df = pd.read_csv("./titanic.csv", sep=",")
# We drop the first column, as it is not needed leaving only "Class","Sex","Age","Survived"
df = df.drop(df.columns[0], axis=1)
# One-hot encoding
df_encoded = pd.get_dummies(df)
# The output is a data frame with the support for each itemsets
frequent_itemsets = apriori(df_encoded, min_support=0.005, use_colnames=True)

# 2. Run the association rules algorithm on the dataset with sensible parameters (minimum confidence 0.8)
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.8)
rules = rules.sort_values(by="confidence", ascending=False)

# 3. Find the most interesting rules, especially those indicating who survived and who did not
interesting_rules = rules[
    rules["consequents"].apply(lambda x: "Survived_Yes" in x or "Survived_No" in x)
]
print(interesting_rules)

# 4. Visualize the rules on auxiliary plots
plt.figure(figsize=(10, 5))
plt.scatter(interesting_rules["support"], interesting_rules["confidence"], alpha=0.5)
plt.xlabel("support")
plt.ylabel("confidence")
plt.title("Support vs Confidence")
plt.show()
