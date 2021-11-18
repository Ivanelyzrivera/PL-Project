# Author: Gloriel M. Soto Maldonado

import ply.yacc as yacc
# import lexer
# tokens = lexer.tokens

def mainexplist(p):
    """mainexplist : explist
		           | empty"""


def explist(p):
    """explist : exp
               | exp COMMA explist"""


def exp(p):
    """exp : term
           | term binop exp
           | IF exp THEN exp ELSE exp
           | LET def IN exp
           | MAP idlist TO exp"""


def term(p):
    """term : unop term
            | factor
            | factor LP mainexplist RP
            | empty
            | int
	        | string
            | bool"""


def factor(p):
    """factor   : LP exp RP
                | prim
                | id
		        | string"""


def define(p):
    """define  : id ASSIGN exp SC
                | id ASSIGN exp SC define"""


def idlist(p):
    """idlist   : propidlist
                | empty"""


def propidlist(p):
    """propidlist   : id
                    | id COMMA propidlist"""


def bool(p):
    """bool : TRUE
            | FALSE"""


def unop(p):
    """unop : sign
            | TILDE """


def binop(p):
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


def sign(p):
    """sign : PLUS
            | MINUS """


def prim(p):
    """prim : NUMQ
            | FUNQ
            | LISTQ
            | EMPTYQ
            | CONSQ
            | CONS
            | FIRST
            | REST
            | ARITY"""


def id(p):
    """id   :
            | id
            | int
            | int id
            | string
            | string id"""


# def p_id(p):
#     '''id   :
#             | id CHARACTER?
#             | id DIGIT
#             | id NAME
#             | id REGION
#             | id SERVER
#             | id ID
#             | id TAG
#             | id OS '''

def int(p):
    """int  : DIGIT
            | DIGIT int"""


def string(p):
    """string : CHARACTER
              | CHARACTER string"""


def empty(p):
    """empty :
             | EMPTY"""


def error(p):
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
