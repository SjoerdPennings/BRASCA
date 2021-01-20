import sys, getch

class BrascaClass:
    """Stack, registers and variables"""
    def __init__(self):
        self.stack = []
        self.a = 0
        self.b = 0
        
        self.string_mode = False

        self.while_loops = {}

        self.code_pointer = 0
        self.code = ""

    def toggle_string_mode(self):
        self.string_mode = not self.string_mode

    def push_number(self, num):
        self.stack.append(num)

    def push_char(self, char):
        self.stack.append(ord(char))

    def push_number_bottom(self, num):
        self.stack.insert(0, num)

    def push_char_bottom(self, char):
        self.stack.insert(0, ord(char))

    def pop(self):
        return self.stack.pop()
    
    def pop_bottom(self):
        return self.stack.pop(0)

    def set_register(self, register):
        if register == "a":
            self.a = self.pop()
        elif register == "b":
            self.b = self.pop()
    
    def read_register(self, register):
        if register == "a":
            return self.a
        elif register == "b":
            return self.b

    def reverse(self):
        self.stack.reverse()

    def length(self):
        return len(self.stack)

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
    if len(sys.argv) == 3:
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
    elif len(sys.argv) > 3:
        print("ERROR: Too many arguments.")
        sys.exit()

    # Build the loop map
    brasca.build_loops()
    
    if len(brasca.code) <= 0:
        sys.exit()
    # Main loop
    while brasca.code_pointer < len(brasca.code):
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

        ######DEBUG
        if sys.argv[1] == "cd" or sys.argv[1] == "fd":
            print(brasca.stack)

        brasca.code_pointer += 1