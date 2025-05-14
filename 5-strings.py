# string is orderes immutable sequence of characters

# how to write a string
# 1. single quotes
s = 'hello'
# 2. double quotes
s = "hello"
# 3. triple quotes
s = '''hello'''
s = """hello"""
# 4. raw string
s = r'hello'    
# 5. multi-line string
s = '''hello
world'''
# 6. string with escape characters
s = 'hello\nworld'
# 7. string with special characters
s = 'hello\tworld'
# 8. string with unicode characters
s = 'hello\u03A9'
# 9. string with bytes
s = b'hello'

# string reverse by slicing
s = 'hello'
s = s[::-1]

# string concatenation
s1 = 'hello'
s2 = 'world'
s = s1 + ' ' + s2
# string repetition
s = s1 * 3  

# string looping
s = 'hello'
for c in s:
    print(c)

# string membership
s = 'hello'
if 'h' in s:
    print('h is in hello')

# string length
s = 'hello'
l = len(s)


# string methods

# 1- strip method
s = '   hello   '
s1 = s.strip()  # removes leading and trailing whitespace
s2 = s.lstrip()  # removes leading whitespace
s3 = s.rstrip()  # removes trailing whitespace
print(s1,s2,s3)

# 2- split method
s = 'hello world'
s1 = s.split()  # splits the string into a list of words
s2 = s.split('o')  # splits the string into a list of words using 'o' as a separator
print(s1,s2)

# 3- join method
s = ['hello', 'world']
s1 = ' '.join(s)  # joins the list of words into a string using ' ' as a separator
s2 = '-'.join(s)  # joins the list of words into a string using '-' as a separator  
print(s1,s2)

# 4- find method
s = 'hello world'
s1 = s.find('o')  # returns the index of the first occurrence of 'o'
s2 = s.find('o', 5)  # returns the index of the first occurrence of 'o' after index 5
s3 = s.find('x')  # returns -1 if 'x' is not found
print(s1,s2,s3)

# 5- replace method
s = 'hello world'
s1 = s.replace('o', 'x')  # replaces 'o' with 'x'
s2 = s.replace('o', 'x', 1)  # replaces the first occurrence of 'o' with 'x'
print(s1,s2)

# 6- upper method
s = 'hello world'
s1 = s.upper()  # converts the string to uppercase
s2 = s.lower()  # converts the string to lowercase
s3 = s.title()  # converts the string to title case
s4 = s.capitalize()  # converts the first character of the string to uppercase  
s5 = s.swapcase()  # converts uppercase characters to lowercase and vice versa
print(s1,s2,s3,s4,s5)

# 7- startswith and endswith method
s = 'hello world'   
s1 = s.startswith('h')  # returns True if the string starts with 'h'
s2 = s.endswith('d')  # returns True if the string ends with 'd'
print(s1,s2)

# 8- count method
s = 'hello world'
s1 = s.count('o')  # returns the number of occurrences of 'o'
s2 = s.count('o', 5)  # returns the number of occurrences of 'o' after index 5
s3 = s.count('o', 0, 5)  # returns the number of occurrences of 'o' between index 0 and 5
print(s1,s2,s3)

# 9- isalpha, isdigit, isalnum, isspace method (space is considered)
s = 'hello'
s1 = s.isalpha()  # returns True if the string contains only alphabetic characters
s2 = s.isdigit()  # returns True if the string contains only digits 
s3 = s.isalnum()  # returns True if the string contains only alphanumeric characters (letters or digits, or combination of both)
s4 = s.isspace()  # returns True if the string contains only whitespace characters
print(s1,s2,s3,s4)

# 10- isupper, islower, istitle method
s = 'hello'
s1 = s.islower()  # returns True if the string contains only lowercase characters
s2 = s.isupper()  # returns True if the string contains only uppercase characters
s3 = s.istitle()  # returns True if the string is in title case

# 11- variable inclusion string
s = 'world'
s1 = 'hello'
s2 = f'{s1} {s}'
print(s2)  # hello world