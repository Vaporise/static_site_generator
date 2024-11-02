import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_init(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.dog.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "www.dog.com")
        self.assertEqual(node, node2)
    
    def test_notequal(self):
        node = TextNode("This is a text nod", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_nourl(self):
        node = TextNode("Text", TextType.ITALIC)
        self.assertIsNone(node.url)

if __name__ == "__main__":
    unittest.main()