import sys, getch, math
from brasca_class import BrascaClass


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

                #Push strings/char
                elif command == '`':
                    brasca.string_mode = True
                elif command == "'":
                    brasca.push_char(brasca.code[brasca.code_pointer+1])
                    brasca.code_pointer += 1

                #Math operators
                elif command == "+":
                    a = brasca.pop()
                    b = brasca.pop()
                    brasca.push_number(b+a)
                elif command == "-":
                    a = brasca.pop()
                    b = brasca.pop()
                    brasca.push_number(b-a)
                elif command == "*":
                    a = brasca.pop()
                    b = brasca.pop()
                    brasca.push_number(b*a)
                elif command == "/":
                    a = brasca.pop()
                    b = brasca.pop()
                    brasca.push_number(b//a)
                elif command == "%":
                    a = brasca.pop()
                    b = brasca.pop()
                    brasca.push_number(b%a)
                elif command == "^":
                    a = brasca.pop()
                    b = brasca.pop()
                    brasca.push_number(b**a)
                elif command == "s":
                    a = brasca.pop()
                    brasca.push_number(math.floor(math.sqrt(a)))

                #Bitwise operators
                elif command == "~":
                    a = brasca.pop()
                    brasca.push_number(~a)
                elif command == "&":
                    a = brasca.pop()
                    b = brasca.pop()
                    brasca.push_number(b&a)
                elif command == "|":
                    a = brasca.pop()
                    b = brasca.pop()
                    brasca.push_number(b|a)
                elif command == "_":
                    a = brasca.pop()
                    b = brasca.pop()
                    brasca.push_number(b^a)


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
            