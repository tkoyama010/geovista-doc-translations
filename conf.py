# basedir is set by <lang>/conf.py
"""
Use "-D language=<LANG>" option to build a localized geovista-docs document.

For example::

    sphinx-build -D language=ja -b html . _build/html

This conf.py do:

- Specify `locale_dirs`.
- Overrides source directory as 'geovista/docs/src`.

"""

from pathlib import Path

basedir = Path(__file__).resolve().parent() / "geovista/docs/src"
exec((basedir / "conf.py").read_text(), globals())
autoapi_dirs = [basedir / "../../../geovista/src/geovista/"]
locale_dirs = [basedir / "../../../locale/"]
package_dir = basedir / "../../../geovista/src/geovista/"
sphinx_gallery_conf["examples_dirs"] = str(package_dir / "examples")  # noqa: F821


def setup(app) -> None:
    app.srcdir = basedir
    app.confdir = app.srcdir
