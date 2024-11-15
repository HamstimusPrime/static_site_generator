from textnode import *
import re

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes






def extract_markdown_images(markdown):
    matching_pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(matching_pattern, markdown)

def extract_markdown_links(markdown):
    matching_pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(matching_pattern, markdown)
    
def split_nodes_image(old_nodes):
    node_list = []
    for node_object in old_nodes:
        if not node_object.text:
            continue 
        matched_image_text_and_link = extract_markdown_images(node_object.text)
        if len(matched_image_text_and_link) == 0:
            node_list.append(node_object)
            continue
        for image_and_link in matched_image_text_and_link:
            delimiter = f'![{image_and_link[0]}]({image_and_link[1]})'
            filtered_text = node_object.text.split(delimiter, 1)
            #if the first image_and_link is a blank string, it means that's there was a text and link in that position, so just create a TextNode to the node list
            if filtered_text[0] == "":
                node_list.append(TextNode(image_and_link[0], TextType.IMAGE, image_and_link[1]))
                continue
            if len(filtered_text) != 2:
                raise Exception("invalid image value")
            node_list.extend([TextNode(filtered_text[0],
                                      TextType.TEXT),
                             TextNode(image_and_link[0],
                                      TextType.IMAGE, image_and_link[1])])
            node_object.text = filtered_text[1]
        if node_object.text:  # if there's any text left
            node_list.append(TextNode(node_object.text, TextType.TEXT))
    return node_list

def split_nodes_link(old_nodes):
    node_list = []
    for node_object in old_nodes:
        if not node_object.text:
            continue 
        matched_image_text_and_link = extract_markdown_links(node_object.text)
        if len(matched_image_text_and_link) == 0:
            node_list.append(node_object)
            continue
        for link in matched_image_text_and_link:
            delimiter = f'[{link[0]}]({link[1]})'
            filtered_text = node_object.text.split(delimiter, 1)
            #if the first image_and_link is a blank string, it means that's there was a text and link in that position, so just create a TextNode to the node list
            if filtered_text[0] == "":
                node_list.append(TextNode(link[0], TextType.LINK, link[1]))
                continue
            if len(filtered_text) != 2:
                raise Exception("invalid image value")
            node_list.extend([TextNode(filtered_text[0],
                                      TextType.TEXT),
                             TextNode(link[0],
                                      TextType.LINK, link[1])])
            node_object.text = filtered_text[1]
        if node_object.text:  # if there's any text left
            node_list.append(TextNode(node_object.text, TextType.TEXT))
    return node_list
