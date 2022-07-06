#141. Write a python program to convert decimal to hexadecimal. 
#Sample decimal number: 30, 4
#Expected output: 1e, 04
#code:

x  = int(input("Enter a number : "))
print(format(x, '02x'))


#142. Write a Python program to check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones of same
# length in a given string. Return True/False.
#Original sequence: 01010101
#Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
#True
#Original sequence: 00
#Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
#False
#Original sequence: 000111000111
#Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
#True
#Original sequence: 00011100011
#Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
#False
#code:

str1 = input("Enter a Binary no: ")
while '01' in str1:
        str1 = str1.replace('01', '')
print( len(str1) == 0)


#143. Write a Python program to determine if the python shell is executing in 32bit or 64bit mode on operating system. Go to the editor
#code:

import struct
print(struct.calcsize("P") * 8)


#144. Write a Python program to check whether variable is integer or string. Go to the editor

#code:

print(isinstance(25,int) or isinstance(25,str))
print(isinstance([25],int) or isinstance([25],str))
print(isinstance("25",int) or isinstance("25",str))


#145. Write a Python program to test if a variable is a list or tuple or a set. Go to the editor
#code:

#x = ['a', 'b', 'c', 'd']
#x = {'a', 'b', 'c', 'd'}
x = ('tuple', False, 3.2, 1)
if type(x) is list:
    print('x is a list')
elif type(x) is set:
    print('x is a set')
elif type(x) is tuple:
    print('x is a tuple')    
else:
    print('Neither a list or a set or a tuple.')


#146. Write a Python program to find the location of Python module sources. Go to the editor

#code:

import imp
module = input("Enter a module name : ")
print("Location of Python os module sources:")
print(imp.find_module(module))


#147. Write a Python function to check whether a number is divisible by another number. Accept two integers values form the user. Go to the editor
#code:

x =int(input("enter a value : "))
y =int(input("enter second value : "))

if x%y == 0 :
    print("True")
else: 
    print("False")


#148. Write a Python function to find the maximum and minimum numbers from a sequence of numbers. Go to the editor
#Note: Do not use built-in functions.
#code:

data = [0, 10, 15, 40, -5, 42, 17, 28, 75]

l = data[0]
s = data[0]

for num in data:
    if num> l:
        l = num
    elif num< s:
        s = num
print(f'Smallest value is {s}\nLargest value is {l}')  


#149. Write a Python function that takes a positive integer and returns the sum of the cube of all the positive integers smaller than the specified number. Go to the editor
#code:

n = int(input("Enter a number : "))
sum = 0 

while n > 0:
    n -=1
    sum += n**3

print(sum)


#150. Write a Python function to check whether a distinct pair of numbers whose product is odd present in a sequence of integer values.
#code:

dt2 = [2, 4, 6, 8]

count = 0

for i in dt2:
    if (i % 2 != 0):
        count +=1

if count >= 2:
    print("True")
else: 
    print("False")
