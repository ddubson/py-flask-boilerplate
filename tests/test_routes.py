import unittest

from web_service.routes import index


class TestRoutes(unittest.TestCase):
    def test_index(self):
        self.assertEqual(index(), "Hello, World!")
