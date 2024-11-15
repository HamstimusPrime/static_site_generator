import os
from htmlnode import *
from extract_title import *
from markdown_to_html import *

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for item in os.listdir(dir_path_content):
        item_full_path = os.path.join(dir_path_content,item)
        
        if os.path.isfile(item_full_path,) and item.endswith(".md"):
            with open(item_full_path, "r") as file:
                markdown = file.read()
            page_title = extract_title(markdown)
            html_content = markdown_to_html_node(markdown).to_html()
            
            content_html = f"{item[:-3]}.html"
            os.makedirs(dest_dir_path, exist_ok= True)
            
            with open(os.path.join(dest_dir_path,content_html), "w") as file, open(template_path) as template:
                template_file = template.read()
                updated_template = (template_file.replace("{{ Title }}", page_title)).replace("{{ Content }}", html_content)
                file.write(updated_template)
        else:
            nested_content_dir = os.path.join(dir_path_content, item)
            nested_dest_dir = os.path.join(dest_dir_path, item)
            generate_pages_recursive(nested_content_dir, template_path, nested_dest_dir)
            
            

