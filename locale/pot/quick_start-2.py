import geovista as gv
from geovista.pantry.data import oisst_avhrr_sst

# Load sample data.
sample = oisst_avhrr_sst()

# Create the mesh from the sample data.
mesh = gv.Transform.from_1d(
    sample.lons,
    sample.lats,
    data=sample.data
)

# Plot the mesh with coastlines.
plotter = gv.GeoPlotter()
sargs = {"title": f"{sample.name} / {sample.units}"}
plotter.add_mesh(
    mesh,
    cmap="balance",
    scalar_bar_args=sargs
)
plotter.add_coastlines(color="white")
plotter.camera.zoom(1.2)
plotter.show()