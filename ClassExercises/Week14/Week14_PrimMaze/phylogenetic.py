import numpy as np
import matplotlib.pyplot as plt
import json
from unionfind import *

class TreeNode(object):
    """
    Attributes
    ----------
    left: TreeNode
        Left child
    right: TreeNode
        Right child
    sim: int
        Phylogenetic similarity between two children if
        internal node, or max similarity between any two
        nodes if leaf node
    key: string
        Name of species if leaf node
    """

    def __init__(self, key, dist = 0):
        """
        Initialize a tree node
        """
        self.key = key
        self.sim = dist
        self.left = None
        self.right = None
        self.mask = True
    
    def __str__(self):
        """
        String is key if key is not None, or blank otherwise
        """
        return "{}".format(self.key)

    def compute_y_coords(self, maxsim=[0], y=[0]):
        """
        Recursively compute y coordinate of nodes via an inorder
        traversal, while computing the maximum phylogenetic 
        similarity as a side effect

        Parameters
        ----------
        maxsim: list of [int]
            Maximum similarity
        y: list of [int]
            Current y coordinate
        """
        if self.left:
            self.left.compute_y_coords(maxsim, y)
        maxsim[0] = max(maxsim[0], self.sim)
        self.y = y[0]
        y[0] += 1
        if self.right:
            self.right.compute_y_coords(maxsim, y)

    def compute_x_coords(self, maxsim):
        """
        Recursively compute and store the x coordinates
        of all nodes.  If the nodes are internal, then the
        x coordinate is the phylogenetic similarity.
        If the node is a leaf node, then the x coordinate
        is the maximum phylogenetic similarity among all
        internal nodes

        Parameters
        ----------
        maxsim: int
            Maximum phylogenetic similarity across all nodes
        """
        if self.left:
            self.left.compute_x_coords(maxsim)
        if self.right:
            self.right.compute_x_coords(maxsim)
        self.x = self.sim
            

    def draw(self):
        """
        Recursively draw phylogenetic tree.  Assumes that the
        x and y coordinates have been precomputed
        """
        x1, y1 = self.y, self.x
        if self.mask:
            # Draw a dot
            plt.scatter(x1, y1, 50, 'k')
            # Draw some text indicating what the key is
            plt.text(x1+0.02, y1+0.005, "{}".format(self))
        if self.left:
            # Draw a line segment from my node to this left child
            if self.mask and self.left.mask:
                x2, y2 = self.left.y, self.left.x
                plt.plot([x1, x2], [y1, y2], 'k')
            self.left.draw()
        if self.right:
            # Draw a line segment from my node to this right child
            if self.mask and self.right.mask:
                x2, y2 = self.right.y, self.right.x
                plt.plot([x1, x2], [y1, y2], 'k')
            self.right.draw()

class PhyloTree(object):
    def __init__(self):
        self.root = None

    def draw(self, threshold=None):
        """
        Draw the phylogenetic tree from the bottom up

        Parameters
        ----------
        threshold: int
            If specified, draw a vertical line showing a similarity
            threshold for clustering
        """
        if self.root:
            maxsim = [0]
            self.root.compute_y_coords(maxsim)
            self.root.compute_x_coords(maxsim[0])
            self.root.draw()
            ax = plt.gca()
            ax.set_xticks([])
            plt.ylim([-0.1, self.root.x+0.1])
            plt.xlabel("Single-Linkage Clustering")
            plt.tight_layout()


def load_blosum(filename):
    """
    Load in a BLOSUM scoring matrix for Needleman-Wunsch

    Parameters
    ----------
    filename: string
        Path to BLOSUM file
    
    Returns
    -------
    A dictionary of {string: int}
        Key is string, value is score for that particular 
        matching/substitution/deletion
    """
    fin = open(filename)
    lines = [l for l in fin.readlines() if l[0] != "#"]
    fin.close()
    symbols = lines[0].split()
    X = [[int(x) for x in l.split()] for l in lines[1::]]
    X = np.array(X, dtype=int)
    N = X.shape[0]
    costs = {}
    for i in range(N-1):
        for j in range(i, N):
            c = X[i, j]
            if j == N-1:
                costs[symbols[i]] = c
            else:
                costs[symbols[i]+symbols[j]] = c
                costs[symbols[j]+symbols[i]] = c
    return costs
