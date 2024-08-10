from geovista.geodesic import npoints
import numpy as np
points = npoints(start_lon=-10, start_lat=20, end_lon=10, end_lat=30, npts=5)
np.array(points, dtype=np.float16)
# Expected:
## array([[-6.887, -3.69 , -0.41 ,  2.963,  6.43 ],
##        [21.84 , 23.62 , 25.34 , 26.98 , 28.53 ]], dtype=float16)
#
# ..
