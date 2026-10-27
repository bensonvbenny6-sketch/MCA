import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
X = np.array([[1,2,3],[4,5,6],[7,8,9]])
Y = np.array([1,0,1])
model = LinearRegression()
model.fit(X,Y)
y_pred = model.predict(X)
