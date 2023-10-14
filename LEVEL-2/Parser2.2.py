from sly import Parser
from lexer1 import *
from symboltable import *
from ast_1 import *
from abc import *
from function import Function
from program import *

'''

<program>  :=  <return_type><identifier>() {  <statements> }
<return_type> :=  int
<statements> :=  <statement>; <statements> | <statement>;
<statement> := <declaration_stmt> |  <assignment_stmt> | <print_stmt>
<declaration_stmt> := <type> <list_of_variables>
<list_of_variables> := <identifier> , <list_of_variables> |  <identifier>
<assignment_stmt> := <identifier> = <expr>
<print_stmt>            :=  print <identifier>
<type>                     :=  int | double
<expr>       :=  <expr> <arop> <expr> | <expr> <relop> <expr> | <expr> <logop> <expr>
<arop>      := + | - | * | / | %
<relop>     :=  > | < | >= | <= | == | !=
<logop>    :=  && | || 
<expr>      :=  <unaryop> <expr> | ( <expr>)
<unrayop>  :=  + | -  | (<type>) | !
<expr>      := <identifier>  | <intconstant>  | <doubleconstant>  
<identifier>   rule is similar to C
<intconstant>  integer constant rule is similar to C 
<doubleconstant> rule is one or more digits and optional fractional part where optional fractional part is dot followed by one or more digits.  



'''

class CParser(Parser):
    literals=clexer.literals
    tokens = clexer.tokens
    stable=SymbolTable()
    precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MUL', 'DIV', 'MOD'),)
    @_('return_type ID "(" ")" "{" statements "}"')
    def program(self, value):
        main_function = Function(value.return_type, value.ID)
        main_function.statementsAstList=value.statements
        program_ast = Program()
        program_ast.addFunctionDetails(value.ID, main_function)
        main_function_entry = SymbolTableEntry(value.ID, value.return_type)
        print_ast = PrintAst(main_function_entry)
        program_ast.print()
        return program_ast

    @_('INT')
    def return_type(self, value):
        return DataType.INT

    @_('statement ";" statements')
    def statements(self, value):
        return [value.statement] + value.statements
    
    @_('statement ";"')
    def statements(self, value):
        return [value.statement]

    @_('declaration_stmt')
    def statement(self, value):
        return value[0]

    @_('assignment_stmt')
    def statement(self, value):
        return value[0]

    @_('print_stmt')
    def statement(self, value):
        return value[0]

    @_('type list_of_variables')
    def declaration_stmt(self, value):
        DataType = value.type
        variables = value.list_of_variables
        for variable in variables:
                self.stable.addSymbol(SymbolTableEntry(variable, DataType))

    @_('ID "," list_of_variables')
    def list_of_variables(self, value):
        return [value[0]] + value[2]

    @_('ID')
    def list_of_variables(self, value):
        return [value[0]]
    
    @_('ID "=" expr')
    def assignment_stmt(self,value):
        return AssignAst(NameAst(value[0]),value[2],value.lineno)
    
    @_('PRINT ID')
    def print_stmt(self, value):
        keyword = value[0]
        variable_name = self.stable.getSymbolEntry(value[1])
        return PrintAst(NameAst(variable_name.name))

    @_('INT')
    def type(self, value):
        keyword = value[0]
        return keyword
    
    @_('DOUBLE')
    def type(self,value):
        keyword=value[0]
        return keyword
    
    @_('expr arop expr')
    def expr(self,value):
        left_exp=value.expr0
        operator=value.arop
        right_exp=value.expr1

        if operator=='+':
            return AddAst(left_exp,right_exp,operator,value.lineno)
        elif operator=='-':
            return SubAst(left_exp,right_exp,operator,value.lineno)
        elif operator=='*':
            return MulAst(left_exp,right_exp,operator,value.lineno)
        elif operator=='/':
            return DivAst(left_exp,right_exp,operator,value.lineno)
        elif operator=='%':
            return PerAst(left_exp,right_exp,operator,value.lineno)
        else:
            raise ValueError(f"Invalid operator:{operator}")

    @_('expr relop expr')
    def expr(self,value):
        left_exp=value.expr0
        operator=value.relop
        right_exp=value.expr1

        if operator=='>':
            return GrtAst(left_exp,right_exp,operator,value.lineno)
        elif operator=='<':
            return LstAst(left_exp,right_exp,operator,value.lineno)
        elif operator=='>=':
            return GeAst(left_exp,right_exp,operator,value.lineno)
        elif operator=='<=':
            return LeAst(left_exp,right_exp,operator,value.lineno)
        elif operator=='==':
            return CpaAst(left_exp,right_exp,operator,value.lineno)
        elif operator=='!=':
            return NeAst(left_exp,right_exp,operator,value.lineno)
        else:
            raise ValueError(f"Invalid operator:{operator}")

    @_('expr logop expr')
    def expr(self,value):
        left_exp=value[0]
        operator=value[1]
        right_exp=value[2]

        if operator=='&&':
            return LAndAst(left_exp,right_exp,operator,value.lineno)
        elif operator=='||':
            return LOrAst(left_exp,right_exp,operator,value.lineno)
        else:
            raise ValueError(f"Invalid operator:{operator}")

