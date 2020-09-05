# All imports go here
from functools import reduce
from polygon import Polygon

# Polygons class recieves the number of edges of largest polygon it will contain
# It contains all the polygons starting from 3 edges to the number of edges passed
class Polygons:
    
    # Initialisation goes here
    def __init__(self, number, common_radius):
        if not isinstance(number, int):
            raise TypeError('Unsupported type for the number of edges for the largest polygon')
        elif number < 3:
            raise ValueError('Largest Polygon should have atleast 3 edges')
        self._radius = common_radius
        self._polygons = [Polygon(edge, self._radius) for edge in range(3,number+1)]
    
    # Calculates the most efficient polygon based on the area to perimeter ratio
    def efficient_polygon(self):
        return reduce(Polygons._efficient, self._polygons)
        
    # Static methods can only be called by the class
    # This is a helper function for efficient_polygon method
    @staticmethod    
    def _efficient(polygon1, polygon2):
        polygon1_efficiency = polygon1.area() / polygon1.perimeter()
        polygon2_efficiency = polygon2.area() / polygon2.perimeter()
        return polygon1 if polygon1_efficiency > polygon2_efficiency else polygon2
    
    # Sequencing the class begins from here
    # Returns the total number of polygons present
    def __len__(self):
        return len(self._polygons)
    
    # Makes the Polygons class iterable and indexable thus making it a sequence
    def __getitem__(self, index):
        return self._polygons[index]
    
    # Representation for the polygons class        
    def __repr__(self):
        all_polygons = ', '.join(str(polygon) for polygon in self._polygons)
        return f'{self.__class__.__name__}({all_polygons})'