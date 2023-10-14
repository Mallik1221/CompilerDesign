from sly import Lexer
class clexer(Lexer):
    literals={"(",")","{",",","}",";","="}
    tokens={"ID","PRINT","INT","DOUBLE","PLUS","MINUS","MUL","DIV","MOD","FACT","EQ","LE","LT","GE","GT","NE","LAND","LOR",'UNARY_PLUS', 'UNARY_MINUS'}
    PLUS=r'\+'
    MINUS=r'-'
    MUL=r'\*'
    DIV=r'/'
    MOD=r'%'
    EQ=r'=='
    LE= r'<='
    LT= r'<'
    GE= r'>='
    GT= r'>'
    NE= r'!='
    FACT=r'!'
    LAND=r'&&'
    LOR=r'\|\|'
    UNARY_PLUS = r'\+'
    UNARY_MINUS = r'-'
    INTEGER=r'[0-9]+'
    ID= r'[a-zA-Z_][a-zA-Z0-9_]*'
    ID['int']=INT
    ID['double']=DOUBLE
    ID['print']=PRINT
    # INT=r'int'
    # DOUBLE=r'double'
    # PRINT=r'print'
    ignore=" \t\n"

    def INTEGER(self,t):
        t.value=int(t.value)
        return t

    def DOUB(self,t):
        t.value=float(t.value)
        return t
# lexe=clexer()
# expr="int of integer = 5;"
# for tokens in lexe.tokenize(expr):
#     print(f'type={tokens.type},value={tokens.value}')
# lexer = clexer()
# expr="int main() { int a; double b; print a; }"
# for token in lexer.tokenize(expr):
#     print(f'type={token.type}, value={token.value}')
