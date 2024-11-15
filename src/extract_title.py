from markdown_blocks import *


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("#") and line.count("#") == 1:
            return (line[1:]).lstrip()
    raise Exception("No Title found")     
            
    