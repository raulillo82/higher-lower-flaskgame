#inputs = eval(input())

def logging_decorator(function):
    def wrapper(*args):
      print(f"You called: {function.__name__}{args}")
      print(f"It returned: {function(args[0], args[1], args[2])}")
    return wrapper

@logging_decorator
def a_function(a, b, c):
    return a * b * c

#a_function(inputs[0], inputs[1], inputs[2])
a_function(1, 2, 3)
