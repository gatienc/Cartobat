from dataclasses import dataclass
from shapely.geometry import Point
from .Room import Room

@dataclass
class Receiver:
    room : Room
    point : Point
