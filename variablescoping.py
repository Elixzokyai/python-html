"""
scope refers to accessibility
variable scope: accessibility or visibility of variables in different parts of the program
- Global scope : variable declared outside any functions
- local scope: variables declared withing functions i.e accessed only inside the function
- Block scope: variables are declared within a block of code
- function scope: local scopes
- lexical/Enclosing/non-local scope: a scope referenced in nested functions
- Built in scope: variables available inside of built in functions
"""

global_var = 'I am string global'

def example():
    global_var = 7
    local_var = 'I am local variable'
    print(global_var)
    print(local_var)

    example()
    print(global_var)