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
                    return vector_entries

                case Matrix(elements):
                    matrix_entries = get_matrix_elements(elements)
                    return matrix_entries

                case Sum(e1,e2):
                    vec = get_vector_elements(e1.elements)
                    vec2 = get_vector_elements(e2.elements)
                    vec_object = V(vec)
                    vec2_object = V(vec2)
                    return vec_object + vec2_object

                case Minus(e1,e2):
                    vec = get_vector_elements(e1.elements)
                    vec2 = get_vector_elements(e2.elements)
                    vec_object = V(vec)
                    vec2_object = V(vec2)
                    return vec_object - vec2_object

                case Product(e1,e2):
                    operand = V(get_vector_elements(e1.elements)) if isinstance(e1, Vec) else e1.num
                    operand2 = V(get_vector_elements(e2.elements)) if isinstance(e2, Vec) else e2.num
            
                    return operand * operand2

        case Vec(elements):
            vector_entries = get_vector_elements(elements)
            return V(vector_entries)

        case Matrix(elements):
            matrix_elements = get_matrix_elements(elements)
            return Mat(matrix_elements)

