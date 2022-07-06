#91. Write a Python program to swap two variables. 
#code:


a = int (input("Enter value of a: "))
b = int (input("Enter value of b: "))

c = b
b = a
a = c
print(f'a = {a}')
print(f'b = {b}')

    
#92. Write a Python program to define a string containing special characters in various forms. 
#code:

print("\#{'}${\"}@/")
print("\#{'}${"'"'"}@/")
print(r"""\#{'}${"}@/""")
print('\#{\'}${"}@/')
print('\#{'"'"'}${"}@/')
print(r'''\#{'}${"}@/''')


#93. Write a Python program to get the Identity, Type, and Value of an object. 
#code:

x = 34
print("\nIdentity: ",x)
print("\nType: ",type(x))
print("\nValue: ",id(x))


#94. Write a Python program to convert a byte string to a list of integers. 
#code:

x = b'Abc'

print("\nConvert bytes of the said string to a list of integers:")
print(list(x))


#95. Write a Python program to check whether a string is numeric. 
#code:

str = input('Enter any value: ')

try:
    i = float(str)
    print("It's a numaric Value")
except (ValueError, TypeError):
    print('\nNot numeric')


#96. Write a Python program to print the current call stack. 
#code:

import traceback

def f1():return abc()
def abc():traceback.print_stack()
f1()


#97. Write a Python program to list the special variables used within the language. 
#code:

s_var_names = sorted((set(globals().keys()) | set(__builtins__.__dict__.keys())) - set('_ names i'.split()))
print()
print(s_var_names)
# print( '\n'.join(' '.join(s_var_names[i:i+8]) for i in range(0, len(s_var_names), 8)) )


#98. Write a Python program to get the system time. 
#Note : The system time is important for debugging, network information, random number seeds, or something as simple as program performance.
#code:

import time
print(time.ctime())


#99. Write a Python program to clear the screen or terminal.
#code:

import os
os.system('cls')

#100. Write a Python program to get the name of the host on which the routine is running. 
#code:

import socket
host_name = socket.gethostname()
print("Host name:", host_name)
