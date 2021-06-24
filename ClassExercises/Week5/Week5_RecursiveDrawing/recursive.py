import numpy as np
import matplotlib.pyplot as plt

MAX_DEPTH = 8

def draw_triangle(x0, y0, x1, y1, x2, y2, c="C1", linewidth=1):
    """
    Draw a triangle at the specified coordinates
    
    Parameters
    ----------
    x0, y0, x1, y1, x2, y2: Coordinates of points
    c: string
        Color
    linewidth: float
        linewidth of line to draw
    """
    plt.plot([x0, x1], [y0, y1], c, linewidth=linewidth)
    plt.plot([x1, x2], [y1, y2], c, linewidth=linewidth)
    plt.plot([x2, x0], [y2, y0], c, linewidth=linewidth)

def draw_sierpinski(x0, y0, x1, y1, x2, y2, depth=0, linewidth=1):
    """
    Draw a sierpinski triangle at the specified coordinates
    
    Parameters
    ----------
    x0, y0, x1, y1, x2, y2: Coordinates of points
    depth: int
        Depth of the recursion
    linewidth: float
        linewidth of line to draw
    """
    draw_triangle(x0, y0, x1, y1, x2, y2)

plt.figure(figsize=(10, 10))
draw_sierpinski(0, 0, 1, 0, 0.5, 1)
plt.savefig("Sierpinski.png", bbox_inches='tight')