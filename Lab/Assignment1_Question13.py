import numpy as np
import matplotlib.pyplot as plt

# Saturating linear function
def saturating_linear(v):
    if v < -0.5:
        return 0
    elif -0.5 <= v <= 0.5:
        return v + 0.5
    else:
        return 1

v = np.linspace(-5, 5, 1000)
phi_a = [saturating_linear(val) for val in v]

plt.figure(figsize=(8, 6))
plt.plot(v, phi_a, label="Saturating Linear Function")
plt.title("(a) Saturating Linear Function", fontsize=14)
plt.xlabel("v", fontsize=12)
plt.ylabel("ϕ(v)", fontsize=12)
plt.grid(True)
plt.legend()
plt.show()

# Symmetric (bipolar) saturating linear function
def symmetric_saturating_linear(v):
    if v < -1:
        return -1
    elif -1 <= v <= 1:
        return v
    else:
        return 1

phi_b = [symmetric_saturating_linear(val) for val in v]

plt.figure(figsize=(8, 6))
plt.plot(v, phi_b, label="Symmetric Saturating Linear Function", color="orange")
plt.title("(b) Symmetric (Bipolar) Saturating Linear Function", fontsize=14)
plt.xlabel("v", fontsize=12)
plt.ylabel("ϕ(v)", fontsize=12)
plt.grid(True)
plt.legend()
plt.show()

# Binary sigmoid function
def binary_sigmoid(v, alpha):
    return 1 / (1 + np.exp(-alpha * v))

alphas = [0.1, 0.5, 1.0]
plt.figure(figsize=(8, 6))

for alpha in alphas:
    phi_c = binary_sigmoid(v, alpha)
    plt.plot(v, phi_c, label=f"Binary Sigmoid (α={alpha})")

plt.title("(c) Binary Sigmoid Function", fontsize=14)
plt.xlabel("v", fontsize=12)
plt.ylabel("ϕ(v)", fontsize=12)
plt.grid(True)
plt.legend()
plt.show()

# Hyperbolic tangent sigmoid function
def hyperbolic_tangent_sigmoid(v, alpha):
    return (np.exp(alpha * v) - np.exp(-alpha * v)) / (np.exp(alpha * v) + np.exp(-alpha * v))

plt.figure(figsize=(8, 6))

for alpha in alphas:
    phi_d = hyperbolic_tangent_sigmoid(v, alpha)
    plt.plot(v, phi_d, label=f"Hyperbolic Tangent Sigmoid (α={alpha})")

plt.title("(d) Hyperbolic Tangent Sigmoid Function", fontsize=14)
plt.xlabel("v", fontsize=12)
plt.ylabel("ϕ(v)", fontsize=12)
plt.grid(True)
plt.legend()
plt.show()
