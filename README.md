# BRASCA

**BRASCA - BRAckets and other Symbols turning Code into Ascii**

`i tried my best with the acronym, okay`

## Data

* Stack by default, some commands can treat it like a queue if needed.
* Two registers: A and B.

## Commands

* TOS means Top Of Stack
* BOS means Bottom Of Stack
* Everything that isn't a command is a no-op.
* Implicit output - If nothing is printed before termination, output the stack in reverse as ASCII.

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
|`"`|Push all following symbols to the stack until another \" or EOF|
|`'`|Push the next symbol to the stack|
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
|`~`|Pop A from the stack, push NOT A to the stack
|`&`|Pop A,B from the stack, push B AND A to the stack
|`\|`|Pop A,B from the stack, push B OR A to the stack
|`_`|Pop A,B from the stack, push B XOR A to the stack

### Stack

|Operator|Function|
|-------|-------|
|`a`|Pop the stack, push it to register A|
|`A`|Pop register A, push it to the stack|
|`b`|Pop the stack, push it to register B|
|`B`|Pop register B, push it to the stack|
|`,`|Reverse stack|
|`:`|Duplicate TOS|
|`;`|Duplicate BOS|
|`m`|Pop n from TOS and push the top n items on the stack to BOS|
|`M`|Pop n from BOS and push the bottom n items on the stack to TOS|
|`?`|Push a random number from 0 to 127 to the stack|
|`!`|Push the length of the stack to the stack|
|`$`|Swap the top two items on the stack|
|`S`|Pop A,B from the stack, concatenate B and A, push the result to stack|
|`x`|Pop TOS and discard it|
|`X`|Pop BOS and discard it|

### I/O

|Operator|Function|
|-------|-------|
|`i`|input from STDIN to TOS|
|`I`|input from STDIN to BOS|
|`o`|output from TOS to STDOUT as ASCII|
|`O`|output from BOS to STDOUT as ASCII|
|`n`|output from TOS to STDOUT as number|
|`N`|output from BOS to STDOUT as number|

### Control Flow

|Operator|Function|
|-------|-------|
|`<`|Pop A,B from the stack, push 1 to the stack if B < A, else push 0 to the stack|
|`>`|Pop A,B from the stack, push 1 to the stack if B > A, else push 0 to the stack|
|`=`|Pop A,B from the stack, push 1 to the stack if B == A, else push 0 to the stack|
|`@`|Terminate program without implicit output.|
|`{...}`    |Pop n from the stack, repeat the code inside {} n times, then continue on|
|`(...#...)`|Pop A from the stack, if A > 0, execute everything up to the #, then jump to ) and continue on, else jump to # and continue on|
|`[...]`    |Pop A from the stack, if A > 0 execute the code inside \[\], then jump back to the \[ and repeat, else jump to \] and continue on|
|`j`|Pop n from the stack, move the code pointer n cells backwards|
|`J`|Pop n from the stack, move the code pointer n cells forwards|
