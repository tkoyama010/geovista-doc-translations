import pyvista

pyvista.set_jupyter_backend("static")
pyvista.global_theme.background = "white"
pyvista.global_theme.window_size = [400, 300]
pyvista.global_theme.axes.show = False
pyvista.global_theme.anti_aliasing = "fxaa"
