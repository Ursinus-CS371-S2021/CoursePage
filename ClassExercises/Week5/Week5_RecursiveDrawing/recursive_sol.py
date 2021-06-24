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
    if depth < MAX_DEPTH:
        draw_triangle(x0, y0, x1, y1, x2, y2)
        ax = (x0+x2)/2
        bx = (x1+x2)/2
        cx = (x0+x1)/2
        ay = (y0+y2)/2
        by = (y1+y2)/2
        cy = (y0+y1)/2
        #draw_triangle(x0, y0, x1, y1, x2, y2, "black", linewidth)
        draw_sierpinski(x0, y0, ax, ay, cx, cy, depth+1)
        draw_sierpinski(ax, ay, x2, y2, bx, by, depth+1)
        draw_sierpinski(cx, cy, bx, by, x1, y1, depth+1)

plt.figure(figsize=(10, 10))
draw_sierpinski(0, 0, 1, 0, 0.5, 1)
plt.savefig("Sierpinski.png", bbox_inches='tight')