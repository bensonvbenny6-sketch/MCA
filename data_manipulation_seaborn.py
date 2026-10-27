import matplotlib.pyplot as plt
import seaborn as sns
iris = sns.load_dataset("iris")
print(iris.head())
sns.scatterplot(x = "sepal_width", y = "sepal_length", hue = "species", data = iris)
plt.savefig("iris_scatterplot.png.png")