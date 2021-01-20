import sys, getch, math
from brasca_class import BrascaClass
from random import randrange

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
            brasca.code = ' '.join(sys.argv[2:])
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
                elif command == "m": #move top of stack to bottom n times
                    amount = brasca.pop()
                    for n in range(0,amount):
                        value = brasca.pop()
                        brasca.push_number_bottom(value)
                elif command == "M": #move bottom of stack to top n times
                    amount = brasca.pop()
                    for n in range(0,amount):
                        value = brasca.pop_bottom()
                        brasca.push_number(value)
                elif command == "?": #random number 0-127
                    brasca.push_number(randrange(128))
                elif command == "!": #push length of stack
                    brasca.push_number(brasca.length())
                elif command == "$": #swap top two items on stack
                    a = brasca.pop()
                    b = brasca.pop()
                    brasca.push_number(a)
                    brasca.push_number(b)
                elif command == "S": #concatenate top two numbers
                    a = brasca.pop()
                    b = brasca.pop()
                    brasca.push_number(int(str(b)+str(a)))
                elif command == "x": #discard top of stack
                    brasca.pop()
                elif command == "x": #discard bottom of stack
                    brasca.pop_bottom()

                #I/O


                #Control Flow

                
                elif command == "[": #While-loop start
                    if brasca.stack[-1] == 0:
                        brasca.code_pointer = brasca.while_loops[brasca.code_pointer]
                elif command == "]": #While-loop end
                    if brasca.stack[-1] != 0 and brasca.stack != []:
                        brasca.code_pointer = brasca.while_loops[brasca.code_pointer]

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

            #Move the code pointer
            brasca.code_pointer += 1

        except:
            #Something went wrong, throw an error
            print("ERROR: Something went wrong")
            sys.exit()

    #Implicit output
    if brasca.already_printed == False:
        brasca.reverse()
        for counter in range(0,len(brasca.stack)):
            a=brasca.pop()
            print(chr(a), end='')
            