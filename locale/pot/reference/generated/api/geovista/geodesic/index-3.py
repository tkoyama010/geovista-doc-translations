# Add a ``C32`` bounding-box around the Gulf of Guinea.
# The geodesic bounding-box is generated by defining 4 longitude-latitude
# corners. Natural Earth coastlines are also rendered along
# with a texture mapped Natural Earth base layer.
#
import geovista
from geovista.geodesic import BBox
plotter = geovista.GeoPlotter()
_ = plotter.add_base_layer(
    texture=geovista.natural_earth_hypsometric(), style="wireframe"
)
bbox = BBox(lons=[-15, 20, 25, -15], lats=[-25, -20, 15, 10], c=32)
_ = plotter.add_mesh(bbox.mesh, color="white")
plotter.camera.zoom(1.5)
plotter.show()
#
#
#
# ..