# ----------------------Arithmetic operatores-------------
    
    @_('PLUS')
    def arop(self,value):
        return '+' 
    
    @_('MINUS')
    def arop(self, value):
        return '-'

    @_('MUL')
    def arop(self, value):
        return '*'

    @_('DIV')
    def arop(self, value):
        return '/'

    @_('MOD')
    def arop(self, value):
        return '%'

    
    # ----------------------Relational operators------------------------
    
    @_('GT')
    def relop(self,value):
        return '>'
    
    @_('LT')
    def relop(self, value):
        return '<'

    @_('GE')
    def relop(self, value):
        return '>='

    @_('LE')
    def relop(self, value):
        return '<='

    @_('EQ')
    def relop(self, value):
        return '=='

    @_('NE')
    def relop(self, value):
        return '!='    

# -------------------------logical operators-----------------

    @_('LAND')
    def logop(self, value):
        return '&&'

    @_('LOR')
    def logop(self, value):
        return '||'
    
# ---------------------------unaryoperators--------------------
    @_('unaryop expr')
    def expr(self,value):
        un_operator=value[0]
        operand=value[1]
        if un_operator=="+":
            return UnaryPlusAst(un_operator,operand,value.lineno)
        elif un_operator=="-":
            return UnaryMinus(un_operator,operand,value.lineno)
        elif un_operator=="!":
            return Lnot(un_operator,operand,value.lineno)
        else:
            raise ValueError(f"Invalid unary operator:{un_operator}")

    @_(' "(" expr ")" ')
    def expr(self,value):
        return value.expr

    @_('UNARY_PLUS')
    def unaryop(self,value):
        return '+'

    @_('UNARY_MINUS')
    def unaryop(self,value):
        return '-'

    @_(' "(" type ")" ')
    def unaryop(self,value):
        type_keyword=value.type
        if type_keyword=='int':
            return DataType.INT
        elif type_keyword=='double':
            return DataType.DOUBLE
        else:
            raise ValueError(f"Invalid type expression:{type_keyword}")

    @_('FACT')
    def unaryop(self,value):
        return '!'

    @_('ID')
    def expr(self,value):
        return NameAst(value[0])

    @_('INT')
    def expr(self,value):
        return IntConstant(value.INT)

    @_('DOUBLE')
    def expr(self,value):
        return DoubleConstant(value.DOUBLE)


if __name__ == "__main__":
    lexer = clexer()
    parser = CParser()
    expr = """
    int main()
    {
        int a,b,c,d,e,f,g;
        g=(a + c) * b;
    }
    """
    
    # arthmetic i/ps
        # c = a+b;
        # d = a*c;
        # e = b/d;
        # f = d-a;
        # g = a%b;
    # relational i/ps
        # a=b>c;
        # b=d<e;
        # d=e>=f;
        # e=b<=g;
        # g=a==b;
        # f=g!=a;
    # logical i/ps
        # a=b&&c;
        # d=e||f;
    # unary i\ps
        #b=-d;
        #c=!a;
        #a=+c;
    # parenthses i/p
        # g=(a + c) * b;

    parser.parse(lexer.tokenize(expr))