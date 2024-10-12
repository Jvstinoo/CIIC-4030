import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from scannerMain import tokens

symbols = {}


def p_program(p):
    "program : statements"
    p[0] = p[1]


def p_statements(p):
    "statements : statement | statements statement"
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 3:
        p[0] = p[1]


def p_statement(p):
    "statement : assignment_statement | if_statement | if_else_statement | while_statement | action_statement"
    p[0] = p[1]


def p_assignment_statement(p):
    "assignment_statement : ID EQUALS expression SEMICOLON"
    symbols[p[1]] = p[3]


def p_if_statement(p):
    "if_statement : IF LPAREN expression RPAREN LCURLY statements RCURLY"


def p_if_else_statement(p):
    "if_else_statement : IF LPAREN expression RPAREN LCURLY statements RCURLY ELSE LCURLY statements RCURLY"


def p_while_statement(p):
    "while_statement : WHILE LPAREN expression RPAREN LCURLY statements RCURLY"


def p_action_statement(p):
    "action_statement : RETURN expression | WRITE expression | WHERE expression | LOOP expression"


def p_expression(p):
    "expression : operation_expression | boolean_expression"


def p_operation_expression(p):
    "operation_expression : expression PLUS expression | expression MINUS expression | expression STAR expression | expression SLASH expression | expression MOD expression | expression NEQ expression | expression LEQ expression | expression GEQ expression | expression LT expression | expression GT expression | LPAREN expression RPAREN | NUMBER"
    if len(p) == 4:
        if p[2] == "+":
            p[0] = p[1] + p[3]
        if p[2] == "-":
            p[0] = p[1] - p[3]
        if p[2] == "*":
            p[0] = p[1] * p[3]
        if p[2] == "/":
            p[0] = p[1] / p[3]
        if p[2] == "%":
            p[0] = p[1] % p[3]
        if p[2] == "!=":
            p[0] = p[1] != p[3]
        if p[2] == "<=":
            p[0] = p[1] <= p[3]
        if p[2] == ">=":
            p[0] = p[1] >= p[3]
        if p[2] == "<":
            p[0] = p[1] < p[3]
        if p[2] == ">":
            p[0] = p[1] > p[3]
        if p[1] == "(" and p[3] == ")":
            p[0] = p[1]  # Might need to do some extra work here.
    elif len(p) == 2:
        p[0] = p[1]


def p_boolean_expression(p):
    "boolean_expression : TRUE | FALSE"
    p[0] = p[1]


def p_function(p):
    "function : FN ID LPAREN list_parameters RPAREN type LCURLY statements RCURLY"


def p_list_parameters(p):
    "list_parameters : empty | ID type | ID type COMMA list_parameters"
    if (len(p) == 3):



def p_struct(p):
    "STRUCT : ID LCURLY statements RCURLY"


def p_let_expression(p):
    "let expression : let ID | let MUT IDENTIFIER | let REF ID"


def p_type(p):
    "type : int | float | char | boolean"
    if (
        p.value != "int"
        or p.value != "float"
        or p.value != "char"
        or p.value != "boolean"
    ):
        return False
    return True


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")


parser = yacc.yacc()

while True:
    try:
        s = input("calc > ")
    except EOFError:
        break
    if not s:
        continue
    result = parser.parse(s)
    print(result)
