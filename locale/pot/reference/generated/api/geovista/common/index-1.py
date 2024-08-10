from geovista.common import wrap
import numpy as np
wrap([179.0, 179.999, 180.0, 181.0])
# Expected:
## array([ 179., -180., -180., -179.])
#
wrap([179, 180, 181], period=90)
# Expected:
## array([ -91., -180., -179.])
#
wrap([179, 180, 181], base=0, period=90)
# Expected:
## array([89.,  0.,  1.])
#
# ..
