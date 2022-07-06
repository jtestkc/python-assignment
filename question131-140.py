#131. Write a Python program to split a variable length string into variables. 
#code:

x =input("enter a string: ")
length = int(len(x)/2)
f = ""
l = ""
for i in range(length):
    f += x[i]

print(f)
print("\n")

for i in range(length,len(x)):
    l += x[i]

print(l)


#132. Write a Python program to list home directory without absolute path. 
#code:

import os.path
print(os.path.expanduser('~'))

#133. Write a Python program to calculate the time runs (difference between start and current time) of a program. 
#code:

from timeit import default_timer
def timer(n):
    start = default_timer()
    # some code here
    for row in range(0,n):
        print(".",end="")
    print(f"\nTime taken to print {n} . is : ",default_timer() - start)

timer(1234)


#134. Write a Python program to input two integers in a single line. 
#code:

print("Input the value of x & y & z")
x, y, z = map(int, input().split())
print("The value of x & y are: ",x,y,z)


#135. Write a Python program to print a variable without spaces between values. 
#Sample value : x =30
#Expected output : Value of x is "30"
#code:

x = input("enter a value : ")
print(f'Values of x is {x}')

#136. Write a Python program to find files and skip directories of a given directory.
#code:

import os

# main_path = 'C:/Users/vikrant/Desktop/Python assigment'

main_path = input("Enter a Path: ")
for i in os.listdir(main_path):
    # print(i)
    path = os.path.join(main_path,i)  
    # print(path)  
    if os.path.isfile(path):
        print(i)
    # else:
    #     continue


#137. Write a Python program to extract single key-value pair of a dictionary in variables.
#code:

d = {'Red': 'Green'}
(c1, c2), = d.items()
print(c1)
print(c2)

#138. Write a Python program to convert true to 1 and false to 0. 
#code:

x = input("enter True for 1 : ")

x = int(x.lower() == 'true')
print(x)

#139. Write a Python program to valid a IP address. 
#code:


import socket
addr = input("enter a ip")
try:
    socket.inet_aton(addr)
    print("Valid IP")
except socket.error:
    print("Invalid IP")


#140. Write a Python program to convert an integer to binary keep leading zeros. 
#Sample data : x=12
#Expected output : 00001100
#0000001100
#code:

x = int(input("Enter a number : "))
print(format(x, '08b'))
