from dataclasses import dataclass
from shapely.geometry import Polygon

@dataclass
class Room:
    uid: str
    name: Optional[str]
    polygon : Polygon