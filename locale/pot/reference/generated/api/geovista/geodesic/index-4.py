# Add the anti-meridian great circle to the plotter. A texture mapped Natural Earth
# base layer is also rendered.
#
import geovista
from geovista.geodesic import line
plotter = geovista.GeoPlotter()
_ = plotter.add_base_layer(texture=geovista.natural_earth_1())
meridian = line(-180, [90, 0, -90])
_ = plotter.add_mesh(meridian, color="orange", line_width=3)
plotter.view_yz(negative=True)
plotter.show()
#
#
#
# ..
