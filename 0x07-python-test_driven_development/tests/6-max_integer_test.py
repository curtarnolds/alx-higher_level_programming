#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def testInteger(self):
        self.assertRaises(TypeError, max_integer, 3)

    def testFloat(self):
        self.assertRaises(TypeError, max_integer, 3.1)

    def testTuple(self):
        self.assertEqual(max_integer(
            (7, 4, 6, 12, 4, 6)), 12)

    def testSet(self):
        self.assertRaises(TypeError, max_integer, {2, 3, 4})

    def testEmptySet(self):
        self.assertEqual(max_integer(()), None)

    def testDict(self):
        self.assertRaises(KeyError, max_integer,
                          {'a': 1, 'b': 2})

    def testList(self):
        self.assertEqual(max_integer(
            [2, 3, 4]), 4)

    def testEmptyList(self):
        self.assertEqual(max_integer([]), None)

    def testString(self):
        self.assertEqual(max_integer('abcd'), 'd')

    def testEmptyString(self):
        self.assertEqual(max_integer(''), None)

    def testNone(self):
        self.assertRaises(TypeError, max_integer, None)

    def testNoArgs(self):
        self.assertEqual(max_integer(), None)

    def testListofStrings(self):
        self.assertEqual(max_integer(
            ['sdt', 'dlsd', 'z']), 'z')

    def testBoolean(self):
        self.assertRaises(TypeError, max_integer, True)
