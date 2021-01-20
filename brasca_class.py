import sys

class BrascaClass:
    """Stack, registers and variables"""
    def __init__(self):

        #Stack and registers
        self.stack = []
        self.a = 0
        self.b = 0
        
        #Are we reading everything as characters?
        self.string_mode = False

        #Piped-in data
        if not sys.stdin.isatty():
            self.stdin_data = sys.stdin.readline()[::-1]
        else:
            self.stdin_data = ""

        #Has anything been printed yet?
        self.already_printed = False

        #This will store all the bracket positions
        self.while_loops = {}

        #The code and the pointer
        self.code_pointer = 0
        self.code = ""

    #Push number to the stack
    def push_number(self, num):
        self.stack.append(num)

    #Push value of character to stack
    def push_char(self, char):
        self.stack.append(ord(char))

    #Push number to the bottom of the stack
    def push_number_bottom(self, num):
        self.stack.insert(0, num)

    #Push value of character to the bottom of the stack
    def push_char_bottom(self, char):
        self.stack.insert(0, ord(char))

    #Pop from stack
    def pop(self):
        return self.stack.pop()
    
    #Pop from the bottom of the stack
    def pop_bottom(self):
        return self.stack.pop(0)

    #Set the register
    def set_register(self, register):
        if register == "a":
            self.a = self.pop()
        elif register == "b":
            self.b = self.pop()
    
    #Push the register's value to the stack
    def read_register(self, register):
        if register == "a":
            self.stack.append(self.a)
            self.a = 0
        elif register == "b":
            self.stack.append(self.b)
            self.b = 0

    #Reverse the stack
    def reverse(self):
        self.stack.reverse()

    #Return the length of the stack
    def length(self):
        return len(self.stack)

    #Populate the while loop list (self.while_loops)
    def build_loops(self):
        temp = []
        for position, command in enumerate(self.code):
            if command == "[":
                temp.append(position)
            elif command == "]":
                start = temp.pop()
                self.while_loops[start] = position
                self.while_loops[position] = start
