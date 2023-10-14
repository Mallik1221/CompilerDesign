from enum import Enum
from abc import *
from symboltable import SymbolTable
from symboltable import SymbolTableEntry

DataType = Enum('DataType',['INT','DOUBLE'])

class AST(metaclass=ABCMeta):
	@abstractmethod
	def print(self):
		pass
	@abstractmethod
	def typeCheckAST(self):
		pass
	@abstractmethod
	def getDataType(self):
		pass

class NumberAst(AST):
	def __init__(self, number):
		self.value = number
	def print(self):
		print(f"NumberAST:{self.value})")
	def getDataType(self):
		return type(self.value)
	def typeCheckAST(self):
		data_type=self.getDataType()
		if data_type== DataType.INT or data_type==DataType.DOUBLE:
			return True
		else:
			print(f"Invalid datatype.Expected INT or DOUBLE, got {data_type}")
			return False


class NameAst(AST):
	def __init__(self, symbolEntry):
		self.symbolEntry = symbolEntry
	def print(self):
		print(f"NameAst: '{self.symbolEntry}')")

	def getDataType(self):
		return self.symbolEntry.getDataType()
	def typeCheckAST(self):
		data_typ=self.getDataType()
		if data_typ==DataType.INT or data_typ==DataType.DOUBLE:
			return True
		else:
			print(f"variable '{self.symbolEntry.getSymbolName()}' has invalid type:{data_typ}")

class AssignAst(AST):
	def __init__(self,left,right,lineNo):
		self.left = left
		self.right = right
		self.lineNo = lineNo
	def typeCheckAST(self):
		if(self.left.getDataType()== self.right.getDataType()):
			return True
		else:
			return False
	def print(self):
		print("\t\tAssign AST:")
		print("\t\t\tLHS=(",end="")
		self.left.print()
		print("\t\t\tRHS=(",end="")
		self.right.print()
	def getDataType(self):
		pass

class PrintAst(AST):
	def __init__(self,nameast):
		self.nameast= nameast
	def print(self):
		print("\t\tPrint AST:")
		print("\t\t\t(",end="")
		self.nameast.print()
	def getDataType(self):
		return None
	def typeCheckAST(self):
		return True
# ---------------------------Arthimetic Ast-----------
class AddAst(AST):
	def __init__(self,left,right,operator,lineNo):
		self.left = left
		self.right = right
		self.operator=operator
		self.lineNo = lineNo
	def typeCheckAST(self):
		if(self.left.getDataType()== self.right.getDataType()):
			return True
		else:
			return False
	def print(self):
		print("\tAddition AST:")
		print("\t\t\t\t\tLHS=( ",end="")
		self.left.print()
		print("\t\t\t\t\tOperator:(",end="")
		print(self.operator,")")
		print("\t\t\t\t\tRHS=(",end="")
		self.right.print()
	def getDataType(self):
		pass

class SubAst(AST):
	def __init__(self,left,right,operator,lineNo):
		self.left = left
		self.right = right
		self.operator=operator
		self.lineNo = lineNo
	def typeCheckAST(self):
		if(self.left.getDataType()== self.right.getDataType()):
			return True
		else:
			return False
	def print(self):
		print("\tSubtraction AST:")
		print("\t\t\t\t\tLHS=(",end="")
		self.left.print()
		print("\t\t\t\t\tOperator:(",end="")
		print(self.operator,")")
		print("\t\t\t\t\tRHS=(",end="")
		self.right.print()
	def getDataType(self):
		pass

class MulAst(AST):
	def __init__(self,left,right,operator,lineNo):
		self.left = left
		self.right = right
		self.operator=operator
		self.lineNo = lineNo
	def typeCheckAST(self):
		if(self.left.getDataType()== self.right.getDataType()):
			return True
		else:
			return False
	def print(self):
		print("\tMultiplication AST:")
		print("\t\t\t\t\tLHS=(",end="")
		self.left.print()
		print("\t\t\t\t\tOperator:(",end="")
		print(self.operator,")")
		print("\t\t\t\t\tRHS=(",end="")
		self.right.print()
	def getDataType(self):
		pass

