from sly import Lexer
class clexer(Lexer):
    literals={"(",")","{",",","}",";","=","+","-","*","/"}
    tokens={"INTEGER","ID","PRINT","INT"}
    INTEGER=r'[0-9]+'
    ID= r'[a-zA-Z_][a-zA-Z0-9_]*'
    ID['int'] = INT
    ID['print'] = PRINT
    ignore=" \t\n"
    def INTEGER(self,t):
        t.value=int(t.value)
        return t
# lexe=clexer()
# expr="int of integer = 5;"
# for tokens in lexe.tokenize(expr):
#     print(f'type={tokens.type},value={tokens.value}')