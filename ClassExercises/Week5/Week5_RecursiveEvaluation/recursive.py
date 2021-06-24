from sys import argv

def g(x, depth=0):
    res = 0
    if x > 0:
        print("  "*depth, "g({}) = 2g({}) + 1".format(x, x-3))
        call = g(x-3, depth+1)
        res = 2*call+1
        print("  "*depth, "g({}) = 2*{} + 1 = {}".format(x, call, res))
    else:
        print("  "*depth, "g({}) = {}".format(x, 3*x))
        res = 3*x
    return res

def h(x, depth=0):
    res = 0
    if x > 5:
        print("  "*depth, "h({}) = h({}) + 1".format(x, x-15))
        call = h(x-15, depth+1)
        res = call + 1
        print("  "*depth, "h({}) = {} + 1 = {}".format(x, call, res))
    elif x >= 0:
        print("  "*depth, "h({}) = {}".format(x, x))
        res = x
    else:
        print("  "*depth, "h({}) = h({})".format(x, x+3))
        call = h(x+3, depth+1)
        print("  "*depth, "h({}) = {}".format(x, call))
    return res

def A(m, n, depth=0):
    res = 0
    if m == 0:
        res = n+1
        print("  "*depth, "A({}, {}) = {}".format(m, n, res))
    elif n == 0:
        print("  "*depth, "A({}, {}) = A({}, {})".format(m, 0, m-1, 1))
        res = A(m-1, 1, depth+1)
        print("  "*depth, "A({}, {}) = A({}, {}) = {}".format(m, 0, m-1, 1, res))
    else:
        print("  "*depth, "A({}, {}) = A({}, A({}, {}))".format(m, n, m-1, m, n-1))
        res1 = A(m, n-1, depth+1)
        print("  "*depth, "A({}, {}) = A({}, A({}, {})) = A({}, {})".format(m, n, m-1, m, n-1, m-1, res1))
        res = A(m-1, res1, depth+1)
        print("  "*depth, "A({}, {}) = A({}, {}) = {}".format(m, n, m-1, res1, res))
    return res

m = int(argv[1])
n = int(argv[2])
A(m, n)
