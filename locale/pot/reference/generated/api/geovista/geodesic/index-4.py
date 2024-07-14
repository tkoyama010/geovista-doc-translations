# Add the anti-meridian great circle to the plotter. A texture mapped Natural Earth
# base layer is also rendered.
#
import geovista
from geovista.geodesic import line
p = geovista.GeoPlotter()
_ = p.add_base_layer(texture=geovista.natural_earth_1())
meridian = line(-180, [90, 0, -90])
_ = p.add_mesh(meridian, color="orange", line_width=3)
p.view_yz(negative=True)
p.show()
#
#
#
# ..
