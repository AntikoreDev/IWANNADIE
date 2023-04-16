#!/usr/bin/env python3

import sys, os, random, math, time

"""
IWANNADIE Language Interpreter v2
I already know this is by far the worst interpreter for a language in the world
                                                               - Antikore, 2021
Created in 3 days (originally)
Made using Python 3.9.5
"""

program = None

# Main initialization
def run():
	global program

	arg = sys.argv[1] if len(sys.argv) > 1 else None

	if (arg != None):
		try:
			f = open(arg, mode = "r", encoding = "utf-8")
		except:
			print("Error: Cannot read file '" + arg + "' because this doesn't exist or couldn't be opened")
			return
		
		lines = f.read().splitlines()
		f.close()

		program = Interpeter(arg, lines)
	else:
		program = Interpeter(None, [])

# Run the program
class Interpeter():
	lines = []
	file = None
	ln = 0
	symbols = {}
	tags = {}
	lambdas = {}
	multiline_comment = False

	def __init__(self, f, lines):
		global program

		self.lines = lines
		self.file = f
		self.ln = 0
		
		program = self

		try:

			# Search for tags if there is a file
			if (self.file != None):
				while self.ln < len(self.lines):
					self.run(True)
					self.ln += 1
				self.ln = 0

			while True:
				if (self.file == None):
					if (len(self.lines) <= self.ln):
						command = input("> ").splitlines()
						for c in command:
							self.lines.append(c)
					self.run()
				else:
					self.run()
				self.ln += 1
		except KeyboardInterrupt:
			pass
		except IndexError:
			print("Error: Script must be killed after terminating the program")
			print("At end of file: " + self.lines[len(self.lines) - 1])
		except IWCrashHandler as e:
			print(e.__str__())
		finally:
			sys.exit(0)

	def run(self, searchMarks = False):
		line = self.lines[self.ln]
		if (line.startswith("-[")):
			if (not line.endswith("]-")):
				self.multiline_comment = True
		elif (line.endswith("]-") and self.multiline_comment):
			self.multiline_comment = False
		elif (line.startswith("@")):
			self.tags.update({ line[1:]: self.ln })
		elif (not (searchMarks or self.multiline_comment)):
			cmd = Command(line)
			cmd.run()
		
