from dataclasses import dataclass, field
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
    cartesian_polygon : Polygon
        The polygon representing the shape of the room in cartesian_polygon coordinates.
    spherical_polygon : Polygon
        The polygon representing the shape of the room in cartesian coordinates.
        projection used -> mercator projection (EPSG:3857) https://en.wikipedia.org/wiki/Web_Mercator_projection
        """
    uid: int
    name: Optional[str]
    spherical_polygon : Polygon
    cartesian_polygon : Polygon 
    
