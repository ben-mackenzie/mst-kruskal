'''
Created on Apr 2, 2018

@author: benjaminmackenzie
'''
from DisJSets import DisJSet
from heapqriorityqueue import HeapPriorityQueue


def MST_Kruskal(g):
    '''Computes a minimum spanning tree of a graph using Kruskal's algorithm
    
    Returns a list of edges that comprise the MST
    MUST return a set of vertices with their associated edges
    PLUS the total weight of the MST
    
    The elements of the graph's edges are assumed to be weights
    '''
    tree = [] #list of edges in spanning tree
    pq = HeapPriorityQueue() #min heap - min weights pulled first (weights are keys)
    forest = DisJSet() #instance of Partition class (from DisJSets) - tracks forest clusters
    position = {} #set of nodes mapped to their Partition entries
    
    for v in g.vertices():
        position[v] = forest.make_group(v)
        
    for e in g.edges():
        pq.insert(e) #the edge's element is assumed to be its weight
        
    size = g.vertex_count()
    while len(tree) != size - 1 and not pq.is_empty(): #while there are still unprocesssed edges and tree isn't spanning
        edge = pq.deleteMin()
        u,v = edge.endpoints()
        a = forest.find(position[u])
        b = forest.find(position[v])
        if a != b:
            tree.append(edge)
            forest.unionSets(a,b)
    #also return node position keys (vertices)?        
    return tree
        
    
    