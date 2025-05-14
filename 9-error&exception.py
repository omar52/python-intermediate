# Errors and Exceptions
# A Python program terminates as soon as it encounters an error. In Python, an error can be a syntax error or an exception. In this article we will have a look at:
# 1- Syntax Error vs. Exception
# 2- How to raise Exceptions
# 3- How to handle Exceptions
# 4- Most common built-in Exceptions
# 5- How to define your own Exception

# 1-Syntax Errors
# A Syntax Error occurs when the parser detects a syntactically incorrect statement. A syntax error can be for example a typo, missing brackets, no new line (see code below), 
# or wrong identation (this will actually raise its own IndentationError, but its subclassed from a SyntaxError).

# 2- Exceptions
# Even if a statement is syntactically correct, it may cause an error when it is executed. This is called an Exception Error. There are several different error classes, 
# for example trying to add a number and a string will raise a TypeError.

# 3- Raising an Exception
# If you want to force an exception to occur when a certain condition is met, you can use the raise keyword.
    # x = -5
    # if x < 0:
    #     raise Exception('x should not be negative.')

# You can also use the assert statement, which will throw an AssertionError if your assertion is not True. This way, you can actively test some conditions that have to be fulfilled instead of waiting for your program to unexpectedly crash midway. 
# Assertion is also used in unit testing.

    # x = -5
    # assert (x >= 0), 'x is not positive.'
    # # --> Your code will be fine if x >= 0


# 3-Handling Exceptions

# You can use a try and except block to catch and handle exceptions. If you can catch an exceptions your program won't terminate, and can continue.
# try:
    # a = 5 / 0
    #except:
    #   print('some error occured.')   # This will catch all possible exceptions
                                       

    # except Exception as e:       # You can also catch the type of exception
    #    print(e)
    
try:
    a = 5 / 1 # Note: No ZeroDivisionError here
    b = a + '10'
except ZeroDivisionError as e:
    print('A ZeroDivisionError occured:', e)     # ZeroDivisionError is handled here
except TypeError as e:
    print('A TypeError occured:', e)             # type of exception is handled here
    

# else clause

try:
    a = 5 / 1
except ZeroDivisionError as e:
    print('A ZeroDivisionError occured:', e)
else:
    print('Everything is ok')
    
    
# finally clause
try:
    a = 5 / 1 # Note: No ZeroDivisionError here
    b = a + '10'
except ZeroDivisionError as e:
    print('A ZeroDivisionError occured:', e)
except TypeError as e:
    print('A TypeError occured:', e)
else:
    print('Everything is ok')
finally:
    print('Cleaning up some stuff...')