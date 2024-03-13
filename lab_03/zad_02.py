import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn import tree

df = pd.read_csv("iris.csv")

(train_set, test_set) = train_test_split(df.values, train_size=0.7, random_state=278816)

print("Train set:")
print(train_set)
print("Test set:")
print(test_set)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(train_set[:, :-1], train_set[:, -1])

tree.plot_tree(clf, filled=True)
tree.export_graphviz(clf, out_file="tree.dot")

good_predictions = 0
length = test_set.shape[0]

for i in range(length):
    if clf.predict([test_set[i, :-1]]) == test_set[i, -1]:
        good_predictions += 1

print("Liczba poprawnych predykcji: ", good_predictions)
print("Dokładność: ", round(good_predictions / length * 100, 2), "%")

print("Macierz błędów:")
print(confusion_matrix(test_set[:, -1], clf.predict(test_set[:, :-1])))

print("Remis z zad_01.py: 43/45 = 95.56% vs 43/45 = 95.56%")
