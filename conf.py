# basedir is set by <lang>/conf.py
"""
Use "-D language=<LANG>" option to build a localized geovista-docs document.
For example::

    sphinx-build -D language=ja -b html . _build/html

This conf.py do:

- Specify `locale_dirs`.
- Overrides source directory as 'geovista/docs/src`.

"""

import os
import pathlib

basedir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "geovista/docs/src")
exec(pathlib.Path(os.path.join(basedir, "conf.py")).read_text(), globals())
autoapi_dirs = [os.path.join(basedir, "../../../geovista/src/geovista/")]
locale_dirs = [os.path.join(basedir, "../../../locale/")]
package_dir = pathlib.Path(os.path.join(basedir, "../../../geovista/src/geovista/"))
sphinx_gallery_conf["examples_dirs"] = str(package_dir / "examples")  # noqa F821


def setup(app):
    app.srcdir = basedir
    app.confdir = app.srcdir
