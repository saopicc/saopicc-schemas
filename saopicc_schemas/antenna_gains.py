from typing import List, Literal

import numpy as np
from xradio.measurement_set.schema import Polarization, PolarizationArray
from xradio.schema.bases import (
  xarray_dataarray_schema,
  xarray_dataset_schema,
)
from xradio.schema.typing import Attr, Coord, Coordof, Data

# Define our dimensions here
Direction = Literal["direction"]
Antenna = Literal["antenna"]
GainTime = Literal["gain_time"]
GainFreq = Literal["gain_freq"]
# Define properties for gain combinations
Gain_T0 = Literal["gain_T0"]
Gain_T1 = Literal["gain_T1"]
Gain_nu0 = Literal["gain_nu0"]
Gain_nu1 = Literal["gain_nu1"]
# Add a comments functionality
Comments = Literal["comments"]

# Define time axes


@xarray_dataarray_schema
class GainTimeAxis:
  """Define the gain_time coordinate.
  This structure matches the MSv4 time coordinate axis
  by included astropy time scale attributes"""

  data: Data[GainTime, np.float64]
  type: Attr[str] = "time"
  units: Attr[str] = "s"
  format: Attr[str] = "unix"
  scale: Attr[str] = "utc"


@xarray_dataarray_schema
class GainT0Axis:
  """Define the gain_time coordinate.
  This structure matches the MSv4 time coordinate axis
  by included astropy time scale attributes"""

  data: Data[GainTime, np.float64]
  type: Attr[str] = "time"
  units: Attr[str] = "s"
  format: Attr[str] = "unix"
  scale: Attr[str] = "utc"


@xarray_dataarray_schema
class GainT1Axis:
  """Define the gain_time coordinate.
  This structure matches the MSv4 time coordinate axis
  by included astropy time scale attributes"""

  data: Data[GainTime, np.float64]
  type: Attr[str] = "time"
  units: Attr[str] = "s"
  format: Attr[str] = "unix"
  scale: Attr[str] = "utc"


# Define frequency axes


@xarray_dataarray_schema
class GainFreqAxis:
  """Define the gain_freq coordinate.
  This structure matches the MSv4 frequency coordinate axis
  by included astropy frequency scale attributes"""

  data: Data[GainFreq, np.float64]
  type: Attr[str] = "spectral_coord"
  units: Attr[str] = "Hz"
  observer: Attr[str] = "gcrs"


@xarray_dataarray_schema
class GainNu0Axis:
  """Define the gain_freq coordinate.
  This structure matches the MSv4 frequency coordinate axis
  by included astropy frequency scale attributes"""

  data: Data[GainFreq, np.float64]
  type: Attr[str] = "spectral_coord"
  units: Attr[str] = "Hz"
  observer: Attr[str] = "gcrs"


@xarray_dataarray_schema
class GainNu1Axis:
  """Define the gain_freq coordinate.
  This structure matches the MSv4 frequency coordinate axis
  by included astropy frequency scale attributes"""

  data: Data[GainFreq, np.float64]
  type: Attr[str] = "spectral_coord"
  units: Attr[str] = "Hz"
  observer: Attr[str] = "gcrs"


@xarray_dataset_schema
class AntennaGains:
  # Data Variables
  gain_flags: Data[tuple[Direction, Antenna, GainTime, GainFreq], np.int8]
  gains: Data[tuple[Direction, Antenna, GainTime, GainFreq, Polarization], np.complex64]
  # Coordinates
  antenna: Coord[Antenna, str]
  polarization: Coordof[PolarizationArray]
  direction: Coord[Direction, int]
  gain_time: Coordof[GainTimeAxis]
  gain_t0: Coordof[GainT0Axis]
  gain_t1: Coordof[GainT1Axis]
  gain_freq: Coordof[GainFreqAxis]
  gain_nu0: Coordof[GainNu0Axis]
  gain_nu1: Coordof[GainNu1Axis]
  # Attributes
  GAIN_AXES: Attr[List[str]]
  NAME: Attr[str]
  TYPE: Attr[str]
  # comments field, empty by default
  comment: Attr[str] = ""
  # Version of the schema
  VERSION: Attr[str] = "0.0.1"
