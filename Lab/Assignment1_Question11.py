import matplotlib.pyplot as plt
import numpy as np

# Circle parameters
center_x, center_y = 4, 5  
radius = 10 / 2  

theta = np.linspace(0, 2 * np.pi, 100)  
x = center_x + radius * np.cos(theta)  
y = center_y + radius * np.sin(theta) 

plt.figure(figsize=(6, 6))
plt.plot(x, y, label=f"Circle with center ({center_x}, {center_y}) and diameter 10")
plt.scatter(center_x, center_y, color='red', label="Center (4, 5)") 
plt.gca().set_aspect('equal', adjustable='box')  

plt.title("Circle with Diameter 10 and Center at (4, 5)")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.axhline(0, color='black', linewidth=0.5)  
plt.axvline(0, color='black', linewidth=0.5) 
plt.legend()
plt.grid(True)

plt.show()
