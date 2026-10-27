from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

X, y = load_iris(return_X_y=True)

Xtr, Xte, ytr, yte = train_test_split(
    X, y, test_size=0.2, random_state=42
)

for k in ["linear", "poly", "rbf"]:
    model = SVC(kernel=k)
    model.fit(Xtr, ytr)
    p = model.predict(Xte)
    print(k, "Accuracy:", accuracy_score(yte, p))
