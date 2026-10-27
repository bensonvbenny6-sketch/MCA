import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
X, y = load_iris(return_X_y=True)
X = StandardScaler().fit_transform(X)
for k in range(1, 6):
m = KMeans(n_clusters=k, random_state=42, n_init=10)
m.fit(X)
print(k, m.inertia_)
m = KMeans(n_clusters=3, random_state=42, n_init=10)
c = m.fit_predict(X)
plt.scatter(X[:, 0], X[:, 1], c=c)
plt.title("K-Means Clustering")
plt.show()