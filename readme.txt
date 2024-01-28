Linear Regression with Gradient Descent
This Python script performs linear regression using gradient descent and visualizes the results using Matplotlib.

Requirements
Python 3.x
NumPy
Matplotlib
Usage
Clone the repository or download the script.
Ensure that you have the required dependencies installed.

pip install numpy matplotlib

Run the script using a Python interpreter.
python linear_regression.py

Description
The script generates synthetic data for a linear relationship with added random noise. It then applies linear regression with gradient descent to find the optimal weights that minimize the mean squared error.

The resulting regression line is plotted along with the data points using Matplotlib.

Parameters
learning_rate: The learning rate for gradient descent.
n_iterations: The number of iterations for gradient descent.
Output
The script outputs a scatter plot of the generated data points and the regression line. The red line represents the linear regression model fitted to the data.