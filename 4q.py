import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split, cross_val_score,learning_curve

# Your existing code continues here...
X, y = load_iris(return_X_y=True)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=.2, random_state=42)
m = DecisionTreeClassifier(max_depth=3)
m.fit(Xtr, ytr)
print("Test Accuracy:", m.score(Xte, yte))
print("CV Accuracy:", cross_val_score(m, X, y, cv=5).mean())
size, train, test = learning_curve(m, X, y, cv=5)
plt.plot(size, train.mean(axis=1), label="Training")
plt.plot(size, test.mean(axis=1), label="Validation")
plt.xlabel("Training Size")
plt.ylabel("Accuracy")
plt.legend()
plt.savefig('plot.png')  # Saves the figure
plt.close()