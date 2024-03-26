import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler

# a)
diabetes = pd.read_csv("diabetes.csv")
X = diabetes.drop("class", axis=1)
y = diabetes["class"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# b)
mlp = MLPClassifier(
    hidden_layer_sizes=(6, 3), random_state=45, max_iter=500, activation="relu"
)

# c)
mlp.fit(X_train, y_train)

# d)
predictions = mlp.predict(X_test)
print("Accuracy: ", accuracy_score(y_test, predictions))
print("Confusion Matrix: \n", confusion_matrix(y_test, predictions))

"""
Wynik Accuracy wynosi 0.7272727272727273, co oznacza, że model jest
w stanie poprawnie sklasyfikować 72.73% próbek. Zmieniając parametry
nie zaobserwowałem znaczącej poprawy wyniku.

W moim przypadku confusion matrix wygląda następująco:
[[119  32]
 [ 33  47]]
Z tego wynika, że mamy 32 False Positives i 33 False Negatives.
W tym przypadku False Negatives są bardziej niebezpieczne, ponieważ 
pacjent nie otrzymuje leczenia.
"""
