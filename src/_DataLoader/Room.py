from dataclasses import dataclass
from typing import Optional

from shapely.geometry import Polygon

@dataclass
class Room:
    uid: int
    name: Optional[str]
    polygon : Polygon