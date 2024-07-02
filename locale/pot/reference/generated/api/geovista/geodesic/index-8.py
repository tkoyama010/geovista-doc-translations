# Add a ``C8`` sixty-degree wide ``wireframe`` bounding-box wedge to the plotter. A
# texture mapped NASA Blue Marble base layer is also rendered.
#
import geovista
from geovista.geodesic import wedge
plotter = geovista.GeoPlotter()
_ = plotter.add_base_layer(texture=geovista.blue_marble(), opacity=0.5)
bbox = wedge(-30, 30, c=8)
_ = plotter.add_mesh(bbox.mesh, color="orange", style="wireframe")
plotter.view_yz()
plotter.show()
#
#
#
# ..
