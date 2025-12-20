from textnode import TextNode, TextType

def main():
    node1 = TextNode("Hello, World!", TextType.BOLD)
    node2 = TextNode("Click here", TextType.LINK, url="https://example.com")
    
    print(node1)
    print(node2)

if __name__ == "__main__":
    main()