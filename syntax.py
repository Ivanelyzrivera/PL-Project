# Author: Gloriel M. Soto Maldonado

import ply.yacc as yacc
import lexer

tokens = lexer.tokens


def p_explist(p):
    """explist  : propexplist
                | empty"""


def p_propexplist(p):
    """propexplist  : exp
                    | exp COMMA propexplist"""


def p_exp(p):
    """exp  : term
            | term binop exp
            | IF exp THEN exp ELSE exp
            | LET def IN exp
            | MAP idlist TO exp"""


def p_term(p):
    """term : unop term
            | factor
            | factor LP explist RP
            | empty
            | int
            | string
            | bool"""


def p_factor(p):
    """factor   : LP exp RP
                | prim
                | id"""


def p_def(p):
    """def  : id ASSIGN exp SC
            | id ASSIGN exp SC def"""


def p_idlist(p):
    """idlist   : propidlist
                | empty"""


def p_propidlist(p):
    """propidlist   : id
                    | id COMMA propidlist"""


def p_bool(p):
    """bool : TRUE
            | FALSE"""


def p_unop(p):
    """unop : sign
            | TILDE """


def p_binop(p):
    """binop    : sign
                | TIMES
                | DIVIDE
                | EQ
                | NEQ
                | LT
                | GT
                | LEQ
                | GEQ
                | AND
                | OR """


def p_sign(p):
    """sign : PLUS
            | MINUS """


def p_prim(p):
    """prim : NUMQ
            | FUNQ
            | LISTQ
            | EMPTYQ
            | CONSQ
            | CONS
            | FIRST
            | REST
            | ARITY"""


def p_id(p):
    """id   : type
            | type int
            | type string"""


def p_type(p):
    """type :
            | NAME
            | REGION
            | SERVER
            | OS
            | ID
            | TAG"""


# def p_id(p):
#     '''id   : CHARACTER
#             | id CHARACTER
#             | id DIGIT '''

def p_int(p):
    """int  : DIGIT
            | DIGIT int"""


def p_string(p):
    """string  : CHARACTER
               | CHARACTER string"""


def p_empty(p):
    """empty    :
                | EMPTY"""


def p_error(p):
    print("Syntax Error: ")
    print(p)
    raise TypeError("Error in Syntax. Check token above to fix.")


print("Building Parser...")
parser = yacc.yacc()
print("Parser Built Successfully.")

# Testing the parser
# fileName = "Test.txt"
# print("Parsing " + fileName + "...")
# data = open(fileName, "r").read()
# parser.parse(data)
# print("Parsing " + fileName + " Successful.")
# print("Finished.")
