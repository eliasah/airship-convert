#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, division, absolute_import

import json
import os


def load(path):
    """Loads a single Zeppelin notebook. For now just a wrapper around json.load"""
    with open(path) as fr:
        try:
            return json.load(fr)
        except json.JSONDecodeError:
            return {}


def notebook_for_path(path):
    """"""
    return os.path.join(path, "note.json")
