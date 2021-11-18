# AUTHOR: Gloriel M. Soto Maldonado

import ply.lex as lex

# TOKENS MADE FOR GRAMMAR
reserved = {
        'if' : 'IF', 'then' : 'THEN', 'else' : 'ELSE',
        'let' : 'LET', 'in' : 'IN', 'map' : 'MAP',
        'to' : 'TO', 'true' : 'TRUE', 'false': 'FALSE',
        'empty': 'EMPTY', 'number?' : 'NUMQ', 'function?' : 'FUNQ',
        'list?' : 'LISTQ', 'empty?' : 'EMPTYQ', 'cons?' : 'CONSQ',
        'cons' : 'CONS', 'first' : 'FIRST', 'rest' : 'REST',
        'arity' : 'ARITY'
}
# tokens = [ 'CHARACTER', 'DIGIT', 'DELIMITER', 'OPERATOR', 'PRIMKW' ] + list(reserved.values())
# reserved = [ 'IF', 'THEN', 'ELSE', 'LET', 'IN', 'MAP', 'TO',
#              'TRUE', 'FALSE', 'EMPTY', 'NUMQ', 'FUNQ', 'LISTQ', 'EMPTYQ',
#              'CONSQ', 'CONS', 'FIRST', 'REST', 'ARITY']
tokens = [ 'CHARACTER',
           'DIGIT',
           'LP', 'RP', 'LB', 'RB', 'COMMA', 'SC',
           'PLUS', 'MINUS', 'TILDE', 'TIMES', 'DIVIDE', 'EQ', 'NEQ',
           'LT', 'GT', 'LEQ', 'GEQ', 'AND', 'OR', 'ASSIGN' ] + list(reserved.values())

# OFFICIAL TOKENS
t_ignore    = ' \t'
t_CHARACTER = r'[a-z]|[A-Z]|\?|_'
t_DIGIT     = r'[0-9]'
#t_DELIMITER = r'\{|\}|\(|\)|\,|\;'
# t_OPERATOR  = r'\+|\-|\~|\*|\/|\=|\!\=|\<|\>|\<\=|\>\=|\&|\||\:\='

# DELIMITER TOKENS
t_LP = r'\('; t_RP = r'\)'; t_LB = r'\['; t_RB = r'\]'
t_COMMA = r'\,'; t_SC = r'\;'

# OPERATOR TOKENS
t_PLUS = r'\+'; t_MINUS = r'\-'; t_TILDE = r'\~'; t_TIMES = r'\*'
t_DIVIDE = r'\/'; t_EQ = r'\='; t_NEQ = r'\!\='; t_LT = r'\<'
t_GT = r'\>'; t_LEQ = r'\<\='; t_GEQ = r'\>\='; t_AND = r'\&'
t_OR = r'\|'; t_ASSIGN = r'\:\='

# RESERVED TOKENS
# SIMPLE GRAMMAR
# t_IF = r'if'; t_THEN = r'then'; t_ELSE = r'else'; t_LET = r'let'
# t_IN = r'in'; t_MAP = r'map'; t_TO = r'to'; t_EMPTY = r'empty'
# BOOLEANS
# t_TRUE = r'true'; t_FALSE = r'false'
# PRIMITIVE KEYWORDS
# t_PRIMKW = r'number\?|function\?|list\?|empty\?|cons\?|cons|first|rest|arity'
# t_NUMQ = r'number\?'; t_FUNQ = r'function\?'; t_LISTQ = r'list\?'; t_EMPTYQ = r'empty\?'
# t_CONSQ = r'cons\?'; t_CONS = r'cons'; t_FIRST = r'first'; t_REST = r'rest'
# t_ARITY = r'arity'

def t_reserved(t):
    r'if | then | else | let | in | map | to | true | false | number\? | function\? | list\? | empty\? | empty | cons\? | cons | first | rest | arity'
    if t.value in reserved:
        t.type = reserved[t.value]
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    # print("Illegal character " + t.value[0])
    # t.lexer.skip(1)
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
