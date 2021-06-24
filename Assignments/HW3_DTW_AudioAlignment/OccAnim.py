import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
N = 40
radius = 5
path = [[0, 0]]
choices = [[0, 1], [1, 0], [1, 1]]
for i in range(0, N):
    p = path[-1]
    di, dj = choices[np.random.randint(3)]
    path.append([p[0]+di, p[1]+dj])
path = np.array(path)
M, N = np.max(path*2, axis=0)+1

plt.figure(figsize=(6, 6))
Occ = np.zeros((M, N))
for i, p in enumerate(path):
    plt.clf()
    i1 = max(p[0]*2-radius, 0)
    i2 = min(p[0]*2+radius+1, M)
    j1 = max(p[1]*2-radius, 0)
    j2 = min(p[1]*2+radius+1, N)
    Occ[i1:i2, j1:j2] = 2
    plt.imshow(Occ)
    plt.scatter(path[0:i+1, 1]*2, path[0:i+1, 0]*2, c='C1')
    plt.scatter([p[1]*2], [p[0]*2], 100, c='C3')
    plt.text(p[1]*2, p[0]*2, "({},{})".format(p[0]*2, p[1]*2))
    plt.title("i = {}, j = {}".format(p[0], p[1]))
    plt.savefig("{}.png".format(i))
    Occ[Occ > 0] = 1