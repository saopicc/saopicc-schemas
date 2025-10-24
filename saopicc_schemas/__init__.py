from dataclasses import dataclass
from typing import List, Literal

import numpy as np
from xarray_dataclasses import AsDataset, Attr, Coord, Coordof, Data

#
Singleton = tuple[()]

# Dimensions
Antenna = Literal["antenna"]
Correlation = Literal["correlation"]
Direction = Literal["direction"]
GainTime = Literal["gain_time"]
GainFreq = Literal["gain_freq"]
TimeChunk = Literal["time_chunk"]
FreqChunk = Literal["freq_chunk"]


@dataclass
class GainTimeAxis:
  """Define the gain_time coordinate.
  This structure matches the MSv4 time coordinate axis
  by included astropy time scale attributes"""

  data: Data[GainTime, np.float64]
  type: Attr[str] = "time"
  units: Attr[str] = "s"
  format: Attr[str] = "unix"
  scale: Attr[str] = "utc"


@dataclass
class Gains(AsDataset):
  # Data Variables
  conv_iter: Data[tuple[TimeChunk, FreqChunk], np.int64]
  conv_perc: Data[tuple[TimeChunk, FreqChunk], np.float64]
  gain_flags: Data[tuple[GainTime, GainFreq, Antenna, Direction], np.int8]

  # Coordinates
  antenna: Coord[Antenna, str]
  correlation: Coord[Correlation, str]
  direction: Coord[Direction, int]
  time_chunk: Coord[TimeChunk, int]
  freq_chunk: Coord[FreqChunk, int]
  gain_time: Coordof[GainTimeAxis]
  gain_freq: Coord[GainFreq, np.float64]

  # Attributes
  GAIN_AXES: Attr[List[str]]
  GAIN_SPEC: Attr[List[List[int]]]
  NAME: Attr[str]
  TYPE: Attr[str]

  # Version of the schema
  VERSION: Attr[str] = "0.0.1"
