import numpy as np
import xarray

from saopicc_schemas.antenna_gains import AntennaGains


def test_gains_creation():
  # times are defined approximately based on nenufar dataset
  # 8s dt, 8h observation
  time = np.linspace(1.64e9, 1.64e9 + 3600 * 8, 3600)
  # assume a dt of 32s for the solve
  t0 = time - 16.0
  t1 = time + 16.0
  # observation from 856 MHz to 1.712 GHz, why not
  freqs = np.linspace(0.856e9, 2 * 0.856e9, 64)
  # assume 48 MHz bandwidth for the solve
  nu0 = freqs - 24 * 1e6
  nu1 = freqs + 24 * 1e6
  antenna = np.arange(28).astype(str)
  direction = np.arange(16)
  # nenufar, ska-low etc have linear dipoles
  corrs = np.array(["XX", "XY", "YX", "YY"])
  ntime = len(time)
  nfreq = len(freqs)
  nant = len(antenna)
  ndir = len(direction)
  gain_flags = np.random.choice([0, 1], (ndir, nant, ntime, nfreq))

  gains = AntennaGains.new(
    gain_flags=gain_flags,
    antenna=antenna,
    correlation=corrs,
    direction=direction,
    gain_time=xarray.DataArray(
      time,
      attrs={
        "type": "time",
        "units": "s",
        "format": "unix",
        "scale": "utc",
      },
    ),
    gain_t0=xarray.DataArray(
      t0,
      attrs={
        "type": "time",
        "units": "s",
        "format": "unix",
        "scale": "utc",
      },
    ),
    gain_t1=xarray.DataArray(
      t1,
      attrs={
        "type": "time",
        "units": "s",
        "format": "unix",
        "scale": "utc",
      },
    ),
    gain_freq=xarray.DataArray(
      freqs,
      attrs={
        "type": "spectral_coord",
        "units": "Hz",
        "observer": "gcrs",
      },
    ),
    gain_nu0=xarray.DataArray(
      nu0,
      attrs={
        "type": "spectral_coord",
        "units": "Hz",
        "observer": "gcrs",
      },
    ),
    gain_nu1=xarray.DataArray(
      nu1,
      attrs={
        "type": "spectral_coord",
        "units": "Hz",
        "observer": "gcrs",
      },
    ),
    GAIN_AXES=["direction", "antenna", "gain_time", "gain_freq", "correlation"],
    GAIN_SPEC=[[16], [28], [3600], [64], [4]],
    NAME="G",
    VERSION="0.0.1.1",
    TYPE="complex",
    comment="NenuFAR prototype gain",
  )
  print(gains)
