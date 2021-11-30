# AUTHOR: Gloriel M. Soto Maldonado

import ply.lex as lex

# TOKENS MADE FOR GRAMMAR
reserved = {
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'let': 'LET',
    'in': 'IN',
    'to': 'TO',
    'true': 'TRUE',
    'false': 'FALSE',
    'cons': 'CONS',
}

tokens = ['CHARACTER',
          'DIGIT',
          'LP',
          'RP',
          'LB',
          'RB',
          'COMMA',
          'PLUS',
          'MINUS',
          'TILDE',
          'TIMES',
          'DIVIDE',
          'EQ',
          'NEQ',
          'LT',
          'GT',
          'LEQ',
          'GEQ',
          'AND',
          'OR',
          'ASSIGN'
          ] + list(reserved.values())

# OFFICIAL TOKENS
t_ignore = ' \t'
t_CHARACTER = r'[a-z]|[A-Z]|\?|_'
t_DIGIT = r'[0-9]'

# DELIMITER TOKENS
t_LP = r'\('
t_RP = r'\)'
t_COMMA = r'\,'

# OPERATOR TOKENS
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TILDE = r'\~'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_EQ = r'\='
t_NEQ = r'\!\='
t_LT = r'\<'
t_GT = r'\>'
t_LEQ = r'\<\='
t_GEQ = r'\>\='
t_AND = r'\&'
t_OR = r'\|'
t_ASSIGN = r'\:\='


def t_reserved(t):
    r"""if | then | else | let | in | map | to | true | false | number\? | function\? | list\? | empty\? | empty | cons\? |
    cons | first | rest | arity"""
    if t.value in reserved:
        t.type = reserved[t.value]
    return t


def t_newline(t):
    r"""\n+"""
    t.lexer.lineno += len(t.value)


def t_error(t):
    print(t)
    raise TypeError("Illegal character written above.")


print("Building Lexer...")
lex.lex()
print("Lexer Built Successfully.")

# Testing the lexer
# data = open("Test.txt", "r").read()
# lex.input(data)
# while True:
#     tok = lex.token()
#     if not tok:
#         break
#     print(tok)
