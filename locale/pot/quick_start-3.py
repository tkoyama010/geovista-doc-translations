import cartopy.crs as ccrs

import geovista as gv
from geovista.pantry.data import nemo_orca2

# Load sample data.
sample = nemo_orca2()

# Create the mesh from the sample data.
mesh = gv.Transform.from_2d(sample.lons, sample.lats, data=sample.data)

# Remove cells from the mesh with NaN values.
mesh = mesh.threshold()

# Plot the mesh on a Plate Carrée projection using a cartopy CRS.
plotter = gv.GeoPlotter(crs=ccrs.PlateCarree())
sargs = {"title": f"{sample.name} / {sample.units}"}
plotter.add_mesh(mesh, cmap="thermal", scalar_bar_args=sargs)
plotter.add_base_layer(texture=gv.natural_earth_1())
plotter.add_coastlines(color="white")
plotter.view_xy()
plotter.camera.zoom(1.4)
plotter.show()
