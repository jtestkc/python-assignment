#121. Write a Python program to determine whether variable is defined or not.
#code:

try:
  x = 1
except NameError:
  print("Variable is not defined....!")
else:
  print("x Variable is defined.")
try:
  y 
except NameError:
  print("y Variable is not defined....!")
else:
  print("y Variable is defined.")
  

#122. Write a Python program to empty a variable without destroying it.
#Sample data: n=20
#d = {"x":200}
#Expected Output : 0
#{}

#code:

n = 20
d = {"x":200}
l = [1,3,5]
t= (5,7,8)
print(type(n)())
print(type(d)())
print(type(l)())
print(type(t)())


#123. Write a Python program to determine the largest and smallest integers, longs, floats. 
#code:

import sys
print("Float value information: ",sys.float_info)
print("\nInteger value information: ",sys.int_info)
print("\nMaximum size of an integer: ",sys.maxsize) 

#124. Write a Python program to check whether multiple variables have the same value. 
#code:

x= input("Enter value for x :")
y= input("Enter value for y :")
z= input("Enter value for z :")

if (x==y and y==z):
    print("\nAll entered values for x y and z are Equal.")


#125. Write a Python program to sum of all counts in a collections.
#code:

num = [2,2,4,6,6,8,6,10,4]

print("Total values in a list is : ", len(num))


#126. Write a Python program to get the actual module object for a given object. 
#code:

from inspect import getmodule
from math import sqrt
print(getmodule(sqrt))

#127. Write a Python program to check whether an integer fits in 64 bits. 
#code:

int_val = int(input("Enter any Integer:  "))

if int_val.bit_length() <= 63:
    print("Yes, fites in 64 bits.")
    print(int_val.bit_length(), "is the bit leangth")
else: 
    print("Not fit in 64 bits. ")
    print(int_val.bit_length(), "is the bit leangth")


#128. Write a Python program to check whether lowercase letters exist in a string. 
#code:

string = input("Enter a string without space : ")

for i in string:
    if i == i.lower():
        print("\nString contain a lower case. ")
        break

#129. Write a Python program to add leading zeroes to a string. 
#code:

string = str(input("Enter a String: "))
l_zero = int(input("Enter the Leading zeros: "))

l_string = string.ljust(l_zero, '0')

print(l_string)

#130. Write a Python program to use double quotes to display strings.
#code:

import json
print(json.dumps({'Ankur': 1, 'Vikrant': 2, 'Shubham': 3}))
