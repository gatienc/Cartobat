from dataclasses import dataclass
from shapely.geometry import Point
from .Room import Room

@dataclass
class Receiver:
    uid: int
    room : Room
    point : Point
