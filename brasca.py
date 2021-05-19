import sys, math, itertools
from time import sleep
from random import randrange
import traceback

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
            self.stdin_data = sys.stdin.read()[::-1]
            for _, _ in enumerate(self.stdin_data):
                self.stdin_data, result = self.stdin_data[:-1], self.stdin_data[-1]
                self.stack.append(ord(result))
        else:
            self.stdin_data = ""

        #Has anything been printed yet?
        self.already_printed = False

        #This will store all the bracket positions
        self.while_loops = {}

        #The code and the pointer
        self.code_pointer = 0
        self.code = ""

        self.implicit_num = False
        self.implicit_top = False

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
        if not self.stack:
            return 0
        else:
            return self.stack.pop()
    
    #Pop from the bottom of the stack
    def pop_bottom(self):
        if not self.stack:
            return 0
        else:
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
        temp_strmode = False
        temp_singlequote = 0
        for position, command in enumerate(self.code):
            if temp_singlequote > 0:
                temp_singlequote -= 1
            elif temp_singlequote == 0:
                temp_strmode = False

            if command == "[" and temp_strmode == False:
                temp.append(position)
            elif command == "]" and temp_strmode == False:
                start = temp.pop()
                self.while_loops[start] = position
                self.while_loops[position] = start
            elif command == "'":
                temp_strmode = True
                temp_singlequote = 2
            elif command == "`" and temp_strmode == False:
                temp_strmode == True
            elif command == "`" and temp_strmode == True:
                temp_strmode == False


