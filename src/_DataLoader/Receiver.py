from dataclasses import dataclass
from shapely.geometry import Point
from .Room import Room

@dataclass
class Receiver:
    uid: str
    room : Room
    point : Point
