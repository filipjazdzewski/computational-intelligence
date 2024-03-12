import pandas as pd
from fuzzywuzzy import process

missing_values = ["n/a", "na", "--", "-"]

df = pd.read_csv("iris_with_errors.csv", na_values=missing_values)

# a)
print("Ilość błędów w poszczególnych kolumnach:")
print(df.isnull().sum())

# b)
numeric_columns = ["sepal.length", "sepal.width", "petal.length", "petal.width"]

for column in numeric_columns:
    out_of_range = (df[column] <= 0) | (df[column] >= 15)

    df.loc[out_of_range, column] = pd.NA

    mean_value = round(df[column].mean(), 1)
    df[column].fillna(mean_value, inplace=True)

df.to_csv("iris_task_b.csv", index=False)

# c)
correct_varieties = ["Setosa", "Versicolor", "Virginica"]
print("Poprawne odmiany:", correct_varieties)
incorrect_varieties = [x for x in df["variety"].unique() if x not in correct_varieties]
print("Błędne odmiany:", incorrect_varieties)


def correct_spelling(name):
    if name in correct_varieties:
        return name

    similar_variety = process.extract(name, correct_varieties)
    most_similar_variety, similarity = similar_variety[0]

    if similarity >= 80:
        print(
            f"Poprawiono: {name} -> {most_similar_variety}, podobieństwo: {similarity}%"
        )
        return most_similar_variety
    else:
        return name


df["variety"] = df["variety"].apply(correct_spelling)

df.to_csv("iris_task_c.csv", index=False)
