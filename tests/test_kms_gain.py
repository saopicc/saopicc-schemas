import numpy as np
import pytest
import xarray
from xradio.schema.check import check_dataset

from saopicc_schemas.antenna_gains import AntennaGains


@pytest.mark.filterwarnings(
  "ignore:Could not import the function to convert from MSv2 to MSv4:UserWarning",
)
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
  pols = np.array(["XX", "XY", "YX", "YY"])
  npols = len(pols)
  ntime = len(time)
  nfreq = len(freqs)
  nant = len(antenna)
  ndir = len(direction)
  gain_flags = np.random.choice([0, 1], (ndir, nant, ntime, nfreq)).astype(np.int8)
  gains_data = np.ones((ndir, nant, ntime, nfreq, npols)).astype(np.complex64)

  gains = xarray.Dataset(
    data_vars={
      "gain_flags": (["direction", "antenna", "gain_time", "gain_freq"], gain_flags),
      "gains": (
        ["direction", "antenna", "gain_time", "gain_freq", "polarization"],
        gains_data,
      ),
    },
    coords={
      "antenna": ("antenna", antenna),
      "polarization": ("polarization", pols),
      "direction": ("direction", direction),
      "gain_time": xarray.DataArray(
        time,
        dims=["gain_time"],
        attrs={
          "type": "time",
          "units": "s",
          "format": "unix",
          "scale": "utc",
        },
      ),
      "gain_t0": xarray.DataArray(
        t0,
        dims=["gain_time"],
        attrs={
          "type": "time",
          "units": "s",
          "format": "unix",
          "scale": "utc",
        },
      ),
      "gain_t1": xarray.DataArray(
        t1,
        dims=["gain_time"],
        attrs={
          "type": "time",
          "units": "s",
          "format": "unix",
          "scale": "utc",
        },
      ),
      "gain_freq": xarray.DataArray(
        freqs,
        dims=["gain_freq"],
        attrs={
          "type": "spectral_coord",
          "units": "Hz",
          "observer": "gcrs",
        },
      ),
      "gain_nu0": xarray.DataArray(
        nu0,
        dims=["gain_freq"],
        attrs={
          "type": "spectral_coord",
          "units": "Hz",
          "observer": "gcrs",
        },
      ),
      "gain_nu1": xarray.DataArray(
        nu1,
        dims=["gain_freq"],
        attrs={
          "type": "spectral_coord",
          "units": "Hz",
          "observer": "gcrs",
        },
      ),
    },
    attrs={
      "GAIN_AXES": ["direction", "antenna", "gain_time", "gain_freq", "correlation"],
      "GAIN_SPEC": [[16], [28], [3600], [64], [4]],
      "NAME": "G",
      "VERSION": "0.0.1",
      "TYPE": "complex",
      "comment": "NenuFAR prototype gain",
    },
  )

  issues = check_dataset(gains, AntennaGains)
  assert not issues
