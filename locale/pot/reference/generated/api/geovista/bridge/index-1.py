from geovista import GeoPlotter, Transform
from geovista.pantry import fetch_raster
from geovista.pantry.textures import natural_earth_1
#
# Render the GeoTIFF ``RGB`` image as a geolocated mesh.
#
# First, :func:`rasterio.features.sieve` the GeoTIFF image to remove several
# unwanted masked regions within the interior of the image, due to a lack of
# dynamic range in the ``uint8`` image data. Then, extract the mesh to remove
# cells with no masked points.
#
fname = fetch_raster("bahamas_rgb.tif")
mesh = Transform.from_tiff(fname, rgb=True, sieve=True, extract=True)
#
# Now render the result:
#
p = GeoPlotter()
_ = p.add_mesh(mesh, rgb=True)
p.view_poi()
_ = p.add_base_layer(texture=natural_earth_1(), zlevel=0)
_ = p.add_coastlines(color="white")
p.show()
#
# ..
