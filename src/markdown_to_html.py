import re
from markdown_blocks import *
from htmlnode import *
from inline_markdown import *
from textnode import *




def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)

def block_to_html_node(markdown):
    block_list = markdown_to_blocks(markdown)
    for block in block_list:
        block_type = block_to_block_type(block)
        match block_type:
            case "heading":
                return heading_to_html_node(block)
            case "code":
                return code_to_html_node(block)
            case "quote":
                return quote_to_html_node(block)
            case "unordered_list":
                return unordered_list_to_html_node(block)
            case "ordered_list":
                return block_to_ordered_list(block)
            case "paragraph":
                return paragraph_to_html_node(block)
    
    
            
def text_to_children(text : str):
    text_nodes = text_to_textnodes(text)
    children = []
    for nodes in text_nodes:
        html_nodes = text_node_to_html_node(nodes)
        children.append(html_nodes)
    return children

def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"Invalid heading level: {level}")
    text = block[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)
                
# to code
def code_to_html_node(block : str):
    if not block.startswith("```") and not block.endswith("```"):
        raise Exception("invalid code")
    text = (block[4:-3]).strip()
    code =  ParentNode("code",text_to_children(text))
    return ParentNode("pre", [code])
    

# to quote
def quote_to_html_node(block : str):
    lines = block.split("\n")
    lines_with_quotes = []
    for line in lines:
        if not line.startswith(">"):
            raise Exception("invalid quote")    
        lines_with_quotes.append((line[1:]).strip())
    content = " ".join(lines_with_quotes)
    return ParentNode("blockquote",text_to_children(content))
    
# to unordered list

def unordered_list_to_html_node(block : str):
    items = []
    lines = block.split("\n")
    for line in lines:
        text = (line[2:])
        items.append(ParentNode("li",text_to_children(text)))
    return ParentNode("ol",items) 
        
# to ordered list  
def block_to_ordered_list(block):
    children = []
    lines = block.split("\n")
    for line in lines:
        text = (line[2:]).strip()
        children.append(ParentNode("li", text_to_children(text)))
    return ParentNode("ol", children) 
# to paragraph
def paragraph_to_html_node(block : str):
    lines = block.split("\n")
    paragragraph = " ".join(lines)
    return ParentNode("p", text_to_children(paragragraph))    



