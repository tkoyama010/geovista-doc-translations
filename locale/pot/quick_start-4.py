import geovista as gv
from geovista.pantry.data import ww3_global_tri

# Load the sample data.
sample = ww3_global_tri()

# Create the mesh from the sample data.
mesh = gv.Transform.from_unstructured(
    sample.lons,
    sample.lats,
    connectivity=sample.connectivity,
    data=sample.data,
)

# Plot the mesh.
p = gv.GeoPlotter()
sargs = {"title": f"{sample.name} / {sample.units}"}
p.add_mesh(
    mesh,
    cmap="balance",
    scalar_bar_args=sargs
)
p.add_coastlines(color="white")
p.add_base_layer(texture=gv.natural_earth_hypsometric())
p.view_xy(negative=True)
p.camera.zoom(1.2)
p.show()