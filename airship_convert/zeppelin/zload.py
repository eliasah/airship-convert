#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, division, absolute_import

import json
import os
import codecs


def load(path):
    """Loads a single Zeppelin notebook. For now just a wrapper around json.load"""
    with codecs.open(path, mode="r", encoding="UTF-8") as fr:
        try:
            return json.load(fr)
        except json.JSONDecodeError:
            return {}


def notebook_for_path(path):
    """"""
    return os.path.join(path, "note.json")
