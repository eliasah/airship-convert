#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, division, absolute_import
import os


def path_for_notebook(notebook, output_dir, output_format):
    file_name = "{0}.{1}".format(notebook.get("id"), output_format)
    return os.path.join(output_dir, file_name)
