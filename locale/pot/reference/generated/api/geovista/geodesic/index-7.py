# Add a ``wireframe`` bounding-box to the plotter for the ``americas`` panel of a
# cubed-sphere. The geodesic bounding-box is generated from the 4 corners of the
# cubed-sphere panel located over Americas.  A texture mapped Natural Earth base
# layer is also rendered.
#
import geovista
from geovista.geodesic import panel
plotter = geovista.GeoPlotter()
_ = plotter.add_base_layer(
    texture=geovista.natural_earth_hypsometric(), opacity=0.5
)
bbox = panel("americas", c=8)
_ = plotter.add_mesh(bbox.mesh, color="orange", style="wireframe")
plotter.view_xz()
plotter.show()
#
#
#
# ..
