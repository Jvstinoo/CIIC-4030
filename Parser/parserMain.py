import ply.yacc as yacc

from ply import lex

reserved = {
    "if": "IF",
    "else": "ELSE",
    "while": "WHILE",
    "let": "LET",
    "loop": "LOOP",
    "fn": "FN",
    "mut": "MUT",
    "pub": "PUB",
    "ref": "REF",
    "struct": "STRUCT",
    "return": "RETURN",
    "true": "TRUE",
    "false": "FALSE",
    "where": "WHERE",
    "write": "WRITE",
    "int": "INT",
    "float": "FLOAT",
    "char": "CHAR",
    "boolean": "BOOLEAN"
}

tokens = [
    "IDENTIFIER",
    "NUM",
    "LPAREN",
    "RPAREN",
    "LCURLY",
    "RCURLY",
    "LSQR",
    "RSQR",
    "SEMICOLON",
    "COMMA",
    "EQUALS",
    "NEQ",
    "LEQ",
    "GEQ",
    "LT",
    "GT",
    "PLUS",
    "MINUS",
    "STAR",
    "SLASH",
    "MOD",
    "EMPTY"
    ] + list(reserved.values()) 

t_ignore = " \t"


# Ignore C-style comments
def t_COMMENT(t):
    r"//.*|/\*[\w\W]*\*/"
    pass

t_LPAREN = r"\(" 
t_RPAREN = r"\)"
t_LCURLY = r"\{"
t_RCURLY = r"\}"
t_LSQR = r"\["
t_RSQR = r"\]"
t_SEMICOLON = r";"
t_COMMA = r","
t_EQUALS = r"="
t_NEQ = r"!="
t_LEQ = r"<="
t_GEQ = r">="
t_LT = r"<"
t_GT = r">"
t_PLUS = r"\+"
t_MINUS = r"-"
t_STAR = r"\*"
t_SLASH = r"/"
t_MOD = r"%"


def t_IDENTIFIER(t):
    r"[a-zA-Z_][a-zA-Z_0-9]*" 
    t.type = reserved.get(t.value, "IDENTIFIER")  # Check for reserved words
    return t


def t_NUM(t):
    r"[0-9]+"
    t.value = int(t.value)
    return t


# Ignored token with an action associated with it
def t_ignore_newline(t):
    r"\n+"
    t.lexer.lineno += t.value.count("\n")


# Error handler for illegal characters
def t_error(t):
    print(f"Illegal character {t.value[0]!r}")
    t.lexer.skip(1)


precedence = (('left', 'PLUS', 'MINUS'),
              ('left', 'STAR', 'SLASH'),
              ('left', 'EQUALS', 'NEQ', 'LEQ', 'GEQ', 'LT', 'GT'),)

def p_program(p):
    "program : statements"
    pass

def p_statements(p):
    """statements : statement
    | statements statement"""
    pass

def p_statement(p):
    """statement : assignment_statement
    | if_statement
    | if_else_statement
    | while_statement
    | action_statement
    | function
    | structure"""
    pass

def p_assignment_statement(p):
    '''assignment_statement : IDENTIFIER EQUALS expression SEMICOLON
    | let_expression EQUALS expression SEMICOLON '''
    pass

def p_if_statement(p):
    "if_statement : IF LPAREN expression RPAREN LCURLY statements RCURLY"
    pass

def p_if_else_statement(p):
    '''if_else_statement : IF LPAREN expression RPAREN LCURLY statements RCURLY ELSE LCURLY statements RCURLY
    | IF LPAREN expression RPAREN LCURLY statements RCURLY ELSE IF LPAREN expression RPAREN LCURLY statements RCURLY
    | IF LPAREN expression RPAREN LCURLY statements RCURLY ELSE IF LPAREN expression RPAREN LCURLY statements RCURLY ELSE LCURLY statements RCURLY''' 
    pass

def p_while_statement(p):
    "while_statement : WHILE LPAREN expression RPAREN LCURLY statements RCURLY"
    pass

def p_action_statement(p):
    """action_statement : RETURN expression
    | WRITE expression
    | WHERE expression
    | LOOP expression"""
    pass

def p_expression(p):
    """expression : operation_expression
    | boolean_expression
    | IDENTIFIER"""
    pass

def p_operation_expression(p):
    """operation_expression : expression PLUS expression
    | expression MINUS expression
    | expression STAR expression
    | expression SLASH expression
    | expression MOD expression
    | expression NEQ expression
    | expression LEQ expression
    | expression GEQ expression
    | expression LT expression
    | expression GT expression
    | LPAREN expression RPAREN
    | NUM"""
    pass

def p_boolean_expression(p):
    """boolean_expression : TRUE
    | FALSE"""
    pass

def p_function(p):
    """function : FN IDENTIFIER LPAREN list_parameters RPAREN type LCURLY statements RCURLY"""
    pass

def p_list_parameters(p):
    """list_parameters : 
                       | IDENTIFIER type 
                       | IDENTIFIER type COMMA list_parameters"""
    pass

def p_structure(p):
    """structure : STRUCT IDENTIFIER LCURLY statements RCURLY"""
    pass

def p_let_expression(p):
    """let_expression : LET IDENTIFIER
    | LET MUT IDENTIFIER
    | LET REF IDENTIFIER"""
    pass

def p_type(p):
    """type : INT
    | FLOAT
    | CHAR
    | BOOLEAN"""
    pass

def p_error(p):
    if (p):
        print("Syntax error in input" + str(p))

lexer = lex.lex()
parser = yacc.yacc()

with open('test_file.txt', 'r') as f:
    data = f.read()

lexer.input(data)
for tok in lexer:
    print(tok)

result = parser.parse(data)

