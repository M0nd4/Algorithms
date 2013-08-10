## single-source shortest paths
## Input: directed graph G = (V,E). (m = abs(E), n = abs(V))
## - each edge has non-negative length, le
## - source vertex S
##
## Ouput: for each v in V, compute L(v) = length of shortest
##  path s-v in G
##
## Assumptions:
## - there is a path between s and all other vertices (for convenience,
##   otherwise use BFS of DFS to determine reachable parts and delete
##   the rest)
## - no negative edge lengths (important assumption)
## 
##
## Pseudocode:
## Initialize:
##  - X = {s} # the set of vertices processed so far
##  - A[s] = 0 # the computed shortest path
##  - B[s] = empty path # the computed shortest paths (unecessary, for 
##    comprehension only)
##
## Main Loop
##  - while X != V:
##    - among all edges (v,w) in E with v in X and w not in X (the
##       edges between explored and unexplored nodes), pick the one
##       that minimizes A[v] + Lvw, call it (v*,w*) (Dijkstras greedy criterion)
##    - add w* to X
##    - set A[w*] = A[v*] + Lv*w*
##    - set B[w*] = B[v*] U (v*,w*) (tack the new node onto the path)

## data to use, a directed graph as a list of lists, 
##  the first entry in each list is
##  the number of the vertex, each additional entry is a tuple(a,b),
##  where a is the name of an adjoining vertex and b is the distance
##  between the two
lines = [line.strip() for line in open('dijkstraData.txt')]
Glist = [[int(line[0])] + [tuple(map(int,s.split(','))) for s in line[1:]] for line in [line1.split() for line1 in lines]]
Gdict = {line[0]:line[1:] for line in Glist}

def short_path(G,S):
    """Computes Dijkstras shortest path distances, assumes 
    positive lengths and connected directed graph"""
    X = {S} # set of vertices processed so far
    A = {S:0} # computed shortest path (length)
    B = {S:[]} # computed shortest path (names of nodes along path)
    while X != set(G.keys()):
        # choose the next edge with the shortest path from current node
        minval = ['+inf']
        mindist = min(A[x] + min([b for a, b in G[x] if a not in X] + minval) for x in X)
        # mindist = min([A[x] + min([b for a,b in G[x] if a not in X]) for x in X if [b for a,b in G[x] if a not in X]!=[]])
        nextedge = {x:[(a,b) for a,b in G[x] if b==mindist-A[x] and a not in X] for x in X}
        nextedge = {i:j for i,j in nextedge.items() if j!=[]}
        leavingnode = nextedge.keys()[0]
        nextnode,dist = nextedge[leavingnode][0]
        X = X | {nextnode}
        A[nextnode] = mindist
        B[nextnode] = B[leavingnode]+[leavingnode]
    return A,B

dist,paths = short_path(Gdict,1)

## compute the shortest path between vertex 1 and the following 
##  vertices: 7,37,59,82,99,115,133,165,188,197.
tothese = [7,37,59,82,99,115,133,165,188,197]
output = [dist[i] for i in tothese]
