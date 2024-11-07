class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def __to_html__(self):
        raise NotImplementedError

    def props_to_html(self):
        props_string = ""

        if self.props == None:
            return ""

        for key, value in self.props.items():
            props_string += f' {key}="{value}"'
        
        return props_string

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value):
        super().__init__(tag, value, children=None)
        
    def to_html(self):
        if self.value == None:
            raise ValueError("LeafNode must have a value.")
        if self.tag == None:
            return self.value
        return f'<{self.tag}>{self.value}</{self.tag}>'


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag == "":
            raise ValueError("Invalid Tag")
        if not self.children:
            raise ValueError("Invalid Children")

        children_html = ""
        for child in self.children:
            children_html += child.to_html()

        return f"<{self.tag}>{children_html}</{self.tag}>"


