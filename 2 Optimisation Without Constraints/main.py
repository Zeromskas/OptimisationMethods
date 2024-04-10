import numpy as np #graph points
import matplotlib.pyplot as plt #graphs
from tabulate import tabulate #table
from algorithms import * #import all functions from algorithms.py

def f(x):
	return 1/8*(x[0]**2*x[1]+x[0]*x[1]**2-x[0]*x[1])
def f_gradient(x):
	return [1/8*(2*x[0]*x[1]+x[1]**2-x[1]), 1/8*(x[0]**2+x[0]*2*x[1]-x[0])]

eps=10**(-4)
tableData = [["Algorithm", "Starting point", "Iteracions", "minX", "f(minX)"]]
triangles = []
scatterPoints = []
#let user choose the method by entering number, starting point
#and epsilon
method = int(input("Enter 1 for gradient descent, 2 for steepest descent, 3 for deformed simplex: "))
x1 = float(input("Enter x1 of starting point X0=[x1, x2]: "))
x2 = float(input("Enter x2 of starting point X0=[x1, x2]: "))
X0 = [x1, x2]
if method == 1:
    gamma = float(input("Enter gamma for gradient descent: "))
    x, scatterPoints = gradient_descent(f, f_gradient, X0, gamma, eps)
    tableData.append(["Gradient descent", X0, len(scatterPoints), (x[0], x[1]), x[2]])
elif method == 2:
    x, scatterPoints = fastest_descent(f, f_gradient, X0, eps)
    tableData.append(["Steepest descent", X0, len(scatterPoints), (x[0], x[1]), x[2]])
elif method == 3:
    x, triangles = deformed_simplex(f, X0, 2, eps, 1, 0.5, 2, -0.5)
    tableData.append(["Deformed simplex", X0, len(triangles), (x[0], x[1]), x[2]])

resultTable = tabulate(tableData, headers="firstrow", tablefmt="github")
print(resultTable)

#plotting
if len(triangles) > 0 or len(scatterPoints) > 0:
    l = -0.1 #interval start
    r = 2 #interval end

    x = np.linspace(l, r, 1000)
    y = np.linspace(l, r, 1000)
    z= f([x, y])
    X, Y = np.meshgrid(x, y)
    Z = f([X, Y])

    plt.figure(figsize=(8, 6))
    plt.contour(X, Y, Z, levels=100, alpha = 0.5)
    plt.colorbar(label='z')          
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Gradient descent' if method == 1 else 'Steepest descent' if method == 2 else 'Deformed simplex')
    plt.grid(True)
    plt.axis('equal')
    if len(triangles) > 0:
        for triangle in triangles:
            triangle.append(triangle[0])
            triangle = np.array(triangle)
            plt.plot(triangle[:, 0], triangle[:, 1], 'r-', linewidth=1)
    elif len(scatterPoints) > 0:
        x_values, y_values, z_values = zip(*scatterPoints)
        plt.scatter(x_values, y_values, label='Checkpoints', marker=".")
        plt.scatter(scatterPoints[-1][0], scatterPoints[-1][1], label='mininum', marker="d", color='red') #rezultato atvaizdavimas

    plt.show()
    



