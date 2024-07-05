from geovista.geodesic import npoints_by_idx
import numpy as np

points = npoints_by_idx(
    lons=[-10, 0, 10], lats=[20, 25, 30], start_idx=0, end_idx=1, npts=5
)
np.array(points, dtype=np.float16)
# Expected:
## array([[-8.38 , -6.746, -5.09 , -3.414, -1.718],
##        [20.88 , 21.73 , 22.58 , 23.4  , 24.22 ]], dtype=float16)
#
#
#
# ..
