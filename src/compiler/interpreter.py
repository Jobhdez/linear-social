from parser import (
    Exps,
    Exp,
    Vec,
    Matrix,
    Int,
    Var,
    Sum,
    Minus,
    Product,
    Elements,
    Element,
    Vectors,
)
from utils import get_vector_elements, get_matrix_elements
from linear_algebra import V, Mat

def evaluate(ast):
    match ast:
        case Exp(exp):
            match exp:
                case Vec(elements):
                    vector_entries = get_vector_elements(elements)
                    return V(vector_entries)
                case Matrix(elements):
                    matrix_entries = get_matrix_elements(elements)
                    return Mat(matrix_entries)
        case Vec(elements):
            vector_entries = get_vector_elements(elements)
            return V(vector_entries)

        case Matrix(elements):
            matrix_elements = get_matrix_elements(elements)
            return Mat(matrix_elements)

