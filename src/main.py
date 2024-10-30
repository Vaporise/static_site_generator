from textnode import TextType, TextNode

def main():
    node = TextNode(
        "Dog",
        TextType.BOLD,
        "www.dog.com"
    )
    print(node)

if __name__ == "__main__":
    main()