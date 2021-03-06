#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, division, absolute_import

import argparse

from airship_convert.pipelines import render_func, extract_func
from airship_convert.release import __author__, __version__


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    render_ = subparsers.add_parser("render")
    render_.add_argument("paths", nargs="+",
                         help="At least one path to the notebook directory (one that contains note.json file).")
    render_.add_argument("--output-dir", default=".",
                         help="Directory to put output files.")
    render_.add_argument("--format", default="html",
                         help="Pandoc supported output format.")
    render_.add_argument("--default-lang", default="scala",
                         help="Language to be used if there is no interpreter annotation.")
    render_.set_defaults(func=render_func)

    extract_ = subparsers.add_parser("extract")
    extract_.add_argument("paths", nargs="+",
                          help="At least one path to the notebook directory (one that contains note.json file).")
    extract_.add_argument("--output-dir", default=".",
                          help="Directory to put output files.")
    extract_.add_argument("--language", default="scala", choices=["scala", "python"],
                          help="Which language should be extracted.")
    extract_.set_defaults(func=extract_func)

    args = parser.parse_args()
    args.func(args)
