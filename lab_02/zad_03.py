import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.preprocessing import MinMaxScaler, StandardScaler

iris = datasets.load_iris()
X = iris.data[:, :2]  # sepal length, sepal width
y = iris.target

target_names = iris.target_names
COLORS = ["cornflowerblue", "orange", "green"]


def create_plot(values, title, xlabel, ylabel):
    for i, c in zip(range(len(target_names)), COLORS):
        plt.scatter(values[y == i, 0], values[y == i, 1], c=c, label=target_names[i])
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()


plt.figure(figsize=(15, 5))

# original
plt.subplot(1, 3, 1)
create_plot(X, "Original Database", "Sepal Length (cm)", "Sepal Width (cm)")

# z-score scaled
scaler_zscore = StandardScaler()
X_zscore = scaler_zscore.fit_transform(X)

plt.subplot(1, 3, 2)
create_plot(
    X_zscore, "Z-Score Scaled Database", "Sepal Length (cm)", "Sepal Width (cm)"
)

# min-max normalized
scaler_minmax = MinMaxScaler()
X_minmax = scaler_minmax.fit_transform(X)

plt.subplot(1, 3, 3)
create_plot(
    X_minmax, "Min-Max Scaled Database", "Sepal Length (cm)", "Sepal Width (cm)"
)

plt.tight_layout()
plt.show()
