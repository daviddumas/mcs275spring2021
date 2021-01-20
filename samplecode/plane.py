"""Geometric objects in the plane"""
# MCS 275 Spring 2021 David Dumas
# Lecture 4

class Point:
    """A point in the plane"""
    def __init__(self,x,y):
        """Create a new point with coordinates x,y"""
        self.x = x
        self.y = y

    def __str__(self):
        """Human-readable string representation of a Point"""
        return "Point({},{})".format(self.x,self.y)

    def __repr__(self):
        """String representation of a Point"""
        return str(self)

class Vector:
    """A 2-dimensional vector"""
    def __init__(self,x=0.0,y=0.0):
        """Create a new vector with components x,y"""
        self.x = x
        self.y = y

    def __str__(self):
        """Human-readable string representation of a Vector"""
        return "Vector({},{})".format(self.x,self.y)

    def __repr__(self):
        """String representation of a Vector"""
        return str(self)

    def __add__(self,other):
        """Vector-vector or Vector-Point addition"""
        if isinstance(other,Vector):
            return Vector(self.x+other.x,self.y+other.y)
        elif isinstance(other,Point):
            return Point(self.x+other.x,self.y+other.y)
        else:
            return NotImplemented

    def __radd__(self,other):
        """Point-Vector addition"""
        if isinstance(other,Point):
            return Point(self.x+other.x,self.y+other.y)
        else:
            return NotImplemented

    def __sub__(self,other):
        """Vector subtraction"""
        if isinstance(other,Vector):
            return Vector(self.x-other.x,self.y-other.y)
        else:
            return NotImplemented