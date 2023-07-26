from dataclasses import dataclass
from typing import Optional

from shapely.geometry import Polygon

@dataclass
class Room:
    """
    A class representing a room in a building.

    Attributes:
    -----------
    uid : int
        The unique identifier of the room.
    name : Optional[str]
        The name of the room (optional).
    polygon : Polygon
        The polygon representing the shape of the room.
    """
    uid: int
    name: Optional[str]
    polygon : Polygon