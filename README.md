# BRASCA v0.1

**BRASCA - BRAckets and other Symbols turning Code into Ascii**  
`i tried my best with the acronym, okay`

## Installation & Usage

* Get [Python 3.9](http://www.python.org)
* Run your code with `python brasca.py c <your code>` or `python brasca.py f <filename>`.
* Use `python brasca.py cd/fd <code/file>` for debugging the stack.

## Data

* Data is stored as numbers on a stack.
* Popping an empty stack returns 0.
* Two registers: A and B.

## Commands

### Math Operators

|Operator|Function|
|-------|-------|
|`0-9`|Push the number to the stack|
|`l`|Push 10 to the stack|
|`L`|Push 13 to the stack|
|`e`|Push 26 to the stack|
|`E`|Push 32 to the stack|
|`d`|Push 48 to the stack|
|`D`|Push 65 to the stack|
|`h`|Push 97 to the stack|
|`H`|Push 100 to the stack|
|`K`|Push 1000 to the stack|
|`` ` ``|Push all following characters to the stack until another backtick or EOF|
|`'`|Push the next character to the stack|
|`+`|Pop A,B from the stack, push B+A to the stack|
|`-`|Pop A,B from the stack, push B-A to the stack|
|`*`|Pop A,B from the stack, push B\*A to the stack|
|`/`|Pop A,B from the stack, push B\/A to the stack|
|`%`|Pop A,B from the stack, push B%A to the stack|
|`^`|Pop A,B from the stack, push B\*\*A to the stack|
|`s`|Pop A from the stack, push sqrt(A) to the stack|

### Bitwise Operators

|Operator|Function|
|-------|-------|
|`~`|Pop A from the stack, push NOT A to the stack|
|`&`|Pop A,B from the stack, push B AND A to the stack|
|`\|`|Pop A,B from the stack, push B OR A to the stack|
|`_`|Pop A,B from the stack, push B XOR A to the stack|

### Stack

|Operator|Function|
|-------|-------|
|`a`|Pop the stack, push it to register A|
|`A`|Pop register A, push it to the stack|
|`b`|Pop the stack, push it to register B|
|`B`|Pop register B, push it to the stack|
|`,`|Reverse stack|
|`:`|Duplicate the top of the stack|
|`;`|Duplicate the bottom of the stack|
|`m`|Pop the top of the stack and push the value to BOS|
|`M`|Pop the bottom of the stack and push the value to TOS|
|`p`|Pop n from the top of the stack and push the top n items on the stack to BOS|
|`P`|Pop n from the bottom of the stack and push the bottom n items on the stack to TOS|
|`?`|Push a random number from 0 to 127 to the stack|
|`!`|Push the length of the stack to the stack|
|`$`|Swap the top two items on the stack|
|`R`|Rotate the top three items on the stack|
|`S`|Pop A,B from the stack, concatenate B and A, push the result to stack|
|`x`|Pop the top of the stack and discard it|
|`X`|Pop the bottom of the stack and discard it|

### I/O

|Operator|Function|
|-------|-------|
|Implicit input|If there's any data piped in via STDIN, it's pushed on the stack by default|
|`o`|Output the top of the stack to STDOUT as ASCII|
|`O`|Output the bottom of the stack to STDOUT as ASCII|
|`n`|Output the top of the stack to STDOUT as a number|
|`N`|Output the bottom of the stack to STDOUT as a number|
|Implicit output|If nothing is printed before termination, output the stack in reverse as ASCII.|

### Control Flow

|Operator|Function|
|-------|-------|
|`<`|Pop A,B from the stack, push 1 to the stack if B < A, else push 0 to the stack|
|`>`|Pop A,B from the stack, push 1 to the stack if B > A, else push 0 to the stack|
|`=`|Pop A,B from the stack, push 1 to the stack if B == A, else push 0 to the stack|
|`@`|Terminate program without implicit output.|
|`#`|Pop A from the stack, if A > 0, execute the next instruction, otherwise skip it.|
|`[...]`    |Check, but don't pop, the top of the stack. While it is non-zero, loop the code inside \[ \]|
|`j`|Pop n from the stack, move the code pointer n cells backwards|
|`J`|Pop n from the stack, move the code pointer n cells forwards|
|Anything else|No-op|
