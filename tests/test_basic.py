import numpy as np
import numpy.testing as npt
import xarray

from saopicc_schemas import Gains


def test_gains_creation():
  time = np.linspace(1.0, 2.0, 10)
  freqs = np.linspace(0.856e9, 2 * 0.856e9, 16)
  antenna = np.arange(28).astype(str)
  direction = np.arange(1)
  corrs = np.array(["RR", "RL", "LR", "LL"])
  ntime = len(time)
  nfreq = len(freqs)
  nant = len(antenna)
  ndir = len(direction)
  conv_iter = np.full((4, 4), 4)
  conv_perc = np.full((4, 4), 5)
  gain_flags = np.random.choice([0, 1], (ntime, nfreq, nant, ndir))

  gains = Gains.new(
    conv_iter=conv_iter,
    conv_perc=conv_perc,
    time_chunk=np.arange(conv_iter.shape[0]),
    freq_chunk=np.arange(conv_iter.shape[1]),
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
        "integration_time": {
          "attrs": {"type": "quantity", "units": "s"},
          "data": 8.0,
        },
      },
    ),
    gain_freq=freqs,
    GAIN_AXES=["gain_time", "gain_freq", "antenna", "direction", "correlation"],
    GAIN_SPEC=[[115], [64], [28], [1], [4]],
    NAME="G",
    VERSION="0.0.1",
    TYPE="complex",
  )

  # Test some data variables
  npt.assert_array_equal(gains.data_vars["gain_flags"], gain_flags)
  npt.assert_array_equal(gains.data_vars["conv_iter"], conv_iter)
  npt.assert_array_equal(gains.data_vars["conv_perc"], conv_perc)

  # Test some coordinates
  npt.assert_array_equal(gains.coords["antenna"], antenna)
  npt.assert_array_equal(gains.coords["direction"], direction)

  # Test some attributes
  assert "GAIN_AXES" in gains.attrs
  assert "GAIN_SPEC" in gains.attrs
  assert gains.attrs["NAME"] == "G"
  assert "VERSION" in gains.attrs

  print(gains)
