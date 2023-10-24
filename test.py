import unittest

from main import archiver, unpacker

class TestArchiver(unittest.TestCase):

    def test_not_single(self):
        self.assertEqual(archiver('aaabbccccc'), 'a3b2c5')

    def test_single(self):
        self.assertEqual(archiver('aaabccccc'), 'a3bc5')

    def test_multi_digit(self):
        self.assertEqual(archiver('aaabcccccccccc'), 'a3bc10')


class TestUnpacker(unittest.TestCase):

    def test_not_single(self):
        self.assertEqual(unpacker('a3b2c5'), 'aaabbccccc')

    def test_single(self):
        self.assertEqual(unpacker('a3bc5'), 'aaabccccc')

    def test_multi_digit(self):
        self.assertEqual(unpacker('a3bc10'), 'aaabcccccccccc')
