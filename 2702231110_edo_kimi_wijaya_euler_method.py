# -*- coding: utf-8 -*-
"""2702231110 - Edo Kimi WIjaya - Euler_Method.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WzGd4kwQ8gO1FlZiqUZ3m1B54T0MAngI
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-poster')
# %matplotlib inline

# Define parameters
f = lambda t, s: np.exp(-t) # ODE
h = 0.1 # Step size
t = np.arange(0, 1 + h, h) # Numerical grid
s0 = -1 # Initial Condition

# Explicit Euler Method
s = np.zeros(len(t))
s[0] = s0

for i in range(0, len(t) - 1):
    s[i + 1] = s[i] + h*f(t[i], s[i])

plt.figure(figsize = (12, 8))
plt.plot(t, s, 'bo--', label='Approximate')
plt.plot(t, -np.exp(-t), 'g', label='Exact')
plt.title('Approximate and Exact Solution \n for Simple ODE')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.grid()
plt.legend(loc='lower right')
plt.show()

h = 0.01 # Step size
t = np.arange(0, 1 + h, h) # Numerical grid
s0 = -1 # Initial Condition

# Explicit Euler Method
s = np.zeros(len(t))
s[0] = s0

for i in range(0, len(t) - 1):
    s[i + 1] = s[i] + h*f(t[i], s[i])

plt.figure(figsize = (12, 8))
plt.plot(t, s, 'b--', label='Approximate')
plt.plot(t, -np.exp(-t), 'g', label='Exact')
plt.title('Approximate and Exact Solution \n for Simple ODE')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.grid()
plt.legend(loc='lower right')
plt.show()

import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-poster')

# Define the function for the differential equation y' + 4y = x^2
def f(x, y):
    return x**2 - 4*y

# Parameters
h = 0.1  # Step size
x = np.arange(0, 1 + h, h)  # Numerical grid
y0 = 1  # Initial Condition

# Explicit Euler Method
y = np.zeros(len(x))
y[0] = y0

for i in range(len(x) - 1):
    y[i + 1] = y[i] + h * f(x[i], y[i])

# Exact Solution
exact_y = (31/32) * np.exp(-4*x) + (1/4) * x**2 - (1/8) * x + (1/32)

# Plotting
plt.figure(figsize=(12, 8))
plt.plot(x, y, 'bo--', label='Approximate')
plt.plot(x, exact_y, 'g', label='Exact')
plt.title('Approximate and Exact Solution \n for the ODE y\' + 4y = x^2')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.grid()
plt.legend(loc='upper left')
plt.show()

import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-poster')
# %matplotlib inline  # Uncomment this line if running in a Jupyter Notebook

# Define the function for the ODE dy/dx = sin(y)
f = lambda x, y: np.sin(y)

# Step size
h = 0.1

# Numerical grid
x = np.arange(0, 0.5 + h, h)

# Initial condition
y0 = 1

# Explicit Euler Method
y = np.zeros(len(x))
y[0] = y0

for i in range(0, len(x) - 1):
    y[i + 1] = y[i] + h * f(x[i], y[i])
    y[i + 1] = round(y[i + 1], 4)  # Keep four decimal places

# Plotting
plt.figure(figsize=(12, 8))
plt.plot(x, y, 'bo--', label='Approximate')
plt.title('Approximate Solution for dy/dx = sin(y)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.legend(loc='lower right')
plt.show()

# Print results with four decimal places
for i in range(len(x)):
    print(f"x = {x[i]:.1f}, y = {y[i]:.4f}")