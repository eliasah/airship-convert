#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, division, absolute_import
import unittest

from airship_convert.zeppelin.zlang import detect_language_, strip_interpreter_annotations


class ZeppelinTestCase(unittest.TestCase):
    def test_detect_language(self):
        self.assertEqual(detect_language_({"text": "%pyspark"}), "pyspark")
        self.assertEqual(detect_language_({"text": "%sql \n foo \nbar"}), "sql")
        self.assertIsNone(detect_language_({"text": "%scala python"}))
        self.assertEqual(detect_language_({"text": "%psql.sql \n foo \nbar"}), "psql.sql")

    def test_clean(self):
        self.assertEqual(strip_interpreter_annotations({"text": "%pyspark"}), {"text": ""})
        self.assertEqual(strip_interpreter_annotations({"text": "%sql \n foo \nbar"}), {"text": " foo \nbar"})
        self.assertEqual(strip_interpreter_annotations({"text": "%scala python"}), {"text": "%scala python"})


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
