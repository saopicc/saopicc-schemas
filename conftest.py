import warnings


# -W error (from command line) is applied by pytest AFTER ini filterwarnings, landing at
# position 0 in warnings.filters and overriding any ignore filter set earlier.
# pytest_collection fires after all filter setup, so inserting here ensures our filter
# stays at position 0 during test file imports.
def pytest_collection(session):
  warnings.filterwarnings(
    "ignore",
    message="Could not import the function to convert from MSv2 to MSv4",
    category=UserWarning,
  )
