import pandas as pd
from sklearn.model_selection import train_test_split

"""
Liczba poprawnych predykcji:  43
Dokładność:  95.56 %
"""

df = pd.read_csv("iris.csv")

(train_set, test_set) = train_test_split(df.values, train_size=0.7, random_state=278816)


def classify_iris(sl, sw, pl, pw):
    if pw < 1 and pl < 2.5:
        return "Setosa"
    elif (pl >= 5 and pw > 1.5) or pl >= 5 or sl >= 7:
        return "Virginica"
    else:
        return "Versicolor"


good_predictions = 0
length = test_set.shape[0]

for i in range(length):
    if (
        classify_iris(test_set[i, 0], test_set[i, 1], test_set[i, 2], test_set[i, 3])
        == test_set[i, 4]
    ):
        good_predictions += 1

print("Liczba poprawnych predykcji: ", good_predictions)
print("Dokładność: ", round(good_predictions / length * 100, 2), "%")
