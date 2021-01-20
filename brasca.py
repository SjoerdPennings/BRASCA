import sys, getch

class BrascaClass:
    """Stack, registers and variables"""
    def __init__(self):

        #Stack and registers
        self.stack = []
        self.a = 0
        self.b = 0
        
        #Are we reading everything as characters?
        self.string_mode = False

        #Has anything been printed yet?
        self.already_printed = False

        #This will store all the bracket positions
        self.while_loops = {}

        #The code and the pointer
        self.code_pointer = 0
        self.code = ""

    #Toggle the string mode
    def toggle_string_mode(self):
        self.string_mode = not self.string_mode

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

"""
System arguments:
python brasca.py f <filename>
python brasca.py c <code>

To enable debug, use fd/cd instead of f/c.
"""
if __name__ == "__main__":
    brasca = BrascaClass()

    # Check system arguments and save the code to a variable
    if len(sys.argv) >= 3:
        if sys.argv[1] == "c" or sys.argv[1] == "cd":
            brasca.code = sys.argv[2]
        elif sys.argv[1] == "f" or sys.argv[1] == "fd":
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
    
    # If there's no code, do nothing and close.
    if len(brasca.code) <= 0:
        sys.exit()

    # Main loop
    while brasca.code_pointer < len(brasca.code):
        try:
            command = brasca.code[brasca.code_pointer]

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

            #Push number shortcuts
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


            #If debug mode is on, print the stack and registers after every command
            if sys.argv[1] == "cd" or sys.argv[1] == "fd":
                print(str(brasca.a) + " | " + str(brasca.b) +" | " + str(brasca.stack))

            #Move the code pointer
            brasca.code_pointer += 1

        except:
            #Something went wrong, throw an error
            print("ERROR: Something went wrong")

    #Implicit output
    if brasca.already_printed == False:
        brasca.reverse()
        for counter in range(0,len(brasca.stack)):
            print(chr(brasca.pop()), end='')
            