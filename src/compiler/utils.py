from parser import Elements
from parser import Element

def get_vector_elements(ast):
    """given an AST it takes the elements of a vector and puts them in a list."""
    while ast is not None:
        if isinstance(ast, Elements):
            elements.append(ast.e1)
            ast = ast.elements

        else:
            elements.append(ast.exp)
            ast = None