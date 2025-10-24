import numpy as np
import xarray

from saopicc_schemas import AntennaGains


def test_gains_creation():
  # times are defined approximately based on nenufar dataset
  # 8s dt, 8h observation
  time = np.linspace(1.64e9, 1.64e9 + 3600 * 8, 3600)
  freqs = np.linspace(0.856e9, 2 * 0.856e9, 64)
  antenna = np.arange(28).astype(str)
  direction = np.arange(16)
  corrs = np.array(["RR", "RL", "LR", "LL"])
  ntime = len(time)
  nfreq = len(freqs)
  nant = len(antenna)
  ndir = len(direction)
  #  conv_iter = np.full((4, 4), 4)
  #  conv_perc = np.full((4, 4), 5)
  gain_flags = np.random.choice([0, 1], (ndir, nant, ntime, nfreq))

  gains = AntennaGains.new(
    #    conv_iter=conv_iter,
    #    conv_perc=conv_perc,
    #    time_chunk=np.arange(conv_iter.shape[0]),
    #    freq_chunk=np.arange(conv_iter.shape[1]),
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
    GAIN_AXES=["direction", "antenna", "gain_time", "gain_freq", "correlation"],
    GAIN_SPEC=[[115], [64], [28], [1], [4]],
    NAME="G",
    VERSION="0.0.1",
    TYPE="complex",
  )
  print(gains)
