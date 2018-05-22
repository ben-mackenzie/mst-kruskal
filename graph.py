'''
Created on Apr 2, 2018

@author: benjaminmackenzie
'''

class Graph:
    '''Representation of an undirected graph using an adjacency map'''
    
    class Vertex:
        '''creates vertex objects for graph'''
        __slots__ = '_element'
        
        def __init__(self, x):
            '''graph's insert_vertex(x) method constructs vertices'''
            self._element = x
            
        def element(self):
            '''Return element associated with vertex'''
            return self._element
        
        def __hash__(self): #allows vertex to be a map/set key
            return hash(id(self))
        
    class Edge:
        '''creates edge objects for the graph class'''
        __slots__ = '_origin', '_destination', '_element'
        
        def __init__(self, u, v, x):
            '''Called by the graph's insert_edge(u, v, x) method'''
            self._origin = u
            self._destination = v
            self._element = x
            
        def endpoints(self):
            '''Returns (u,v) tuple for vertices u and v'''
            return (self._origin, self._destination)
        
        def opposite(self, v):
            '''Returns the vertex that is opposite v on this edge'''
            return self._destination if v is self._origin else self._origin
        
        def element(self):
            '''Returns element associated with edge'''
            return self._element
        
        def __hash__(self): #allows edge to be a map/set key
            return hash( (self._origin, self._destination) )
            
    def __init__(self, directed=False):
        '''creates an empty graph, undirected'''
        self._outgoing = {}
    
    def vertex_count(self):
        return len(self._outgoing)
   
    def vertices(self):
        return self._outgoing.keys()
   
    def edges(self):
        result = set()
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values()) #add edges to resulting set
        return result
            
    def insert_vertex(self, x=None):
        '''Inserts and returns a new Vertex with element x.'''
        v = self.Vertex(x)
        self._outgoing[v] = {}
        return v
    
    def insert_edge(self, u, v, x=None):
        '''Inserts and returns a new Edge from u to v with aux element x.'''
        e = self.Edge(u, v, x)
        self._outgoing[u][v] = e
        