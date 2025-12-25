from markdown_to_blocks import markdown_to_blocks , block_to_block_type, markdownBlockType
import unittest
class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
        
    def test_heading_valid(self):
        self.assertEqual(
            block_to_block_type("# Hello"),
            markdownBlockType.HEADING
        )
        self.assertEqual(
            block_to_block_type("###### Title"),
            markdownBlockType.HEADING
        )

    def test_heading_invalid_no_space(self):
        self.assertEqual(
            block_to_block_type("##Title"),
            markdownBlockType.PARAGRAPH
        )

    def test_heading_invalid_too_many_hashes(self):
        self.assertEqual(
            block_to_block_type("####### nope"),
            markdownBlockType.PARAGRAPH
        )

    def test_code_block(self):
        block = "```print('hi')```"
        self.assertEqual(
            block_to_block_type(block),
            markdownBlockType.CODE
        )

    def test_quote_block(self):
        block = "> hello\n> world"
        self.assertEqual(
            block_to_block_type(block),
            markdownBlockType.QUOTE
        )

    def test_quote_invalid_mixed_lines(self):
        block = "> hello\nworld"
        self.assertEqual(
            block_to_block_type(block),
            markdownBlockType.PARAGRAPH
        )

    def test_unordered_list(self):
        block = "- one\n- two\n- three"
        self.assertEqual(
            block_to_block_type(block),
            markdownBlockType.UNORDERED_LIST
        )

    def test_unordered_list_invalid(self):
        block = "- one\n* two"
        self.assertEqual(
            block_to_block_type(block),
            markdownBlockType.PARAGRAPH
        )

    def test_ordered_list_valid(self):
        block = "1. one\n2. two\n3. three"
        self.assertEqual(
            block_to_block_type(block),
            markdownBlockType.ORDERED_LIST
        )

    def test_ordered_list_invalid_wrong_start(self):
        block = "2. start wrong\n3. nope"
        self.assertEqual(
            block_to_block_type(block),
            markdownBlockType.PARAGRAPH
        )

    def test_ordered_list_invalid_wrong_sequence(self):
        block = "1. one\n3. wrong"
        self.assertEqual(
            block_to_block_type(block),
            markdownBlockType.PARAGRAPH
        )

    def test_paragraph(self):
        block = "This is a normal paragraph."
        self.assertEqual(
            block_to_block_type(block),
            markdownBlockType.PARAGRAPH
        )
        
if __name__ == "__main__":
    unittest.main()