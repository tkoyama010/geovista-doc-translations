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
p = geovista.GeoPlotter()
_ = p.add_mesh(bahamas, rgb=True)
p.view_poi()
_ = p.add_base_layer(texture=geovista.natural_earth_1())
p.show()
#
# In comparison, add a texture mapped base layer to a ``plotter`` **before** the
# ``bahamas`` mesh. The camera is still centered over the ``bahamas`` in the
# rendered scene, however the base layer is now fully visible.
#
p = geovista.GeoPlotter()
_ = p.add_base_layer(texture=geovista.natural_earth_1())
_ = p.add_mesh(bahamas, rgb=True)
p.view_poi()
p.show()
#
#
#
# ..
