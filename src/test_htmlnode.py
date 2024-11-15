import unittest

from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):
    def test_eq(self):
        test_prop = {
            "href": "https://www.google.com", 
            "target": "_blank",
        }

        html_node1 = HTMLNode(props=test_prop)
        print(html_node1.props_to_html())


if __name__ == "__main__":
    unittest.main()