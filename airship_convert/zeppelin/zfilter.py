#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, division, absolute_import
from toolz import curry


def not_empty(cell):
    """Check if a given paragraph is empty"""
    return (cell.get("text") or cell.get('msg')) is not None


@curry
def for_language(cell, languages=set()):
    """Check if a given paragraph is in an expected language"""
    return cell.get("_lang") in languages


@curry
def filter_paragraphs(notebook, filters=None):
    if filters:
        filtered = [p for p in notebook.get("paragraphs", []) if all(f(p) for f in filters)]
        notebook["paragraphs"] = filtered
    return notebook
