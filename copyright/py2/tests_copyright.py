#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest, copyright, datetime
class TestCopyright(unittest.TestCase):
    def test_DEFAULT_NAME(self):
        self.assertEqual('{{AuthorName}}', copyright.Copyright.DEFAULT_NAME)

    def test_Generate(self):
        self.assertEqual(
            '© {} {}'.format(datetime.datetime.now().strftime('%Y'), copyright.Copyright.DEFAULT_NAME),
            copyright.Copyright.Generate())
    def test_Generate_name_pos(self):
        name = 'MyName'
        self.assertEqual(
            '© {} {}'.format(datetime.datetime.now().strftime('%Y'), name),
            copyright.Copyright.Generate(name))
    def test_Generate_name_kw(self):
        name = 'MyName'
        self.assertEqual(
            '© {} {}'.format(datetime.datetime.now().strftime('%Y'), name),
            copyright.Copyright.Generate(name=name))
    def test_Generate_name_TypeError(self):
        with self.assertRaises(TypeError):
            copyright.Copyright.Generate(0)

    def test_init(self):
        c = copyright.Copyright()
        self.assertEqual(copyright.Copyright, type(c))
        self.assertEqual('{{AuthorName}}', c.DefaultName)
        self.assertEqual(copyright.Copyright.DEFAULT_NAME, c.DefaultName)
    def test_init_default_name_pos(self):
        def_name = 'MyDefaultName'
        c = copyright.Copyright(def_name)
        self.assertEqual(def_name, c.DefaultName)
    def test_init_default_name_kw(self):
        def_name = 'MyDefaultName'
        c = copyright.Copyright(default_name=def_name)
        self.assertEqual(def_name, c.DefaultName)
    def test_init_default_name_TypeError(self):
        with self.assertRaises(TypeError):
            c = copyright.Copyright(0)

    def test_DefaultName_set(self):
        def_name = 'MyDefaultName'
        c = copyright.Copyright()
        c.DefaultName = def_name
        self.assertEqual(def_name, c.DefaultName)
    def test_DefaultName_set_TypeError(self):
        c = copyright.Copyright()
        with self.assertRaises(TypeError):
            c.DefaultName = 0

    def test_generate(self):
        self.assertEqual(
            '© {} {}'.format(datetime.datetime.now().strftime('%Y'), '{{AuthorName}}'),
            copyright.Copyright().generate())
    def test_generate_name_pos(self):
        name = 'test_name'
        self.assertEqual(
            '© {} {}'.format(datetime.datetime.now().strftime('%Y'), name),
            copyright.Copyright().generate(name))
    def test_generate_name_kw(self):
        name = 'test_name'
        self.assertEqual(
            '© {} {}'.format(datetime.datetime.now().strftime('%Y'), name),
            copyright.Copyright().generate(name=name))
    def test_generate_name_TypeError(self):
        with self.assertRaises(TypeError):
            copyright.Copyright().generate(0)


if __name__ == '__main__':
    unittest.main()

