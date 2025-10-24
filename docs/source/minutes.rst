:tocdepth: 1

Meeting Minutes
===============

21-10-2025
----------

**Topic:** Formats to be used within ECLAT/SARAO sofware

**Attendees:**

- Etienne Bonnassieux (ECLAT, Observatoire de Paris)
- Cyril Tasse (ECLAT, Observatoire de Paris)
- Jon Kenyon (SARAO)
- Landman Bester (SARAO)
- Simon Perkins (SARAO)
- Oleg Smirnov (SARAO)

**Minutes:**

* NRAO and SKAO are going to provide an exhaustive definition of visibility data format in xarray
* They are also working on doing the same for `image formats <https://github.com/casangi/xradio/issues/497_>`_.
* Their schema defines MSv4 dataset and datastructures, and will be used to enforce conformity with the schema
* Basic idea is to have something similar to define the schema for the gains.
* this is to ensure cross-compatibility between quartical/kms, ddf/pfb
* versioning of the datastructure can allow for efficient development work
* long discussion : do we store phase screens as a function inside the dataformat, or just the coefficient
* all agree that it's a good idea to define gain solution files as xarrays
