from sly import Parser
from lexer1 import clexer
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
<assignment_stmt> :=  <identifier> = <identifier>  |  <identifier> = <constant>
<print_stmt>            :=  print <identifier>

'''

class CParser(Parser):
    literals=clexer.literals
    tokens = clexer.tokens
    stable=SymbolTable()
    # precedence=(('left','-','+'),('right','*','/'))
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
        return [value.ID] + value.list_of_variables

    @_('ID')
    def list_of_variables(self, value):
        return [value[0]]

     @_('ID "=" ID ')
    def assignment_stmt(self, value):
        left_variable = self.stable.getSymbolEntry(value[0])
        right_variable = self.stable.getSymbolEntry(value[2])
        assignment_ast = AssignAst(NameAst(left_variable), NameAst(right_variable), lineNo=0)
        return assignment_ast

    @_('ID "=" INTEGER')
    def assignment_stmt(self, value):
        left_variable = self.stable.getSymbolEntry(value[0])
        value_variable = value[2]
        assignment_ast = AssignAst(NameAst(left_variable), NumberAst(value_variable), lineNo=0)
        return assignment_ast

    @_('PRINT ID')
    def print_stmt(self, value):
        keyword = value[0]
        variable_name = self.stable.getSymbolEntry(value[1])
        
            # print_ast = PrintAst(variable_name)
            # print_ast=SymbolTable.getSymbolEntry(variable_name)
        return PrintAst(NameAst(variable_name))

    @_('INT')
    def type(self, value):
        keyword = value[0]
        return keyword

    @_('INTEGER')
    def statement(self, value):
        value_variable = int(value[0])
        assignment_ast = AssignAst(NumberAst(value_variable), None, lineNo=0)
        return assignment_ast

if __name__ == "__main__":
    lexer = clexer()
    parser = CParser()
    expr = """
    int main()
    {
        int a,b,c,d;
        a = 30;
        b = 20;
        c = 10;
        d = a ;
        print a;
        print d;
    }
    """
    parser.parse(lexer.tokenize(expr))
    # result.print()
    # main_function = result.getMainFunction
    # main_function.setStatementsAstList(result.functions['main'].statementsAstList)
    # main_function.print()
