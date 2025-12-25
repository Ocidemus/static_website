from enum import Enum
import re


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
    import re

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

