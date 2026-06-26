import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Arc

# --- función principal ---
def draw_qubit():
    fig, ax = plt.subplots(figsize=(6,6))

    # Círculo unidad
    circle = Circle((0,0), 1, fill=False)
    ax.add_patch(circle)

    # Ejes
    ax.axhline(0, color='black')
    ax.axvline(0, color='black')

    # Vectores base
    ax.arrow(0,0,1,0, head_width=0.05, color='blue')
    ax.text(1.05,0,"|0⟩")

    ax.arrow(0,0,-1,0, head_width=0.05, color='purple')
    ax.text(-1.15,0,"|1⟩")

    ax.arrow(0,0,0,1, head_width=0.05, color='gray')
    ax.text(0,1.05,"|1⟩")

    ax.arrow(0,0,0,-1, head_width=0.05, color='gray')
    ax.text(0,-1.15,"|1⟩")

    # Estado |+>
    x, y = 1/np.sqrt(2), 1/np.sqrt(2)
    ax.arrow(0,0,x,y, head_width=0.05, color='blue')
    ax.text(x+0.05, y+0.05, "|+⟩")

    # Punto del estado
    ax.plot(x, y, 'ro')

    # Ángulo π/4
    arc = Arc((0,0), 0.8, 0.8, angle=0, theta1=0, theta2=45)
    ax.add_patch(arc)
    ax.text(0.2,0.1,"π/4")

    # Ajustes visuales
    ax.set_xlim(-1.2,1.2)
    ax.set_ylim(-1.2,1.2)
    ax.set_aspect('equal')
    plt.grid()

    plt.show()


# --- ejecutar ---
draw_qubit()

#py -3.14 "c:\Users\Gerardo AvSn\OneDrive\Programacion\Quantum-Computing\Quantum-operators-on-a-(real-valued)-qubit\Unit-Circle.py"