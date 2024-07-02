# First, create an RGB mesh of the Bahamas from a GeoTIFF.
#
import geovista
from geovista.pantry import fetch_raster
fname = fetch_raster("bahamas_rgb.tif")
bahamas = geovista.Transform.from_tiff(
    fname, rgb=True, sieve=True, extract=True
)
#
# Now add the ``bahamas`` mesh to a ``plotter`` **before** adding a texture mapped
# base layer. Note that, the camera is centered over the ``bahamas`` mesh, which
# is the primary focus of the scene.
#
plotter = geovista.GeoPlotter()
_ = plotter.add_mesh(bahamas, rgb=True)
plotter.view_poi()
_ = plotter.add_base_layer(texture=geovista.natural_earth_1())
plotter.show()
#
# In comparison, add a texture mapped base layer to a ``plotter`` **before** the
# ``bahamas`` mesh. The camera is still centered over the ``bahamas`` in the
# rendered scene, however the base layer is now fully visible.
#
plotter = geovista.GeoPlotter()
_ = plotter.add_base_layer(texture=geovista.natural_earth_1())
_ = plotter.add_mesh(bahamas, rgb=True)
plotter.view_poi()
plotter.show()
#
#
#
# ..
