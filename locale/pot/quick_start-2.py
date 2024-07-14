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
p = gv.GeoPlotter()
sargs = {"title": f"{sample.name} / {sample.units}"}
p.add_mesh(
    mesh,
    cmap="balance",
    scalar_bar_args=sargs
)
p.add_coastlines(color="white")
p.camera.zoom(1.2)
p.show()