"""
System arguments:
python brasca.py f <filename>
python brasca.py c <code>

To enable debug, use fd/cd instead of f/c.
To slow down output, use fs/cs
"""
if __name__ == "__main__":
    brasca = BrascaClass()

    # Check system arguments and save the code to a variable
    if len(sys.argv) >= 3:
        if sys.argv[1] == "c" or sys.argv[1] == "cd" or sys.argv[1] == "cs" or sys.argv[1] == "cds":
            brasca.code = ' '.join(sys.argv[2:])
        elif sys.argv[1] == "f" or sys.argv[1] == "fd" or sys.argv[1] == "fs" or sys.argv[1] == "fds":
            try:
                f = open(sys.argv[2])
                brasca.code = f.readline()
            except:
                print("ERROR: Couldn't read file.")
                sys.exit()
        else:
            print("ERROR: Invalid argument.")
            sys.exit()
    elif len(sys.argv) < 3:
        print("ERROR: Not enough arguments.")
        sys.exit()

    # Build the loop map
    brasca.build_loops()

    # Main loop
    while brasca.code_pointer < len(brasca.code):
        try:
            command = brasca.code[brasca.code_pointer]
            if brasca.string_mode == False:
                
                # Push <num> to stack
                if command == "0":
                    brasca.push_number(0)
                elif command == "1":
                    brasca.push_number(1)
                elif command == "2":
                    brasca.push_number(2)
                elif command == "3":
                    brasca.push_number(3)
                elif command == "4":
                    brasca.push_number(4)
                elif command == "5":
                    brasca.push_number(5)
                elif command == "6":
                    brasca.push_number(6)
                elif command == "7":
                    brasca.push_number(7)
                elif command == "8":
                    brasca.push_number(8)
                elif command == "9":
                    brasca.push_number(9)
                elif command == "l":
                    brasca.push_number(10)
                elif command == "L":
                    brasca.push_number(13)
                elif command == "e":
                    brasca.push_number(26)
                elif command == "E":
                    brasca.push_number(32)
                elif command == "d":
                    brasca.push_number(48)
                elif command == "D":
                    brasca.push_number(65)
                elif command == "h":
                    brasca.push_number(97)
                elif command == "H":
                    brasca.push_number(100)
                elif command == "K":
                    brasca.push_number(1000)
                elif command == "{": #Decrement
                    brasca.push_number(brasca.pop()-1)
                elif command == "}": #Increment
                    brasca.push_number(brasca.pop()+1)
                elif command == "r": #Push Range
                    a = brasca.pop()
                    b = brasca.pop()
                    for i in range(b, a+1):
                        brasca.push_number(i)

                #Push strings/char
                elif command == '`':
                    brasca.string_mode = True
                elif command == "'":
                    brasca.push_char(brasca.code[brasca.code_pointer+1])
                    brasca.code_pointer += 1

                #Math operators
                elif command == "+": #Add
                    a = brasca.pop()
                    b = brasca.pop()
                    brasca.push_number(b+a)
                elif command == "-": #Subtract
                    a = brasca.pop()
                    b = brasca.pop()
                    brasca.push_number(b-a)
                elif command == "*": #Multiply
                    a = brasca.pop()
                    b = brasca.pop()
                    brasca.push_number(b*a)
                elif command == "/": #Integer division
                    a = brasca.pop()
                    b = brasca.pop()
                    brasca.push_number(b//a)
                elif command == "%": #Modulo
                    a = brasca.pop()
                    b = brasca.pop()
                    brasca.push_number(b%a)
                elif command == "^": #Exponent
                    a = brasca.pop()
                    b = brasca.pop()
                    brasca.push_number(b**a)
                elif command == "s": #Sqrt
                    a = brasca.pop()
                    brasca.push_number(math.floor(math.sqrt(a)))

                #Bitwise operators
                elif command == "~": #NOT
                    a = brasca.pop()
                    brasca.push_number(~a)
                elif command == "&": #AND
                    a = brasca.pop()
                    b = brasca.pop()
                    brasca.push_number(b&a)
                elif command == "|": #OR
                    a = brasca.pop()
                    b = brasca.pop()
                    brasca.push_number(b|a)
                elif command == "_": #XOR
                    a = brasca.pop()
                    b = brasca.pop()
                    brasca.push_number(b^a)


                #Stack
                elif command == "a": #push to register A
                    brasca.set_register("a")
                elif command == "b": #push to register B
                    brasca.set_register("b")
                elif command == "A": #pop from register A
                    brasca.read_register("a")
                elif command == "B": #pop from register B
                    brasca.read_register("b")
                elif command == ",": #reverse stack
                    brasca.reverse()
                elif command == ":": #duplicate top of stack
                    a = brasca.pop()
                    brasca.push_number(a)
                    brasca.push_number(a)
                elif command == ";": #duplicate bottom of stack
                    a = brasca.pop_bottom()
                    brasca.push_number_bottom(a)
                    brasca.push_number_bottom(a)
                elif command == "m": #move top of stack to bottom
                    value = brasca.pop()
                    brasca.push_number_bottom(value)
                elif command == "M": #move bottom of stack to top
                    value = brasca.pop_bottom()
                    brasca.push_number(value)
                elif command == "p": #move top of stack to bottom n times
                    amount = brasca.pop()
                    for n in range(0,amount):
                        value = brasca.pop()
                        brasca.push_number_bottom(value)
                elif command == "P": #move bottom of stack to top n times
                    amount = brasca.pop()
                    for n in range(0,amount):
                        value = brasca.pop_bottom()
                        brasca.push_number(value)
                elif command == "?": #random number 0-127
                    brasca.push_number(randrange(int(brasca.pop()+1)))
                elif command == "!": #push length of stack
                    brasca.push_number(brasca.length())
                elif command == "$": #swap top two items on stack
                    a = brasca.pop()
                    b = brasca.pop()
                    brasca.push_number(a)
                    brasca.push_number(b)
                elif command == "R": #rotate top three items on stack
                    a = brasca.pop()
                    b = brasca.pop()
                    c = brasca.pop()
                    brasca.push_number(a)
                    brasca.push_number(c)
                    brasca.push_number(b)
                    
                elif command == "S": #concatenate top two numbers
                    a = brasca.pop()
                    b = brasca.pop()
                    brasca.push_number(int(str(b)+str(a)))
                elif command == "g": #concatenate stack
                    temp = int(''.join(str(n) for n in brasca.stack))
                    for counter in range(0,len(brasca.stack)):
                        brasca.pop()
                    brasca.push_number(temp)
                elif command == "G": #concatenate stack and split
                    #`1.23.45` '. i G => 1 23 45
                    delim = brasca.pop()
                    spl = [list(y) for x, y in itertools.groupby(brasca.stack, lambda z: z == delim) if not x]
                    for counter in range(0,len(brasca.stack)):
                        brasca.pop()
                    for x in spl:
                        temp = int(''.join(str(y) for y in x))
                        brasca.push_number(temp)
                elif command == "i": #convert ascii to number (-48)
                    for count, value in enumerate(brasca.stack):
                        if value >= 48 and value <= 57:
                            brasca.stack[count] = value-48
                elif command == "I": #convert number to ascii (+48)
                    for count, value in enumerate(brasca.stack):
                        if value >= 0 and value <= 9:
                            brasca.stack[count] = value+48

                elif command == "x": #discard top of stack
                    brasca.pop()
                elif command == "X": #discard bottom of stack
                    brasca.pop_bottom()
                elif command == "u": #Un-S
                    n = brasca.pop()
                    for d in str(n):
                        brasca.push_number(int(d))
                elif command == "U": #Un-g
                    n = ''.join(str(x) for x in brasca.stack)
                    brasca.stack = []
                    for d in str(n):
                        brasca.push_number(int(d))


                #I/O

                elif command == "o": #Output as ASCII from top of stack
                    if brasca.already_printed == False:
                        brasca.already_printed = True
                    print(chr(brasca.pop()), end='')
                elif command == "O": #Output as ASCII from bottom of stack
                    if brasca.already_printed == False:
                        brasca.already_printed = True
                    print(chr(brasca.pop_bottom()), end='')
                elif command == "n": #Output as number from top of stack
                    if brasca.already_printed == False:
                        brasca.already_printed = True
                    print(brasca.pop(), end='')
                elif command == "N": #Output as number from bottom of stack
                    if brasca.already_printed == False:
                        brasca.already_printed = True
                    print(brasca.pop_bottom(), end='')


                #Control Flow
                elif command == "<": #Less than
                    a = brasca.pop()
                    b = brasca.pop()
                    if b<a:
                        brasca.push_number(1)
                    else:
                        brasca.push_number(0)
                elif command == ">": #Greater than
                    a = brasca.pop()
                    b = brasca.pop()
                    if b>a:
                        brasca.push_number(1)
                    else:
                        brasca.push_number(0)
                elif command == "=": #Equals
                    a = brasca.pop()
                    b = brasca.pop()
                    if b==a:
                        brasca.push_number(1)
                    else:
                        brasca.push_number(0)
                elif command == 'Y': #Between
                    a = brasca.pop()
                    b = brasca.pop()
                    c = brasca.pop()
                    if b <= c <= a:
                        brasca.push_number(1)
                    else:
                        brasca.push_number(0)
                elif command == "@": #Terminate
                    brasca.already_printed = True
                    sys.exit()
                elif command == "#": #Conditional jump
                    if brasca.pop() <= 0:
                        brasca.code_pointer += 1
                elif command == "j": #Jump forwards
                    brasca.code_pointer += brasca.pop()-1
                elif command == "J": #Jump backwards
                    brasca.code_pointer -= brasca.pop()+1
                elif command == "[": #While-loop start
                    if brasca.stack != []:
                        if brasca.stack[-1] <= 0:
                            brasca.code_pointer = brasca.while_loops[brasca.code_pointer]
                elif command == "]": #While-loop end
                    if brasca.stack != []:
                        if brasca.stack[-1] > 0:
                            brasca.code_pointer = brasca.while_loops[brasca.code_pointer]-1
                elif command == "C":
                    brasca.implicit_num = True
                elif command == "T":
                    brasca.implicit_top = True

            #If the interpreter is reading as a string
            elif brasca.string_mode == True:
                #Turn it off when another backtick is found
                if command == '`':
                    brasca.string_mode = False
                #Otherwise push it
                else:
                    brasca.push_char(command)

            #If debug mode is on, print the stack and registers after every command
            if sys.argv[1] == "cd" or sys.argv[1] == "fd":
                print(command + " | " + str(brasca.string_mode) + " | " + str(brasca.a) + " | " + str(brasca.b) +" | " + str(brasca.stack))
            elif sys.argv[1] == "cs" or sys.argv[1] == "fs":
                sleep(0.1)
            elif sys.argv[1] == "cds" or sys.argv[1] == "fds":
                print(command + " | " + str(brasca.string_mode) + " | " + str(brasca.a) + " | " + str(brasca.b) +" | " + str(brasca.stack))
                sleep(0.3)

            #Move the code pointer
            brasca.code_pointer += 1
        except KeyboardInterrupt:
            sys.exit()
        except Exception as e:
            #Something went wrong, throw an error
            print("ERROR: Something went wrong")
            print(traceback.format_exc())
            sys.exit()

    #Implicit output
    if brasca.already_printed == False:
        if brasca.implicit_top is False:
            brasca.reverse()
            for counter in range(0,len(brasca.stack)):
                a=brasca.pop()
                if brasca.implicit_num is False:
                    print(chr(a), end='')
                elif brasca.implicit_num is True:
                    print(a, end='')
        elif brasca.implicit_top is True:
            a=brasca.pop()
            if brasca.implicit_num is False:
                print(chr(a), end='')
            elif brasca.implicit_num is True:
                print(a, end='')
            