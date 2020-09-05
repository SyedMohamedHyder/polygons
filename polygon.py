# All imports go here
import math
import numbers

# This is a simple Polygon class which creates a polygon 
# based on the number of edges and the circumradius
class Polygon:
    
    # Initialisation starts here
    def __init__(self, edges, radius):
        self._edges = None
        self._radius = None
        
        self.edges = edges
        self.radius = radius
        
    # Getters and setters start here
    # edges getter and setter
    @property
    def edges(self):
        return self._edges
    
    @edges.setter
    def edges(self, value):
        if not isinstance(value, int):
            raise TypeError('Number of edges of a polygon should only be integers')
        elif value < 3 :
            raise ValueError('There must be atleast 3 edges in a polygon')
        else:
            self._edges = value
    
    # radius getter and setter        
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if not isinstance(value, numbers.Real):
            raise TypeError('Circumradius of a polygon can only be a real number')
        if value <= 0 :
            raise ValueError('Circumradius of a polygon can only be positive')
        else:
            self._radius = value
    
    # This is a property and hence not callable
    # Returns the number of vertices. Same as self.edges
    # Value cannot be assigned to vertices since we didn't implement setter
    @property
    def vertices(self):
        return self.edges
    
    # Calculates the interior angle of the polygon
    def interior_angle(self):
        return (self.edges - 2) * (180/self.edges)
    
    # Calculates the edge length
    # All sides have the same length
    def edge_length(self):
        return (2 * self.radius) * (math.sin(math.pi/self.edges))
    
    # Calculates area of the polygon
    def area(self):
        a = self.radius * math.cos(math.pi / self.edges)
        s = self.edge_length()
        return (self.edges * s * a) / 2
    
    # Calculates perimeter of the polygon
    def perimeter(self):
        s = self.edge_length()
        return self.edges * s
    
    # Equality implementation
    # Can compare only Polygons
    # Polygons are said to be equal if they have same number of vertices and same circumradius
    def __eq__(self, other):
        if isinstance(other, Polygon):
            return self.edges == other.edges and self.radius == other.radius
        else:
            raise TypeError('Incompatble type for comparision. Can only compare with another Polygon')
            
    # '>' operator implementation
    # Polygons are compared based on the number of vertices
    def __gt__(self, other):
        if isinstance(other, Polygon):
            return self.edges > other.edges
        else:
            raise TypeError('Incompatble type for comparision. Can only compare with another Polygon')
            
    # Representation of Polygon object
    def __repr__(self):
        return f'{self.__class__.__name__}(edges={self.edges}, radius={self.radius})'