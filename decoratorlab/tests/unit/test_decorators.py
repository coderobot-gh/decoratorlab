# -*- coding: utf-8 -*-
"""
Test decorators
"""

import unittest
from decoratorlab import decorators


class Test(unittest.TestCase):

    @unittest.skip
    def test_import(self):
        with self.assertRaises("ImportError"):
            import decoratorlab

    def test_identity_decorator(self):
        @decorators.identity_decorator
        def decorated_function(_int):
            return _int
        result = decorated_function(3)
        self.assertEqual(result, 3)

    def test_double_decorator(self):
        @decorators.double_decorator
        def decorated_function(_int):
            return _int
        result = decorated_function(3)
        self.assertEqual(result, 6)

    def test_parameterized_decorator(self):
        @decorators.parameterized_decorator(5)
        def decorated_function(_int):
            return _int
        result = decorated_function(3)
        self.assertEqual(result, 15)


if __name__ == "__main__":
    unittest.main()
