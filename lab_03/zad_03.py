import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import GaussianNB

df = pd.read_csv("iris.csv")

(train_set, test_set) = train_test_split(df.values, train_size=0.7, random_state=278816)


def test_classifier(classifier, name):
    classifier.fit(train_set[:, :-1], train_set[:, -1])
    print(name)
    print(
        "Dokładność: ", classifier.score(test_set[:, :-1], test_set[:, -1]) * 100, "%"
    )
    print("Macierz błędów:")
    print(confusion_matrix(test_set[:, -1], classifier.predict(test_set[:, :-1])))
    print()


knn3 = KNeighborsClassifier(n_neighbors=3)
test_classifier(knn3, "k-NN, k=3")

knn5 = KNeighborsClassifier(n_neighbors=5)
test_classifier(knn5, "k-NN, k=5")

knn11 = KNeighborsClassifier(n_neighbors=11)
test_classifier(knn11, "k-NN, k=11")

nb = GaussianNB()
test_classifier(nb, "Naive Bayes")

# Output:
# k-NN, k=3
# Dokładność:  95.56 %
# Macierz błędów:
# [[15  0  0]
#  [ 0 14  1]
#  [ 0  1 14]]
# k-NN, k=5
# Dokładność:  95.56 %
# Macierz błędów:
# [[15  0  0]
#  [ 0 14  1]
#  [ 0  1 14]]
# k-NN, k=11
# Dokładność:  95.56 %
# Macierz błędów:
# [[15  0  0]
#  [ 0 14  1]
#  [ 0  1 14]]
# Naive Bayes
# Dokładność:  91.11 %
# Macierz błędów:
# [[15  0  0]
#  [ 0 14  1]
#  [ 0  1 14]]