class DivAst(AST):
	def __init__(self,left,right,operator,lineNo):
		self.left = left
		self.right = right
		self.operator=operator
		self.lineNo = lineNo
	def typeCheckAST(self):
		if(self.left.getDataType()== self.right.getDataType()):
			return True
		else:
			return False
	def print(self):
		print("\tDivision AST:")
		print("\t\t\t\t\tLHS=(",end="")
		self.left.print()
		print("\t\t\t\t\toperator:(",end="")
		print(self.operator,")")
		print("\t\t\t\t\tRHS=(",end="")
		self.right.print()
	def getDataType(self):
		pass

class PerAst(AST):
	def __init__(self,left,right,operator,lineNo):
		self.left = left
		self.right = right
		self.operator=operator
		self.lineNo = lineNo
	def typeCheckAST(self):
		if(self.left.getDataType()== self.right.getDataType()):
			return True
		else:
			return False
	def print(self):
		print("\tPer AST:")
		print("\t\t\t\t\tLHS=(",end="")
		self.left.print()
		print("\t\t\t\t\tOperator:(",end="")
		print(self.operator,")")
		print("\t\t\t\t\tRHS=(",end="")
		self.right.print()
	def getDataType(self):
		pass

# ----------------------Relational Operators--------------------------
class GrtAst(AST):
	def __init__(self,left,right,operator,lineNo):
		self.left = left
		self.right = right
		self.operator=operator
		self.lineNo = lineNo
	def typeCheckAST(self):
		if(self.left.getDataType()== self.right.getDataType()):
			return True
		else:
			return False
	def print(self):
		print("\tGreaterThan AST:")
		print("\t\t\t\t\tLHS=(",end="")
		self.left.print()
		print("\t\t\t\t\tOperator:(",end="")
		print(self.operator,")")
		print("\t\t\t\t\tRHS=(",end="")
		self.right.print()
	def getDataType(self):
		pass 

class LstAst(AST):
	def __init__(self,left,right,operator,lineNo):
		self.left = left
		self.right = right
		self.operator=operator
		self.lineNo = lineNo
	def typeCheckAST(self):
		if(self.left.getDataType()== self.right.getDataType()):
			return True
		else:
			return False
	def print(self):
		print("\tLessThan AST:")
		print("\t\t\t\t\tLHS=(",end="")
		self.left.print()
		print("\t\t\t\t\tOperator:(",end="")
		print(self.operator,")")
		print("\t\t\t\t\tRHS=(",end="")
		self.right.print()
	def getDataType(self):
		pass

class GeAst(AST):
	def __init__(self,left,right,operator,lineNo):
		self.left = left
		self.right = right
		self.operator=operator
		self.lineNo = lineNo
	def typeCheckAST(self):
		if(self.left.getDataType()== self.right.getDataType()):
			return True
		else:
			return False
	def print(self):
		print("\tGreaterThan/EqualTo AST:")
		print("\t\t\t\t\tLHS=(",end="")
		self.left.print()
		print("\t\t\t\t\tOperator:(",end="")
		print(self.operator,")")
		print("\t\t\t\t\tRHS=(",end="")
		self.right.print()
	def getDataType(self):
		pass

class LeAst(AST):
	def __init__(self,left,right,operator,lineNo):
		self.left = left
		self.right = right
		self.operator=operator
		self.lineNo = lineNo
	def typeCheckAST(self):
		if(self.left.getDataType()== self.right.getDataType()):
			return True
		else:
			return False
	def print(self):
		print("\tLessThan/EqualTo AST:")
		print("\t\t\t\t\tLHS=(",end="")
		self.left.print()
		print("\t\t\t\t\tOperator:(",end="")
		print(self.operator,")")
		print("\t\t\t\t\tRHS=(",end="")
		self.right.print()
	def getDataType(self):
		pass

