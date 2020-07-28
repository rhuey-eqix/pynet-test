''' simple math functions to demonstrate unit testing'''

def func1(x, y):
    return x + y


def func2(x,y):
    return x*y


list = [10, 11]

return_val1 = func1(*list)
return_val2 = func2(*list)

print(return_val1)
print(return_val2)

