"""krakenctl — deck utilities for the S.S. Kraken navigation console."""

__version__ = "1.1.0"
__all__ = ["bearing", "haversine", "Waypoint", "Sounding", "is_safe"]

from .charts import Waypoint, bearing, haversine
from .soundings import Sounding, is_safe
