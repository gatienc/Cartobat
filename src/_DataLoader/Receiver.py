from dataclasses import dataclass,field
from shapely.geometry import Point
from .Room import Room

@dataclass
class Receiver:
    """
    A class representing a receiver in a room.This class has been tought to be the element of a set with mac module id as key.

    Attributes:
    -----------
    room : Room
        The room in which the receiver is located.
    point : Point
    spherical_point : Point
        The point in spherical coordinates (lat,long).
    cartesian_polygon : Polygon
        The polygon representing the shape of the room in cartesian coordinates.
        projection used -> Equirectangular projection https://en.wikipedia.org/wiki/Equirectangular_projection

        """
    room : Room
    spherical_point : Point
    cartesian_point : Point
