from dataclasses import dataclass
from typing import List, Literal

import numpy as np
from xarray_dataclasses import AsDataset, Attr, Coord, Data

# Define our dimensions here
Direction = Literal["direction"]
Antenna = Literal["antenna"]
GainTime = Literal["gain_time"]
GainFreq = Literal["gain_freq"]
Correlation = Literal["correlation"]
# Define properties for gain combinations
Gain_T0 = Literal["gain_T0"]
Gain_T1 = Literal["gain_T1"]
Gain_nu0 = Literal["gain_nu0"]
Gain_nu1 = Literal["gain_nu1"]
# Add a comments functionality
Comments = Literal["comments"]


@dataclass
class AntennaGains(AsDataset):
  # Data Variables
  gain_flags: Data[tuple[Direction, Antenna, GainTime, GainFreq], np.int8]
  # Coordinates
  antenna: Coord[Antenna, str]
  correlation: Coord[Correlation, str]
  direction: Coord[Direction, int]
  gain_time: Coord[GainTime, np.float64]
  gain_freq: Coord[GainFreq, np.float64]
  gain_t0: Coord[Gain_T0, np.float64]
  gain_t1: Coord[Gain_T1, np.float64]
  gain_nu0: Coord[Gain_nu0, np.float64]
  gain_nu1: Coord[Gain_nu0, np.float64]
  # Attributes
  GAIN_AXES: Attr[List[str]]
  GAIN_SPEC: Attr[List[List[int]]]
  NAME: Attr[str]
  TYPE: Attr[str]
  # comments field, empty by default
  comment: Attr[str] = ""
  # Version of the schema
  VERSION: Attr[str] = "0.0.1"
