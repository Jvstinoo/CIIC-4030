
data = textFile.read()

lexer.input(data)

for tok in lexer:
print(tok)
