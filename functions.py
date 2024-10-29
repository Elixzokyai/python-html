def functionNae():
    pass

functionNae()

# a function with parameters(a, b)
def function_with_params(a,b):
    print(a)


function_with_params(functionNae(), b=2) #2, 2, are called arguments



def outer_function(text):
    def inner_function():
        return text
    return inner_function()

closure_func = outer_function('Hello class , from closure')
print(closure_func)
