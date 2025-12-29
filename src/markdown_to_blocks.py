from enum import Enum
from textnode import TextNode, TextType , text_node_to_html_node
from inline_to_markdown import split_nodes_delimiter, split_nodes_image, split_nodes_link , text_to_textnodes
import re
from htmlnode import *

class markdownBlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"
    
    
def markdown_to_blocks(markdown):
    blocks= markdown.split("\n\n")
    blocks= [block.strip() for block in blocks]
    blocks= [block for block in blocks if block ]
    return blocks

def block_to_block_type(block):
    if re.match(r'^#{1,6}\s+.+$', block):
        return markdownBlockType.HEADING
    
    elif block.startswith("```") and block.endswith("```"):
        return markdownBlockType.CODE
    
    lines = block.split("\n")
    if all(line.startswith(">") for line in lines):
        return markdownBlockType.QUOTE
    
    elif all(line.startswith("- ") for line in lines):
        return markdownBlockType.UNORDERED_LIST
    
    else:
        for i, line in enumerate(lines, start=1):
            if not re.match(rf'^{i}\.\s', line):
                break
        else:
            return markdownBlockType.ORDERED_LIST

    return markdownBlockType.PARAGRAPH

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []

    for block in blocks:
        children.append(block_to_html_node(block))

    return ParentNode("div", children)


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_children = [text_node_to_html_node(tn) for tn in text_nodes]
    return html_children

def block_to_html_node(block):
    block_type = block_to_block_type(block)

    if block_type == markdownBlockType.HEADING:
        return heading_to_node(block)

    if block_type == markdownBlockType.PARAGRAPH:
        return paragraph_to_node(block)

    if block_type == markdownBlockType.QUOTE:
        return quote_to_node(block)

    if block_type == markdownBlockType.UNORDERED_LIST:
        return ul_to_node(block)

    if block_type == markdownBlockType.ORDERED_LIST:
        return ol_to_node(block)

    if block_type == markdownBlockType.CODE:
        return code_to_node(block)

def heading_to_node(block):
    level = len(re.match(r'^(#+)', block).group(1))
    text = block[level+1:].strip()
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)

def paragraph_to_node(block):
    text = " ".join(block.split("\n"))
    text = re.sub(r'\s+', ' ', text).strip()
    children = text_to_children(text)
    return ParentNode("p", children)

def quote_to_node(block):
    lines = [line[1:].strip() for line in block.split("\n")]
    text = " ".join(lines)
    children = text_to_children(text)
    return ParentNode("blockquote", children)

def ul_to_node(block):
    items = []
    for line in block.split("\n"):
        text = line[2:].strip()
        li_children = text_to_children(text)
        items.append(ParentNode("li", li_children))
    return ParentNode("ul", items)

def ol_to_node(block):
    items = []
    for line in block.split("\n"):
        text = re.sub(r'^\d+\.\s', "", line).strip()
        li_children = text_to_children(text)
        items.append(ParentNode("li", li_children))
    return ParentNode("ol", items)

def code_to_node(block):
    content = block[3:-3]

    if content.startswith("\n"):
        content = content[1:]   

    code_node = LeafNode("code", content)
    return ParentNode("pre", [code_node])

