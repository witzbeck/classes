# Alex Beckwith
# Set Operations

union = lambda x, y: list(set(list(x) + list(y)))

intersection = lambda x, y: [z for z in union(x, y) if (z in x and z in y)]

complement = lambda x, y: [z for z in y if z not in x]

def disjoint(list1: list, list2: list):
    sction = intersection(list1, list2)
    if len(sction) == 0:
        return True
    else:
        return False