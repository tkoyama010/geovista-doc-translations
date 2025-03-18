# Add a ``C8`` sixty-degree wide ``wireframe`` bounding-box wedge to the plotter. A
# texture mapped NASA Blue Marble base layer is also rendered.
#
import geovista
from geovista.geodesic import wedge
p = geovista.GeoPlotter()
_ = p.add_base_layer(texture=geovista.blue_marble(), opacity=0.5)
bbox = wedge(-30, 30, c=8)
_ = p.add_mesh(bbox.mesh, color="orange", style="wireframe")
p.view_yz()
p.show()
#
# ..
