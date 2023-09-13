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
			# self.symbolEntry.print()
		# print(f"Datatype:{self.getDataType},variable:{self.symbolEntry}")
		
		print(f"NameAst: '{self.symbolEntry.getSymbolName()}')")

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
		# print("- Assignment (variable: '{0}', value: {1})".format(self.left.symbolEntry, self.right.value))
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
		# print()
		# sn=SymbolTable.getSymbolEntry(self.symbolEntry)
		# sn.print()
		# symbol_name = name_ast.getSymbolName()

		# name_ast = NameAst(self.symbolEntry)  
		# symbol_name = name_ast.symbolEntry
		# print(f"\t\t\tNameAst: '{symbol_name}'")

	def getDataType(self):
		return None
	def typeCheckAST(self):
		return True
	
