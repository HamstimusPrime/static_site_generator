import unittest

from markdown_blocks import *

class TestBlockToBlock(unittest.TestCase):
    def test_heading_block(self):
        self.assertEqual(block_to_block_type("#"), "paragraph")
        self.assertEqual(block_to_block_type("#### this is a heading"), "heading")
        self.assertEqual(block_to_block_type("``` this is a test ```"), "code")
        self.assertEqual(block_to_block_type(">this is a test\n>this is also a test"), "quote")
        self.assertEqual(block_to_block_type(">this is a test\nthis is also a test"), "paragraph")
        self.assertEqual(block_to_block_type("1. this is an ordered list test\n2. this is also a test"), "ordered_list")
        self.assertEqual(block_to_block_type("1. this is a paragraph\nthis is also a test"), "paragraph")
        self.assertEqual(block_to_block_type("1. this is an ordered list test"), "ordered_list")
