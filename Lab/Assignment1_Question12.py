import numpy as np
import matplotlib.pyplot as plt

def normal_pdf(x, mean, variance):
    sigma = np.sqrt(variance) 
    return (1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-((x - mean)**2) / (2 * variance))

x = np.linspace(-5, 5, 500) 
parameters = [
    {"mean": 0, "variance": 1, "label": "μ=0, σ²=1"},
    {"mean": 0, "variance": 0.2, "label": "μ=0, σ²=0.2"},
    {"mean": 2, "variance": 0.5, "label": "μ=2, σ²=0.5"},
    {"mean": -2, "variance": 0.5, "label": "μ=-2, σ²=0.5"},
]

# Plot all PDFs
plt.figure(figsize=(10, 6))
for param in parameters:
    mean = param["mean"]
    variance = param["variance"]
    y = normal_pdf(x, mean, variance)
    plt.plot(x, y, label=param["label"])

plt.title("Probability Density Function of Normal Distribution", fontsize=14)
plt.xlabel("x", fontsize=12)
plt.ylabel("f(x|μ, σ²)", fontsize=12)
plt.axhline(0, color='black', linewidth=0.5, linestyle="--")  
plt.axvline(0, color='black', linewidth=0.5, linestyle="--") 
plt.legend(fontsize=10)
plt.grid(True)

# Show the plot
plt.show()
