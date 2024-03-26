from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler

iris = load_iris()
train_data, test_data, train_labels, test_labels = train_test_split(
    iris.data, iris.target, test_size=0.7, random_state=42
)

# c)
scaler = StandardScaler()
train_data = scaler.fit_transform(train_data)
test_data = scaler.transform(test_data)

# d)
mlp = MLPClassifier(hidden_layer_sizes=(2), max_iter=2000)
mlp.fit(train_data, train_labels)

# e)
predictions = mlp.predict(test_data)
print(
    "Accuracy with 2 neurons in hidden layer: ",
    accuracy_score(test_labels, predictions),
)

# f)
mlp = MLPClassifier(hidden_layer_sizes=(3), max_iter=2000)
mlp.fit(train_data, train_labels)
predictions = mlp.predict(test_data)
print(
    "Accuracy with 3 neurons in hidden layer: ",
    accuracy_score(test_labels, predictions),
)

# g)
mlp = MLPClassifier(hidden_layer_sizes=(3, 3), max_iter=2000)
mlp.fit(train_data, train_labels)
predictions = mlp.predict(test_data)
print(
    "Accuracy with two hidden layers, each with 3 neurons: ",
    accuracy_score(test_labels, predictions),
)
