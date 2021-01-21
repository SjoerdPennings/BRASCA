# BRASCA

**BRASCA - BRAckets and other Symbols turning Code into Ascii**
`i tried my best with the acronym, okay`

## Installation & Usage

* Get [Python 3.9](http://www.python.org)
* Run your code with `python brasca.py c <your code>` or `python brasca.py f <filename>`.
* Use `python brasca.py cd/fd <code/file>` for debugging the stack.

## Data

* Stack by default, some commands can treat it like a queue if needed.
* Two registers: A and B.

## Commands

* TOS means Top Of Stack
* BOS means Bottom Of Stack
* Everything that isn't a command is a no-op.

### Math Operators

|Operator|Function|Implemented|
|-------|-------|------|
|`0-9`|Push the number to the stack|Yes|
|`l`|Push 10 to the stack|Yes|
|`L`|Push 13 to the stack|Yes|
|`e`|Push 26 to the stack|Yes|
|`E`|Push 32 to the stack|Yes|
|`d`|Push 48 to the stack|Yes|
|`D`|Push 65 to the stack|Yes|
|`h`|Push 97 to the stack|Yes|
|`H`|Push 100 to the stack|Yes|
|`K`|Push 1000 to the stack|Yes|
|`` ` ``|Push all following symbols to the stack until another backtick or EOF|Yes|
|`'`|Push the next symbol to the stack|Yes|
|`+`|Pop A,B from the stack, push B+A to the stack|Yes|
|`-`|Pop A,B from the stack, push B-A to the stack|Yes|
|`*`|Pop A,B from the stack, push B\*A to the stack|Yes|
|`/`|Pop A,B from the stack, push B\/A to the stack|Yes|
|`%`|Pop A,B from the stack, push B%A to the stack|Yes|
|`^`|Pop A,B from the stack, push B\*\*A to the stack|Yes|
|`s`|Pop A from the stack, push sqrt(A) to the stack|Yes|

### Bitwise Operators

|Operator|Function|Implemented|
|-------|-------|------|
|`~`|Pop A from the stack, push NOT A to the stack|Yes|
|`&`|Pop A,B from the stack, push B AND A to the stack|Yes|
|`\|`|Pop A,B from the stack, push B OR A to the stack|Yes|
|`_`|Pop A,B from the stack, push B XOR A to the stack|Yes|

### Stack

|Operator|Function|Implemented|
|-------|-------|------|
|`a`|Pop the stack, push it to register A|Yes|
|`A`|Pop register A, push it to the stack|Yes|
|`b`|Pop the stack, push it to register B|Yes|
|`B`|Pop register B, push it to the stack|Yes|
|`,`|Reverse stack|Yes|
|`:`|Duplicate TOS|Yes|
|`;`|Duplicate BOS|Yes|
|`m`|Pop the top of the stack and push the value to BOS|Yes|
|`M`|Pop the bottom of the stack and push the value to TOS|Yes|
|`p`|Pop n from TOS and push the top n items on the stack to BOS|Yes|
|`P`|Pop n from BOS and push the bottom n items on the stack to TOS|Yes|
|`?`|Push a random number from 0 to 127 to the stack|Yes|
|`!`|Push the length of the stack to the stack|Yes|
|`$`|Swap the top two items on the stack|Yes|
|`S`|Pop A,B from the stack, concatenate B and A, push the result to stack|Yes|
|`x`|Pop TOS and discard it|Yes|
|`X`|Pop BOS and discard it|Yes|

### I/O

|Operator|Function|Implemented|
|-------|-------|------|
|`i`|input from STDIN to TOS|Yes|
|`I`|input from STDIN to BOS|Yes|
|`o`|output from TOS to STDOUT as ASCII|Yes|
|`O`|output from BOS to STDOUT as ASCII|Yes|
|`n`|output from TOS to STDOUT as number|Yes|
|`N`|output from BOS to STDOUT as number|Yes|
|Implicit output|If nothing is printed before termination, output the stack in reverse as ASCII.|Yes|

### Control Flow

|Operator|Function|Implemented|
|-------|-------|------|
|`<`|Pop A,B from the stack, push 1 to the stack if B < A, else push 0 to the stack|Yes|
|`>`|Pop A,B from the stack, push 1 to the stack if B > A, else push 0 to the stack|Yes|
|`=`|Pop A,B from the stack, push 1 to the stack if B == A, else push 0 to the stack|Yes|
|`@`|Terminate program without implicit output.|Yes|
|`#`|Pop A from the stack, if A > 0, execute the next instruction, otherwise skip it.|Yes|
|`[...]`    |Check, but don't pop, the top of the stack. If it is non-zero execute the code inside \[\], then jump back to the \[ and repeat, else jump to \] and continue on|Yes|
|`j`|Pop n from the stack, move the code pointer n cells backwards|Yes|
|`J`|Pop n from the stack, move the code pointer n cells forwards|Yes|
