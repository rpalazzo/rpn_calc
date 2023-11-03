# RPN Calc
Runs a Reverse Polish Notation (RPN) calculator from your terminal.

Enter the numbers to operate on separately, then enter the operator.
The operands are replaced with the result at the bottom of the stack.

## Supports the following operators
- "+" for addition
- "-" for subtraction 
- "*" for multiplication
- "/" for division
- "exp" for exponents (the 2nd oldest number raised the the latest number)
- "inv" for the inverse - 1/N
- "swp" for swapping the latest 2 values
- "clr" to clear the entire stack
- "drp" to drop the latest number

Press *Enter* without a value to exit.

## Implementation Features
- Uses dictionary for the operator functions
- Test cases in pytest