class CpaAst(AST):
	def __init__(self,left,right,operator,lineNo):
		self.left = left
		self.right = right
		self.operator=operator
		self.lineNo = lineNo
	def typeCheckAST(self):
		if(self.left.getDataType()== self.right.getDataType()):
			return True
		else:
			return False
	def print(self):
		print("\tComparision AST:")
		print("\t\t\t\t\tLHS=(",end="")
		self.left.print()
		print("\t\t\t\t\tOperator:(",end="")
		print(self.operator,")")
		print("\t\t\t\t\tRHS=(",end="")
		self.right.print()
	def getDataType(self):
		pass

class NeAst(AST):
	def __init__(self,left,right,operator,lineNo):
		self.left = left
		self.right = right
		self.operator=operator
		self.lineNo = lineNo
	def typeCheckAST(self):
		if(self.left.getDataType()== self.right.getDataType()):
			return True
		else:
			return False
	def print(self):
		print("\tNotEqualTo AST:")
		print("\t\t\t\t\tLHS=(",end="")
		self.left.print()
		print("\t\t\t\t\tOperator:(",end="")
		print(self.operator,")")
		print("\t\t\t\t\tRHS=(",end="")
		self.right.print()
	def getDataType(self):
		pass
# -------------------------logical operatores------------
class LAndAst(AST):
	def __init__(self,left,right,operator,lineNo):
		self.left = left
		self.right = right
		self.operator=operator
		self.lineNo = lineNo
	def typeCheckAST(self):
		if(self.left.getDataType()== self.right.getDataType()):
			return True
		else:
			return False
	def print(self):
		print("\tLogicalAnd AST:")
		print("\t\t\t\t\tLHS=(",end="")
		self.left.print()
		print("\t\t\t\t\tOperator:(",end="")
		print(self.operator,")")
		print("\t\t\t\t\tRHS=(",end="")
		self.right.print()
	def getDataType(self):
		pass

class LOrAst(AST):
	def __init__(self,left,right,operator,lineNo):
		self.left = left
		self.right = right
		self.operator=operator
		self.lineNo = lineNo
	def typeCheckAST(self):
		if(self.left.getDataType()== self.right.getDataType()):
			return True
		else:
			return False
	def print(self):
		print("\tLogicalOR AST:")
		print("\t\t\t\t\tLHS=(",end="")
		self.left.print()
		print("\t\t\t\t\tOperator:(",end="")
		print(self.operator,")")
		print("\t\t\t\t\tRHS=(",end="")
		self.right.print()
	def getDataType(self):
		pass

# ------------------------------Unary Operators------------------------------
class UnaryPlusAst(AST):
	def __init__(self,opertor,operand,lineNo):
		self.operator=opertor
		self.operand=operand
		self.lineNo = lineNo
	def typeCheckAST(self):
		pass
	def print(self):
		print("\tUnaryPlus AST:")
		print("\t\t\t\t\tOperator:(",end="")
		print(self.operator,")")
		print("\t\t\t\t\tOperand=(",end="")
		self.operand.print()
	def getDataType(self):
		pass

class UnaryMinus(AST):
	def __init__(self,opertor,operand,lineNo):
		self.operator=opertor
		self.operand=operand
		self.lineNo = lineNo
	def typeCheckAST(self):
		pass
	def print(self):
		print("\tUnaryMinus AST:")
		print("\t\t\t\t\tOperator:(",end="")
		print(self.operator,")")
		print("\t\t\t\t\tOperand=(",end="")
		self.operand.print()
	def getDataType(self):
		pass

class Lnot(AST):
	def __init__(self,operator,operand,lineNo):
		self.operator=operator
		self.operand=operand
		self.lineNo = lineNo
	def typeCheckAST(self):
		pass
	def print(self):
		print("\tLogicalNot AST:")
		print("\t\t\t\t\tOperator:(",end="")
		print(self.operator,")")
		print("\t\t\t\t\tOperand=(",end="")
		self.operand.print()
	def getDataType(self):
		pass
