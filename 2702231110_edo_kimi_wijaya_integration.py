# -*- coding: utf-8 -*-
"""2702231110 - Edo Kimi Wijaya - Integration.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1r-tcgsNFSWLO9Fs4oE9MHXQohepnAZYq

Riemann
"""

import numpy as np


a = 0
b = np.pi
n = 11
h = (b - a) / (n - 1)
x = np.linspace(a, b, n)
f = np.sin(x)

I_riemannL = h * sum(f[:n-1])
err_riemannL = 2 - I_riemannL

I_riemannR = h * sum(f[1::])
err_riemannR = 2 - I_riemannR

I_mid = h * sum(np.sin((x[:n-1] \
                        + x[1:]) /2))
err_mid = 2 - I_mid

print(I_riemannL)
print(err_riemannL)

print(I_riemannR)
print(err_riemannR)

print(I_mid)
print(err_mid)

"""Trapezoid"""

import  numpy as np

a = 0
b = np.pi
n = 11
h = (b - a) / (n - 1)
x = np.linspace(a, b, n)
f = np.sin(x)

I_trap = (h/2)*(f[0] + \
                2 * sum(f[1:n-1]) +f[n-1])
err_trap = 2 - I_trap

print(I_trap)
print(err_trap)

import  numpy as np
from scipy.integrate import trapz

a = 0
b = np.pi
n = 11
h = (b - a) / (n - 1)
x = np.linspace(a, b, n)
f = np.sin(x)

I_trapz = trapz(f, x)
I_trap = (h/2)*(f[0] + 2 * sum(f[1:n-1]) + f[n-1])

print(I_trapz)
print(I_trap)

"""Simpson"""

from scipy.integrate import quad

I_quad, est_err_quad = \
          quad(np.sin, 0, np.pi)
print(I_quad)
err_quad = 2 - I_quad
print(est_err_quad, err_quad)

import numpy as np

def composite_trapezoid_rule(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    I_trap = (h / 2) * (y[0] + 2 * sum(y[1:-1]) + y[-1])
    return I_trap

# Function to integrate
f = np.sin

# Integration bounds
a = 0
b = np.pi

# Number of panels
n1 = 8
n2 = 16

# Composite trapezoid rule with 8 panels
I_trap_8 = composite_trapezoid_rule(f, a, b, n1)
err_trap_8 = 2 - I_trap_8

# Composite trapezoid rule with 16 panels
I_trap_16 = composite_trapezoid_rule(f, a, b, n2)
err_trap_16 = 2 - I_trap_16

print(f"Integral approximation with 8 panels: {I_trap_8}, Error: {err_trap_8}")
print(f"Integral approximation with 16 panels: {I_trap_16}, Error: {err_trap_16}")