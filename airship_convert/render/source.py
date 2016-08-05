#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, division, absolute_import
import codecs

from jinja2 import PackageLoader, Environment
from toolz import curry

from airship_convert import utils

_env = Environment(loader=PackageLoader("airship_convert", "templates"))

template_for_language = {
    "scala": ("scala/base.scala", "scala"),
    "python": ("python/base.pyi", "py")
}


def render_source_(notebook, output_file, template):
    with codecs.open(output_file, mode="w", encoding="utf-8") as fw:
        fw.write(template.render(notebook))


@curry
def render_source(notebook, output_dir, language):
    template_path, ext = template_for_language[language]

    template = _env.get_template(template_path)
    output_file = utils.path_for_notebook(notebook, output_dir, ext)

    render_source_(notebook, output_file, template)

