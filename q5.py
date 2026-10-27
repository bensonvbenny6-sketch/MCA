from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, precision_score, recall_score
X, y = load_iris(return_X_y=True)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=.2, random_state=42)
m = GaussianNB()
m.fit(Xtr, ytr)
p = m.predict(Xte)
print("Accuracy:", accuracy_score(yte, p))
print("Precision:", precision_score(yte, p, average="weighted"))
print("Recall:", recall_score(yte, p, average="weighted"))