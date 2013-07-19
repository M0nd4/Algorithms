## Randomized Contraction Algorithm to find the smallest cuts in 
## primitive graph data
## Pseudocode:
##
##  While there are more than 2 vertices:
##   -pick a remaining edge (u,v) uniformly at random
##   -Do contraction: merge u,v into a single vertex that represents
##   -both of them
##   -remove self-loops
##  Return cut represented by final two vertices
lines = [line.strip() for line in open('kargerMinCut.txt')]
lines = [[int(j) for j in i.split()] for i in lines]

import random    

def graph_contract(adj_list, a, b):
    """
    Contracts vertices a and b in a graph to a single vertex, pruning any
    self-loops.
    """
    # We're editing in-place, so list indices may not correspond to node
    # labels.
    label_a, label_b = adj_list[a][0], adj_list[b][0]
    # Prune all entries with value (a) from b and vice-versa.
    for i in xrange(adj_list[b].count(label_a)):
        adj_list[b].remove(label_a)
    for i in xrange(adj_list[a].count(label_b)):
        adj_list[a].remove(label_b)

    # Extend entry (a) with values from (b), except b label. Discard entry b.
    adj_list[a].extend(adj_list[b][1:])
    _ = adj_list.pop(b)

    # Replace all references to (b) in adj_list with a. Gotta be a better way
    # to do this.
    for entry in adj_list:
        for i in xrange(entry.count(label_b)):
            entry[entry.index(label_b)] = label_a


def find_min_cut(adj_list):
    min_cut = len(adj_list) ** 2  # Bigger than any cut we might find.

    for iter in xrange(1000000):  # Arbitrary.
        working_list = adj_list
        for node in xrange(len(working_list) - 2):
            random.seed()
            a = random.randrange(len(working_list))

            # Find random entry connected to entry a. This is ugly because
            # list indices don't actually correspond to node labels.
            b = [i[0] for i in working_list].index(random.choice(working_list[a][1:]))

            graph_contract(working_list, a, b)
        assert len(working_list) == 2, "Something went wrong. Don't have 2 nodes."\
                + str(len(working_list))
        assert len(working_list[0]) == len(working_list[1]), "Something went wrong."\
                + " Contracted adjacency list not symmetric: " + str((\
                len(working_list[0]), len(working_list[1])))
        min_cut = min(min_cut, len(working_list[0]) - 1)

    return min_cut

count = 0
while count < 100:
    lines = [line.strip() for line in open('kargerMinCut.txt')]
    lines = [[int(j) for j in i.split()] for i in lines]
    print find_min_cut(lines)
    count += 1
