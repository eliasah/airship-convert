#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, division, absolute_import

from toolz import pipe, compose

from airship_convert import zeppelin, render


# Find path of the notebook and load
load_zeppelin_for_path = compose(zeppelin.load, zeppelin.notebook_for_path)


def tag_and_strip_annotations(lang):
    """"Add language info and clean code blocks"""
    return zeppelin.transform_paragraphs(transformations=(
        zeppelin.add_lang_tag(default_lang=lang),
        zeppelin.strip_interpreter_annotations
    ))


def process(paths, load_, transform_, filter_, sink_):
    """ Generic pipeline

    :param paths: input paths
    :param load_: data loading function
    :param transform_: transformation function
    :param filter_: filter functions
    :param sink_: output function
    :return:
    """
    for path in paths:
        pipe(path, load_, transform_, filter_, sink_)


def render_func(args):
    """Document rendering pipelines

    :param args: command line arguments
    """
    # Filter empty cells
    filter_ = zeppelin.filter_paragraphs(filters=(zeppelin.not_empty, ))

    # Render doc using pandoc
    sink_ = render.render_doc(output_dir=args.output_dir, output_format=args.format)

    process(args.paths, load_zeppelin_for_path, tag_and_strip_annotations(args.default_lang), filter_, sink_)


def extract_func(args):
    """Document rendering pipelines

    :param args: command line arguments
    """
    filter_ = zeppelin.filter_paragraphs(filters=(
        zeppelin.not_empty, zeppelin.for_language(languages=(args.language, ))
    ))

    sink_ = render.render_source(output_dir=args.output_dir, language=args.language)

    return process(args.paths, load_zeppelin_for_path, tag_and_strip_annotations(args.language), filter_, sink_)
