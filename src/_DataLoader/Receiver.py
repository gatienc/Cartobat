from dataclasses import dataclass
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
        The point in the room where the receiver is located.
    """
    room : Room
    point : Point
