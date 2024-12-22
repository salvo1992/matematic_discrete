import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Polygon, Circle

# Function to add labels and color
def add_labels(ax, x, y, label, color="blue"):
    ax.text(x, y, label, fontsize=14, color=color, ha="center", va="center")

# Function to draw a NOT gate
def draw_not_gate(ax):
    ax.plot([0, 1], [0, 0], color="black")  # Input line
    add_labels(ax, 0.5, 0.2, "A", color="red")
    ax.add_patch(Polygon([[1, -0.5], [2, 0], [1, 0.5]], closed=True, edgecolor="black", facecolor="lightblue"))  # Triangle
    ax.add_patch(Circle((2.2, 0), 0.2, edgecolor="black", facecolor="white"))  # Circle
    ax.plot([2.4, 3], [0, 0], color="black")  # Output line
    add_labels(ax, 2.8, 0.2, "NOT A", color="green")
    ax.text(1.5, -1.5, "NOT: Output is the inverse of input", fontsize=10, ha="center")

# Function to draw an AND gate
def draw_and_gate(ax):
    ax.plot([0, 1], [1, 1], color="black")  # Input line 1
    add_labels(ax, 0.5, 1.2, "A", color="red")
    ax.plot([0, 1], [-1, -1], color="black")  # Input line 2
    add_labels(ax, 0.5, -0.8, "B", color="red")
    ax.add_patch(Polygon([[1, -1.5], [1, 1.5], [2, 1.5], [2, -1.5]], closed=True, edgecolor="black", facecolor="lightblue"))  # Rectangle
    ax.add_patch(Ellipse((2, 0), 1, 3, edgecolor="black", facecolor="lightblue"))  # Semicircle
    ax.plot([2.5, 3], [0, 0], color="black")  # Output line
    add_labels(ax, 2.8, 0.2, "A AND B", color="green")
    ax.text(1.5, -2, "AND: Output is 1 if both inputs are 1", fontsize=10, ha="center")

# Function to draw an OR gate
def draw_or_gate(ax):
    ax.plot([0, 1], [1, 1], color="black")  # Input line 1
    add_labels(ax, 0.5, 1.2, "A", color="red")
    ax.plot([0, 1], [-1, -1], color="black")  # Input line 2
    add_labels(ax, 0.5, -0.8, "B", color="red")
    ax.add_patch(Polygon([[1, -1.5], [1, 1.5], [2, 0]], closed=True, edgecolor="black", facecolor="lightblue"))  # Triangle
    ax.add_patch(Ellipse((2.5, 0), 1, 3, edgecolor="black", facecolor="lightblue"))  # Rounded part
    ax.plot([3.5, 4], [0, 0], color="black")  # Output line
    add_labels(ax, 3.8, 0.2, "A OR B", color="green")
    ax.text(2, -2, "OR: Output is 1 if at least one input is 1", fontsize=10, ha="center")

# Function to draw a NAND gate
def draw_nand_gate(ax):
    draw_and_gate(ax)  # Base AND gate
    ax.add_patch(Circle((2.5, 0), 0.2, edgecolor="black", facecolor="white"))  # Circle for NOT
    ax.plot([2.7, 3.2], [0, 0], color="black")  # Output line
    add_labels(ax, 3.1, 0.2, "NOT (A AND B)", color="green")
    ax.text(1.5, -2, "NAND: Output is 1 unless both inputs are 1", fontsize=10, ha="center")

# Function to draw a NOR gate
def draw_nor_gate(ax):
    draw_or_gate(ax)  # Base OR gate
    ax.add_patch(Circle((3.5, 0), 0.2, edgecolor="black", facecolor="white"))  # Circle for NOT
    ax.plot([3.7, 4.2], [0, 0], color="black")  # Output line
    add_labels(ax, 4.1, 0.2, "NOT (A OR B)", color="green")
    ax.text(2.5, -2, "NOR: Output is 1 if both inputs are 0", fontsize=10, ha="center")

# Function to draw an XOR gate
def draw_xor_gate(ax):
    ax.plot([0, 1], [1, 1], color="black")  # Input line 1
    add_labels(ax, 0.5, 1.2, "A", color="red")
    ax.plot([0, 1], [-1, -1], color="black")  # Input line 2
    add_labels(ax, 0.5, -0.8, "B", color="red")
    ax.add_patch(Polygon([[1.2, -1.5], [1.2, 1.5], [2, 0]], closed=True, edgecolor="black", facecolor="lightblue"))  # Triangle
    ax.add_patch(Ellipse((2.5, 0), 1, 3, edgecolor="black", facecolor="lightblue"))  # Rounded part
    ax.add_patch(Ellipse((1, 0), 0.5, 3, edgecolor="black", linestyle="dotted", facecolor="none"))  # Extra curve
    ax.plot([3.5, 4], [0, 0], color="black")  # Output line
    add_labels(ax, 3.8, 0.2, "A XOR B", color="green")
    ax.text(2, -2, "XOR: Output is 1 if inputs are different", fontsize=10, ha="center")

# Function to draw an XNOR gate
def draw_xnor_gate(ax):
    draw_xor_gate(ax)  # Base XOR gate
    ax.add_patch(Circle((3.5, 0), 0.2, edgecolor="black", facecolor="white"))  # Circle for NOT
    ax.plot([3.7, 4.2], [0, 0], color="black")  # Output line
    add_labels(ax, 4.1, 0.2, "NOT (A XOR B)", color="green")
    ax.text(2.5, -2, "XNOR: Output is 1 if inputs are the same", fontsize=10, ha="center")

# Set up the figure
fig, axes = plt.subplots(2, 3, figsize=(18, 10))
axes = axes.flatten()
for ax in axes:
    ax.set_xlim(-1, 5)
    ax.set_ylim(-3, 3)
    ax.axis("off")

# Draw gates
draw_not_gate(axes[0])
draw_and_gate(axes[1])
draw_or_gate(axes[2])
draw_nand_gate(axes[3])
draw_nor_gate(axes[4])
draw_xnor_gate(axes[5])

plt.tight_layout()
plt.show()



#Ecco i diagrammi delle porte logiche con etichette, colori e spiegazioni:

# NOT Gate:

# Inverte l'ingresso (
# NOT A
# NOT A).
# Uscita alta se l'ingresso è basso e viceversa.
# AND Gate:

# Restituisce 
# 1
# 1 solo se entrambi gli ingressi sono 
# 1
# 1 (
# 𝐴
#  AND 
# 𝐵
# A AND B).
# OR Gate:

# Restituisce 
# 1
# 1 se almeno uno degli ingressi è 
# 1
# 1 (
# 𝐴
#  OR 
# 𝐵
# A OR B).
# NAND Gate:

# L'inverso della porta AND (
# NOT (A AND B)
# NOT (A AND B)).
# Restituisce 
# 1
# 1 a meno che entrambi gli ingressi siano 
# 1
# 1.
# NOR Gate:

# L'inverso della porta OR (
# NOT (A OR B)
# NOT (A OR B)).
# Restituisce 
# 1
# 1 solo se entrambi gli ingressi sono 
# 0
# 0.
# XNOR Gate:

# L'inverso della porta XOR (
# NOT (A XOR B)
# NOT (A XOR B)).
# Restituisce 
# 1
# 1 se gli ingressi sono uguali.