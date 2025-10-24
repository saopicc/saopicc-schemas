from dataclasses import dataclass, asdict
from typing import Any, Dict, List, Literal
import numpy as np
from xarray_dataclasses import AsDataset
from xarray_dataclasses import Attr, Coord, Data, Name, Dataof, Coordof

# Singleton = tuple[()]

# Define our dimensions here
Direction   = Literal["direction"]
Antenna     = Literal["antenna"]
GainTime    = Literal["gain_time"]
GainFreq    = Literal["gain_freq"]
Correlation = Literal["correlation"]
# Define properties for gain combinations
Gain_T0     = Literal["gain_T0"]
Gain_T1     = Literal["gain_T1"]
Gain_nu0    = Literal["gain_nu0"]
gain_nu1    = Literal["gain_nu1"]
# TBD what we do with below
#TimeChunk   = Literal["time_chunk"]
#FreqChunk   = Literal["freq_chunk"]


@dataclass
class AntennaGains(AsDataset):
  # Data Variables
  conv_iter: Data[tuple[TimeChunk, FreqChunk], np.int64]
  conv_perc: Data[tuple[TimeChunk, FreqChunk], np.float64]
  gain_flags: Data[tuple[GainTime, GainFreq, Antenna, Direction], np.int8]

  # Coordinates
  antenna: Coord[Antenna, str]
  correlation: Coord[Correlation, str]
  direction: Coord[Direction, int]
#  time_chunk: Coord[TimeChunk, int]
#  freq_chunk: Coord[FreqChunk, int]
  gain_time: Coord[GainTime, np.float64]
  gain_freq: Coord[GainFreq, np.float64]

  # Attributes
  GAIN_AXES: Attr[List[str]]
  GAIN_SPEC: Attr[List[List[int]]]
  NAME: Attr[str]
  TYPE: Attr[str]

  # Version of the schema
  VERSION: Attr[str] = "0.0.1.1"
