import os
import shutil
from textnode import TextNode
from generate_pages_recursive import *




def main():
    static_directory = "./static"
    public_directory = "./public"
    content_path_dir = "./content"
    dest_directory = "./public"
    template_path = "./template.html"
    
    copy_content(static_directory, public_directory)
    generate_pages_recursive(content_path_dir, template_path,dest_directory )

def copy_content(source_dir, destination_dir):
    if os.path.exists(destination_dir): 
        shutil.rmtree(destination_dir)
    os.mkdir(destination_dir)
    src_dir_content = os.listdir(source_dir)
    if len(src_dir_content) == 0:
        return
    for item in src_dir_content:
        nxt_src_dir = os.path.join(source_dir,item)
        file_path = os.path.join(source_dir, item)
        if os.path.isfile(file_path):
            shutil.copy(file_path,destination_dir)
            continue
        destination_path = os.path.join(destination_dir,item)
        os.mkdir(destination_path)
        copy_content(nxt_src_dir, destination_path)



if __name__ == "__main__":
    main()
    
    
    