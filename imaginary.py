import matplotlib.pyplot as plt
import numpy as np
#---------------------------------#
def f(z):
    z ** 2 + 1
#---------------------------------#
x = np.linspace(-5, 5, 999)
y = np.linspace(-5, 5, 999)
X, Y = np.meshgrid(x, y)
Z = X + 1j * Y
#---------------------------------#
F = f(Z)
#---------------------------------#
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, np.real(F), cmap='viridis')
#---------------------------------#
ax.set_xlabel('Re(x)')
ax.set_ylabel('Im(x)')
ax.set_zlabel('Re(f(x))')
ax.set_title('x^2+1 extended to the complex plane')
#---------------------------------#
plt.show()
#---------------------------------#

