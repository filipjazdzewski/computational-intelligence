from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

iris = load_iris()
X = pd.DataFrame(data=iris.data, columns=iris.feature_names)
y = iris.target

target_names = iris.target_names
COLORS = ["navy", "turquoise", "darkorange"]
pca = PCA()

iris_pca = pca.fit_transform(X)

explained_variance_ratio = pca.explained_variance_ratio_
cumulative_variance = explained_variance_ratio.cumsum()

num_components_to_keep = np.argmax(cumulative_variance >= 0.95) + 1

iris_compressed = iris_pca[:, :num_components_to_keep]

print(f"Explained Variance Ratios: {explained_variance_ratio}")
print(f"Cumulative Explained Variance: {cumulative_variance}")
print(f"Number of Components to Keep for 95% Variance: {num_components_to_keep}")

if num_components_to_keep == 2:
    for i, c in zip(range(len(target_names)), COLORS):
        plt.scatter(
            iris_compressed[y == i, 0],
            iris_compressed[y == i, 1],
            c=c,
            label=target_names[i],
        )
    plt.title("PCA - 2D Compression")
    plt.legend()
    plt.show()
elif num_components_to_keep == 3:
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.scatter(
        iris_compressed[:, 0],
        iris_compressed[:, 1],
        iris_compressed[:, 2],
        c=iris.target,
    )
    ax.set_title("PCA - 3D Compression")
    plt.legend()
    plt.show()
