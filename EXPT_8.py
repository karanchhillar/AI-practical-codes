import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Sample data
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)  # Independent variable (feature)
y = np.array([2, 3, 4, 5, 7])  # Dependent variable (target)

model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X)

# Printing the coefficients (slope and intercept)
print("Slope (Coefficient):", model.coef_[0])
print("Intercept:", model.intercept_)

# Plot the data and regression line
plt.scatter(X, y, label="Data Points")
plt.plot(X, y_pred, color='red', label="Linear Regression Line")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.title("Linear Regression")
plt.show()
