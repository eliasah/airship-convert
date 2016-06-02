#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, division, absolute_import

import pypandoc
from jinja2 import Environment, PackageLoader
from toolz import curry

from airship_convert import utils

_env = Environment(loader=PackageLoader("airship_convert", "templates"))


def render_doc_(notebook, output_format, output_file, template, extra_args):
    """"""
    pypandoc.convert(
        source=template.render(notebook), to="pdf" if output_format == "pdf" else output_format,
        format="markdown-blank_before_header",
        outputfile=output_file,
        extra_args=extra_args
    )


@curry
def render_doc(notebook, output_dir, output_format="html", extra_args=("-s", "--highlight-style=tango")):
    """"""
    template = _env.get_template("markdown/base.md")
    output_file = utils.path_for_notebook(notebook, output_dir=output_dir, output_format=output_format)
    render_doc_(notebook, output_format, output_file, template, extra_args)
