#111. Write a Python program to make file lists from current directory using a wildcard.
#code:

import glob
file_list = glob.glob('*.*')
print(file_list)

print(glob.glob('*.py'))

#112. Write a Python program to remove the first item from a specified list. 
#code:

color = ["Red", "Black", "Green", "White", "Orange"]
print("Original list elements:", color)
del color[0]
print("After removing the first color:", color)

#113. Write a Python program to input a number, if it is not a number generates an error message. 
#code:

a = input("enter a number: ")

try:
    b = float(a)
    
except:
    print("not a numarice value. ")

#114. Write a Python program to filter the positive numbers from a list. 
#code:

nums = [34, 1, 0, -23, 12, -88]

for i in nums:
    if i>0:
        print(i)


#115. Write a Python program to compute the product of a list of integers (without using for loop).
#code:

from functools import reduce
nums = [10, 20, 30,]
print("Original list numbers:")
print(nums)
nums_product = reduce( (lambda x, y: x * y), nums)
print("\nProduct is ",nums_product)


#116. Write a Python program to print Unicode characters. 
#code:

str = u'\u0056\u0069\u006b\u0072\u0061\u006e\u0074 \u0044\u0065\u0076\u004f\u0070\u0073'
print(str)


#117. Write a Python program to prove that two string variables of same value point same memory location.
#code:

a = "ajay"
b = "ajay"

print("Memory location of a = ", id(a))
print("Memory location of b = ", id(b))

#118. Write a Python program to create a bytearray from a list. 
#code:

no = int(input("Enter a integer no to convert into Betyarray: "))

x = bytearray(no)
print(x)

#119. Write a Python program to round a floating-point number to specified number decimal places. 
#code:

order_amt = 212.374
print('\nThe total order amount comes to %f' % order_amt)
print('The total order amount comes to %.2f' % order_amt)

#120. Write a Python program to format a specified string limiting the length of a string. 
#code:

str_num = "Vikrant from DevOps"
print("Original string:", str_num)
print('%.7s' % str_num)
print('%.15s' % str_num)