# This is a class that belongs to data of a command.
class Command():
	name = ""
	args = []
	def __init__(self, line):
		parsed = self.parse(line.strip())

		self.name = parsed[0]
		self.args = parsed[1]

	def parsesymbol(self, symbol):
		s = symbol.getvalue()
		if (isinstance(s, Symbol)):
			v = s.get()
			return v
		return s

	def tostring(self, v):
		if (isinstance(v, bool)):
			return "true" if v else "false"
		elif (v == None):
			return "null"
		else:
			return v

	def run(self):
		global program
		
		try:
			if (self.name == "print"):
				print(self.tostring(self.parsesymbol(self.args[0])))
			if (self.name == "input"):
				return input(self.args[0].getvalue())
			if (self.name == "set"):
				self.args[0].getvalue().set(self.parsesymbol(self.args[1]))
			if (self.name == "add"):
				arg0 = self.args[0].getvalue()
				arg1 = self.parsesymbol(self.args[1])
				if (arg1 != 0):
					if (isinstance(arg0, Symbol)):
						op = arg0.get() + arg1
						arg0.set(op)
						return op
					else:
						return arg0 + arg1
				else:
					if (isinstance(arg0, Symbol)):
						return arg0.get()
					else:
						return arg0
			if (self.name == "mul"):
				arg0 = self.args[0].getvalue()
				if (isinstance(arg0, Symbol)):
					op = arg0.get() * self.parsesymbol(self.args[1])
					arg0.set(op)
					return op
				else:
					return arg0 * self.parsesymbol(self.args[1])
			if (self.name == "div"):
				arg0 = self.args[0].getvalue()
				if (isinstance(arg0, Symbol)):
					op = arg0.get() / self.parsesymbol(self.args[1])
					arg0.set(op)
					return op
				else:
					return arg0 / self.parsesymbol(self.args[1])
			if (self.name == "mod"):
				arg0 = self.args[0].getvalue()
				if (isinstance(arg0, Symbol)):
					op = arg0.get() % self.parsesymbol(self.args[1])
					arg0.set(op)
					return op
				else:
					return arg0 % self.parsesymbol(self.args[1])
			if (self.name == "time"):
				return time.time()
			if (self.name == "die"):
				sys.exit(0)
			if (self.name == "int"):
				return int(self.parsesymbol(self.args[0]))
			if (self.name == "real"):
				return float(self.parsesymbol(self.args[0]))
			if (self.name == "floor"):
				return math.floor(self.parsesymbol(self.args[0]))
			if (self.name == "round"):
				return round(self.parsesymbol(self.args[0]))
			if (self.name == "text"):
				return (str(self.parsesymbol(self.args[0])) + str(self.parsesymbol(self.args[1])))
			if (self.name == "check"):
				return (self.parsesymbol(self.args[0]) == self.parsesymbol(self.args[1]))
			if (self.name == "not"):
				return not self.parsesymbol(self.args[0])
			if (self.name == "or"):
				return self.parsesymbol(self.args[0]) or self.parsesymbol(self.args[1])
			if (self.name == "and"):
				return self.parsesymbol(self.args[0]) and self.parsesymbol(self.args[1])
			if (self.name in ["comp", "compare"]):
				return (self.parsesymbol(self.args[0]) > self.parsesymbol(self.args[1]))
			if (self.name == "goto"):
				program.ln = program.tags.get(self.parsesymbol(self.args[0]))
			if (self.name == "goif"):
				if (self.parsesymbol(self.args[1])):
					program.ln = program.tags.get(self.parsesymbol(self.args[0]))
			if (self.name == "doif"):
				if (not self.parsesymbol(self.args[0])):
					program.ln += 1
			if (self.name in ["char", "at"]):
				try:
					string = self.parsesymbol(self.args[0])
					return string[self.parsesymbol(self.args[1])]
				except:
					raise IWCrashHandler(program.lines[program.ln], program.ln + 1, "Cannot read index char from value")
			if (self.name in ["lambda", "fn"]):
				program.lambdas.update({ self.parsesymbol(self.args[0]): self.args[1] })
			if (self.name == "run"):
				i = 0
				for _ in self.args:
					if (i > 0):
						program.symbols.update({ "arg" + str(i - 1): self.parsesymbol(self.args[i]) })
					i += 1
				return program.lambdas.get(self.parsesymbol(self.args[0])).getvalue()
			if (self.name == "random"):
				return random.uniform(self.parsesymbol(self.args[0]), self.parsesymbol(self.args[1]))
			if (self.name == "len"):
				try:
					return len(self.parsesymbol(self.args[0]))
				except TypeError:
					raise IWCrashHandler(program.lines[program.ln], program.ln + 1, "Cannot get length from " + self.args[0])
			if (self.name == "clear"):
				os.system('clear' if os.name == 'posix' else 'cls')
			if (self.name.startswith("!")):
				i = 0
				for _ in self.args:
					program.symbols.update({ "arg" + str(i): self.parsesymbol(self.args[i]) })
					i += 1
				return program.lambdas.get(self.name[1:]).getvalue()

			return None
		except ZeroDivisionError as e:
			raise IWCrashHandler(program.lines[program.ln], program.ln + 1, "Cannot divide by zero")
		except Exception as e:
			if (isinstance(e, IWCrashHandler)):
				raise e
			raise IWCrashHandler(program.lines[program.ln], program.ln + 1, "Unknown error trying to execute '" + self.name + "' command")
	
	def parse(self, line):
		string = False
		cmdarg = 0
		escape = False
		name = ""
		arg = ""
		args = []

		for c in line:
			if (arg.endswith("--") and not string):
				arg = arg.rstrip("--")
				break

			if (name == ""):
				if (c == " "):
					name = arg
					arg = ""
				else:
					arg += c
			else:
				if (string):
					if (not escape):
						if (c == "\\"):
							escape = True
						elif (c == "\""):
							string = False
							arg += c
						else:
							arg += c
					else:
						escape = False
						if (c == "n"):
							arg += "\n"
						elif (c == "r"):
							arg += "\r"
						elif (c == "t"):
							arg += "\t"	
						else:
							arg += c
				else:
					if (cmdarg > 0):
						if (c == "["):
							cmdarg += 1
							arg += c
						elif (c == "]"):
							cmdarg -= 1
							if (cmdarg == 0):
								arg = "[" + arg + "]"
							else:
								arg += c
						else:
							arg += c
					else:
						if (c != " "):
							if (c == ","):
								args.append(Item(arg))
								arg = ""
							elif (c == "["):
								cmdarg += 1
							elif (c == "]"):
								cmdarg -= 1
							elif (c == "\""):
								arg += c
								string = True
							else:
								arg += c
		if (arg != ""):
			if (name != ""):
				args.append(Item(arg))
			else:
				name = arg
	
		return name, args

class Item():
	value = 0

	def __init__(self, v):
		self.value = v

	def getvalue(self):
		global program
		try:
			if (self.value.startswith("#")):
				return Symbol(self.value[1:])
			if (self.value.startswith("[") and self.value.endswith("]")):
				try:
					return Command(self.value[1:][:-1]).run()
				except IWCrashHandler as e:
					raise e
			if (self.value.startswith("\"") and self.value.endswith("\"")):
				return self.value[1:][:-1]
			elif (self.value == "true"):
				return True
			elif (self.value == "false"):
				return False
			elif (self.value == "null"):
				return None
			else:
				return float(self.value)
		except Exception as e:
			if (isinstance(e, IWCrashHandler)):
				raise e
			raise IWCrashHandler(program.lines[program.ln], program.ln + 1, "Cannot understand or parse expression '" + self.value + "'")
	

class Symbol():
	name = ""

	def __init__(self, name):
		self.name = name
	
	def get(self):
		global program
		return program.symbols.get(self.name)
	
	def set(self, v):
		global program
		program.symbols.update({ self.name: v })
		return program.symbols.get(self.name)

class Error():
	def __init__(self, line, ln, message):
		self.line = line
		self.ln = ln
		self.message = message
		
		print("Error: " + message)
		print("At line " + str(ln) + ": " + line)

# IWCrashHandler
class IWCrashHandler(Exception):
	def __init__(self, line, ln, message):
		self.line = line
		self.ln = ln
		self.message = message

	def __str__(self) -> str:
		return "Error: " + self.message + "\nAt line " + str(self.ln) + ": " + self.line

# Run the program
if (__name__ == "__main__"):
	run()