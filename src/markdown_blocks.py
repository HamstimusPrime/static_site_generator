import re


def markdown_to_blocks(markdown):
    return re.split(r"\n{2,}", markdown)

def block_to_block_type(block):
    multiple_line_block = block.split("\n")
    contains_multiple_lines = "\n" in block
    
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return "heading"
    
    if block[0:3] == "```":
        code_pattern = r"^```([^`]+)```$"
        if contains_multiple_lines:
            if (re.findall(code_pattern,multiple_line_block[0]) 
            and re.findall(code_pattern, multiple_line_block[-1])):
                return "code"
        if re.findall(code_pattern, block):
            return "code"
    
    if block.startswith(">"):
        for line in multiple_line_block:
            if not line.startswith(">"):
                return "paragraph"
        return "quote"
        
    if block.startswith("* "):
        for line in multiple_line_block:
            if not line.startswith("* "):
                return "paragraph"
        return "unordered_list"
        
        
    if block[0].isnumeric() and block[0:3] == "1. ":
        is_ordered_list = True
        first_list_number = int(block[0])
        if contains_multiple_lines:
            for line in multiple_line_block:
                if not line[0].isnumeric() or int(line[0]) != first_list_number:
                    is_ordered_list = False
                    break
                else:
                    first_list_number += 1   
        if is_ordered_list: return "ordered_list"
    
    return "paragraph"