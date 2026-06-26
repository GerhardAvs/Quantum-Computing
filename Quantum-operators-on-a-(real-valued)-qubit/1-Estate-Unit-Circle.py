import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# ----------------------------
# Configuración de la esfera
# ----------------------------
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# esfera
u = np.linspace(0, 2*np.pi, 100)
v = np.linspace(0, np.pi, 100)

x = np.outer(np.cos(u), np.sin(v))
y = np.outer(np.sin(u), np.sin(v))
z = np.outer(np.ones_like(u), np.cos(v))

ax.plot_surface(x, y, z, color='lightgray', alpha=0.2, edgecolor='none')

# ----------------------------
# Ejes
# ----------------------------
ax.quiver(0,0,0, 1,0,0, color='black')  # X
ax.quiver(0,0,0, 0,1,0, color='black')  # Y
ax.quiver(0,0,0, 0,0,1, color='black')  # Z

# ----------------------------
# Estados cuánticos
# ----------------------------

# |0> (polo norte)
ax.scatter(0,0,1, color='blue', s=80)
ax.text(0, 0, 1.1, r'$|0\rangle$', fontsize=12)

# |1> (polo sur)
ax.scatter(0,0,-1, color='red', s=80)
ax.text(0, 0, -1.2, r'$|1\rangle$', fontsize=12)

# |-> = (|0> - |1>)/sqrt(2) -> eje X negativo
ax.scatter(-1,0,0, color='green', s=80)
ax.text(-1.1, 0, 0, r'$|-\rangle$', fontsize=12)

# ----------------------------
# Ajustes visuales
# ----------------------------
ax.set_xlim([-1,1])
ax.set_ylim([-1,1])
ax.set_zlim([-1,1])

ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])

ax.set_title("Bloch Sphere - States |0>, |1>, |->")

plt.show()