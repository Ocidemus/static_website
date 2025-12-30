from textnode import *
from htmlnode import *
from inline_to_markdown import *
from markdown_to_blocks import *
import os
import shutil
import sys

def generate_pages_recursively(dir_path_content, template_path, dest_dir_path , basepath):
    for item in os.listdir(dir_path_content):
        s = os.path.join(dir_path_content,item)
        d = os.path.join(dest_dir_path,item)
        if os.path.isdir(s):
            os.makedirs(d, exist_ok=True)
            generate_pages_recursively(s, template_path, d, basepath)
        else:
            if item.endswith(".md"):
                dest_file = os.path.splitext(d)[0] + ".html"
                generate_page(s, template_path, dest_file, basepath)  

def generate_page(from_path, template_path, dest_path , basepath):
    print(f"Generating page from {from_path} to {dest_path} using template {template_path}")
    with open(from_path, "r", encoding="utf-8") as f:
        md_content = f.read()
        html_content = markdown_to_html_node(md_content).to_html()
    with open(template_path, "r", encoding="utf-8") as f:
        template_content = f.read()
        
    title = extract_title(md_content)
    template_content = template_content.replace("{{ title }}", title)
    final_content = template_content.replace("{{ content }}", html_content)

    final_html = final_content.replace('href="/', f'href="{basepath}')
    final_html = final_html.replace('src="/', f'src="{basepath}')
    
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(final_html)

def copy_files(items, source_dir, dest_dir):
    for item in items:
        s=os.path.join(source_dir, item)
        d=os.path.join(dest_dir, item)
        if os.path.isdir(s):
            items2 = os.listdir(s)
            os.makedirs(d, exist_ok=True)
            copy_files(items2, s, d)
        else:
            shutil.copy2(s,d)
            
def main():
    
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = ""
    
    d = "docs"
    s = "static"
    if os.path.exists(d) and os.path.isdir(d):
            if os.listdir(d):
                shutil.rmtree(d)
    else:
        os.makedirs(d)
    items = os.listdir(s)
    copy_files(items, s, d)
    generate_pages_recursively("content", "template.html", "docs", basepath)
    
    

if __name__ == "__main__":
    main()