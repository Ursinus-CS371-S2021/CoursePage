import numpy as np

def edit(s1, s2):
    """
    An iterative, dynamic programming version of the string
    edit distance

    Parameters
    ----------
    s1: string of length M
        The first string to match
    s2: string of length N
        The second string to match
    
    Returns
    -------
    cost: int
        The cost of an optimal match
    paths: list of lists
        Each list 
    """
    M = len(s1)
    N = len(s2)
    # Create a 2D array with M+1 rows and N+1 columns
    table = np.zeros((M+1, N+1))
    moves = np.zeros_like(table)
    moves[0, :] = 1
    moves[:, 0] = 2
    # Fill in the base cases
    table[0, :] = np.arange(N+1)
    table[:, 0] = np.arange(M+1)
    for i in range(1, M+1):
        for j in range(1, N+1):
            cost1 = table[i, j-1] + 1 # Delete the last character from s2
            cost2 = table[i-1, j] + 1 # Delete the last character from s1
            cost3 = table[i-1, j-1] # Match or swap both characters at the end
            if s1[i-1] != s2[j-1]:
                cost3 += 1
            moves[i, j] = np.argmin([cost1, cost2, cost3])
            table[i, j] = min(cost1, cost2, cost3)
    cost = int(table[-1, -1])
    i = M
    j = N
    path = []
    verbal = []
    while not (i == 0 and j == 0):
        path.append([i, j])
        if moves[i, j] == 0:
            verbal.append("Add {}".format(s2[j-1]))
            j -= 1
        elif moves[i, j] == 1:
            verbal.append("Delete {}".format(s1[i-1]))
            i -= 1
        else:
            if s1[i-1] != s2[j-1]:
                verbal.append("Swap in an {} for the {}".format(s2[j-1], s1[i-1]))
            else:
                verbal.append("Match {} and {}".format(s1[i-1], s2[j-1]))
            i -= 1
            j -= 1
    verbal.reverse()
    for v in verbal:
        print(v)

edit("school", "fools")