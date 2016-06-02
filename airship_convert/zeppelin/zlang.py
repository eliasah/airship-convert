#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, division, absolute_import
import re

from toolz import curry


language_pattern = re.compile("^%([\.a-z]*)\s*$")

languages = {
    "cassandra": "sql",
    "elasticsearch": "elasticsearch",
    "flink": "scala",
    "ignite": "scala",
    "ignite.ignitesql": "sql",
    "md": "md",
    "pyspark": "python",
    "r": "R",
    "psql.sql": "sql",
    "scala": "scala",
    "scalding": "scala",
    "sh": "shell",
    "sql": "sql",
}


def detect_language_(cell):
    """"""
    m = language_pattern.match(cell.get("text", "").split("\n", 1)[0])
    return m.group(1) if m else None


@curry
def add_lang_tag(cell, default_lang):
    cell["_lang"] = languages.get(detect_language_(cell), default_lang)
    return cell


def strip_interpreter_annotations(cell):
    """"""
    lines = cell.get("text", "").split("\n", 1)
    if language_pattern.match(lines[0]):
        cell["text"] = lines[1] if len(lines) > 1 else ""
    return cell
