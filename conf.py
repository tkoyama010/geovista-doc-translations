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

basedir = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "geovista/docs/src"
)
exec(pathlib.Path(os.path.join(basedir, "conf.py")).read_text(), globals())
autoapi_dirs = [os.path.join(basedir, "../../../geovista/src/geovista/")]
locale_dirs = [os.path.join(basedir, "../../../locale/")]
package_dir = pathlib.Path(os.path.join(basedir, "../../../geovista/src/geovista/"))
sphinx_gallery_conf = {
    "default_thumb_file": str(docs_images_dir / "gallery-thumb.png"),
    "filename_pattern": "/.*",
    "ignore_pattern": "(__init__)|(clouds)|(fesom)|(synthetic)",
    "examples_dirs": str(package_dir / "examples"),
    "gallery_dirs": GALLERY_DIRS,
    "min_reported_time": 90,
    "matplotlib_animations": True,
    # see https://github.com/sphinx-gallery/sphinx-gallery/pull/195
    "plot_gallery": "'True'",
    "doc_module": "geovista",
    "image_scrapers": (scraper, "matplotlib"),
    "download_all_examples": False,
    "remove_config_comments": True,
    "within_subsection_order": "ExampleTitleSortKey",
    "reference_url": {
        "geovista": None,
    },
}


def setup(app):
    app.srcdir = basedir
    app.confdir = app.srcdir
