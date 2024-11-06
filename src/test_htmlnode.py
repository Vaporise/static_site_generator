import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_multiple_attributes(self):
        # Test with multiple attributes
        node_with_props = HTMLNode(tag="a", value=None, children=None, props={
            "href": "https://www.example.com",
            "target": "_blank"
        })
        self.assertEqual(node_with_props.props_to_html(), ' href="https://www.example.com" target="_blank"')

    def test_props_to_html_single_attribute(self):
        # Test with single attribute
        node_with_single_prop = HTMLNode(tag="img", value=None, children=None, props={
            "alt": "An image"
        })
        self.assertEqual(node_with_single_prop.props_to_html(), ' alt="An image"')    

    def test_props_to_html_no_attributes(self):
        # Test with no attributes
        node_no_props = HTMLNode(tag="p")
        self.assertEqual(node_no_props.props_to_html(), '')

    def test_props_to_html_none_as_props(self):
        # Test with None as props
        node_none_props = HTMLNode(tag="div", props=None)
        self.assertEqual(node_none_props.props_to_html(), '')

class TestLeafNode(unittest.TestCase):

    def test_to_html_with_P_tags(self):
        node_with_p_tags = LeafNode(tag="p", value="This is content")
        self.assertEqual(node_with_p_tags.to_html(), "<p>This is content</p>")

    def test_to_html_with_various_tags(self):
        bold_node = LeafNode(tag="b", value="Bold Text")
        strong_node = LeafNode(tag="strong", value="Strong Text")
    
        self.assertEqual(bold_node.to_html(), "<b>Bold Text</b>")
        self.assertEqual(strong_node.to_html(), "<strong>Strong Text</strong>")

    def test_to_html_no_tag(self):
        node_with_no_tag = LeafNode(tag=None, value="Plain Text")
    
        self.assertEqual(node_with_no_tag.to_html(), "Plain Text")


if __name__ == "__main__":
    unittest.main()