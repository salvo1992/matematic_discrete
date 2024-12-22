import matplotlib.pyplot as plt
import numpy as np

# Generazione dati per la parabola con asse verticale (y = (1/4p)x^2)
x = np.linspace(-10, 10, 400)
p_verticale = 2
y_verticale = (1 / (4 * p_verticale)) * x**2

# Generazione dati per la parabola con asse orizzontale (x = (1/4p)y^2)
y = np.linspace(-10, 10, 400)
p_orizzontale = 2
x_orizzontale = (1 / (4 * p_orizzontale)) * y**2

# Disegno delle parabole
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Parabola con asse verticale
axes[0].plot(x, y_verticale, label=r"$y = \frac{1}{4p}x^2$")
axes[0].scatter(0, 0, color="red", label="Vertice (0, 0)")
axes[0].scatter(0, p_verticale, color="blue", label=f"Fuoco (0, {p_verticale})")
axes[0].hlines(-p_verticale, -10, 10, colors="green", linestyles="dashed", label="Direttrice y=-p")
axes[0].set_title("Parabola con asse verticale")
axes[0].set_xlabel("x")
axes[0].set_ylabel("y")
axes[0].legend()
axes[0].grid()

# Parabola con asse orizzontale
axes[1].plot(x_orizzontale, y, label=r"$x = \frac{1}{4p}y^2$")
axes[1].scatter(0, 0, color="red", label="Vertice (0, 0)")
axes[1].scatter(p_orizzontale, 0, color="blue", label=f"Fuoco ({p_orizzontale}, 0)")
axes[1].vlines(-p_orizzontale, -10, 10, colors="green", linestyles="dashed", label="Direttrice x=-p")
axes[1].set_title("Parabola con asse orizzontale")
axes[1].set_xlabel("x")
axes[1].set_ylabel("y")
axes[1].legend()
axes[1].grid()

plt.tight_layout()
plt.show()
