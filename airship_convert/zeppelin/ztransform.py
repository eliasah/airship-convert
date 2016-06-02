#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, division, absolute_import

from toolz import compose, curry


@curry
def transform_paragraphs(notebook, transformations=None):
    """"""
    if transformations:
        f = compose(*reversed(transformations))
        notebook["paragraphs"] = [f(p) for p in notebook.get("paragraphs", [])]
    return notebook
