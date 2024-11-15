from htmlnode import *
from markdown_to_html import *
from extract_title import *
import os


def generate_page(from_path, template_path, dest_path):
    
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path) as file:
        path_file  = file.read()
    page_title = extract_title(path_file)
        
    with open(template_path) as file:
        template_file = file.read()
    
    html_content = (markdown_to_html_node(path_file)).to_html()
    html_file = (template_file.replace("{{ Title }}", page_title)).replace("{{ Content }}",html_content)
    
    try:
        dest_directory = os.path.dirname(dest_path)
        os.makedirs(dest_directory, exist_ok= True)
    except Exception as e:
        print(f"invalid directory path provided---> {dest_directory} ---error---{e}")
    
    with open(dest_path, "w") as file:
        file.write(html_file)
    

    

from_string = "/Users/mohammed/workspace/github.com/hamstimusprime/static_site_generator/content/index.md"