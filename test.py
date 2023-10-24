import unittest

class TestArchiver(unittest.TestCase):

    def test_not_single(self):
        self.assertEqual('aaabbccccc', 'a3b2c5')

    def test_single(self):
            self.assertEqual('aaabccccc', 'a3bc5')

class TestUnpacker(unittest.TestCase):

    def test_not_single(self):
        self.assertEqual('a3b2c5', 'aaabbccccc')

    def test_single(self):
        self.assertEqual('a3bc5', 'aaabccccc')
