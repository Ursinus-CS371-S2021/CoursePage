import numpy as np
import matplotlib.pyplot as plt
from unionfind import *

class GraphNode:
    def __init__(self):
        self.edges = []
        self.data = {}

def draw_2d_graph(nodes, edges):
    ax = plt.gca()
    ax.set_facecolor((0.9, 0.9, 0.9))
    for (i, j, d) in edges:
        x1, y1 = nodes[i].data['x'], nodes[i].data['y']
        x2, y2 = nodes[j].data['x'], nodes[j].data['y']
        plt.plot([x1, x2], [y1, y2])
    for i, n in enumerate(nodes):
        plt.scatter(n.data['x'], n.data['y'], 100, c='k')
        plt.text(n.data['x']+0.002, n.data['y']+0.002, "{}".format(i), zorder=10, c='r', fontsize='xx-large')

def dist_of_edge(e):
    return e[2]

def make_grid_graph(N):
    """
    Parameters
    ----------
    N: int
        Resolution of grid
    """
    nodes = []
    for i in range(N):
        for j in range(N):
            n = GraphNode()
            n.data = {'x':j, 'y':i}
            nodes.append(n)
    edges = ()
    neighbs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for i in range(N):
        for j in range(N):
            idx1 = i*N + j
            for [di, dj] in neighbs:
                ii = i + di
                jj = j + dj
                if ii >= 0 and jj >= 0 and ii < N and jj < N:
                    idx2 = ii*N + jj
                    


def get_mst_kruskal(nodes, edges):
    edges = sorted(edges, key = dist_of_edge)
    djset = UFFast(len(nodes))
    new_edges = []
    for e in edges:
        (i, j, d) = e
        if not djset.find(i, j):
            djset.union(i, j)
            new_edges.append(e)
    return new_edges
    


nodes, edges = make_complete_2D_graph(30, 1)
get_mst_kruskal(nodes, edges)
