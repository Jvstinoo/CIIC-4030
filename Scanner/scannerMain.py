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


lexer = lex.lex()


lexer.input(data)

for tok in lexer:
    print(tok)
