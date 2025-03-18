# Add the geodesic bounding-box manifold for the Arctic cubed-sphere
# panel along with its edges. A texture mapped Natural Earth base layer
# is also rendered.
#
import geovista
from geovista.geodesic import panel
p = geovista.GeoPlotter()
_ = p.add_base_layer(texture=geovista.natural_earth_1(), opacity=0.5)
bbox = panel("arctic")
_ = p.add_mesh(bbox.mesh, color="orange")
_ = p.add_mesh(bbox.outline, color="yellow", line_width=3)
p.view_vector(vector=(1, 1, 0))
p.camera.zoom(1.5)
p.show()
#
# ..
