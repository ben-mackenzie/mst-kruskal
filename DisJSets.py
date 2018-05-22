'''
Created on Apr 1, 2018

@author: benjaminmackenzie
'''

class DisJSet(object):
    '''
    ******************PUBLIC OPERATIONS*********************
    unionSets( root1, root2 ) --> Merge two sets
    find( x )              --> Return set containing x
    ******************ERRORS********************************
    No error checking is performed
    
    * Disjoint set class.
    * Use union by rank and path compression.
    * Elements in the set are numbered starting at 0.
    '''
    class Position:
        __slots__ = '_container', '_s', '_size', '_parent'
        
        def __init__(self, container, element):
            '''Creates a new position that is the leader of its own group'''
            self._container = container #partition instance
            self._element = element
            self._size = 0 #or 1?  python books' default is 1.
            self._parent = self #group leader
    
    def element(self):
        '''returns element/set stored at this position'''
        return self._element
    
    #PUBLIC METHODS:
    
    def make_group(self, element):
        '''Makes a new group containing set s and returns its Position'''
        return self.Position(self, element)
    
    def unionSets(self, root1, root2):
        '''Merges the groups containing p and q, if p and q are distinct'''
        a = self.find(root1)
        b = self.find(root2)
        if a is not b: 
            if a._size > b._size:
                b._parent = a
                a._size += b._size
            else:
                a._parent = b
                b._size += a._size
                
        
    def find(self, x):
        '''Finds the group containing p and returns root'''
        if x._parent != x:
            x._parent = self.find(x._parent)
        return x._parent
