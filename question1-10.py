# 1. Write a Python program to print the following string in a specific format 
# Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" Output :
#
# Twinkle, twinkle, little star,
#	How I wonder what you are! 
#		Up above the world so high,   		
#		Like a diamond in the sky. 
# Twinkle, twinkle, little star, 
#	How I wonder what you are

#Code : 
	
print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")


#2.  Write a Python program to get the Python version you are using.

#Code : 

import sys
print("python version: ", sys.version)

#3. Write a Python program to display the current date and time.
#  Sample Output :
#  Current date and time :
# 2014-07-05 14:34:14
#
#code : 

from datetime import datetime

import datetime

print("Date and time :\n",datetime.datetime.now())


#4. Write a Python program which accepts the radius of a circle from the user and compute the area.
#Sample Output :
#r = 1.1
#Area = 3.8013271108436504
#
##code : 

from distutils.util import rfc822_escape
from math import pi
radius = float(input("Enter raious of circle"))
area = pi*radius**2
print("Area of given radius circle is : ",area)

#5. 5. Write a Python program which accepts the user's first and last name and
# #print them in reverse order with a space between them.
#
#code : 

f_name = str(input("Enter your First name: "))
L_name = str(input("Enter your Last name: "))

print("Hello ",L_name ,f_name)


#6. Write a Python program which accepts a sequence of comma-separated numbers from
# user and generate a list and a tuple with those numbers.
## Sample data : 3, 5, 7, 23
# Output :
## List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')

#code :

data = input("Enter a comma serprated data: ")

split = data.split(",")
print("List =",list(split) )
print("Tuple =",tuple(split) )

#7. Write a Python program to accept a filename from the user and print the extension of that.
#Sample filename : abc.java
#Output : java

#code : 

file_name = input("enter file name with extison: ")
split = file_name.split(".")
print("Your file extison is : ", split[-1])


#8. Write a Python program to display the first and last colors from the following list.
#color_list = ["Red","Green","White" ,"Black"]

#code :

color_list = ["Red","Green","White" ,"Black"]
print("first colour: ",color_list[0],"\nLast color: ", color_list[-1])


#9. Write a Python program to display the examination schedule. (extract the date from exam_st_date).
#exam_st_date = (11, 12, 2014)
##Sample Output : The examination will start from : 11 / 12 / 2014

###code :

exam_st_date = (11,12,2014)
print( "The examination will start from : %i / %i / %i"%exam_st_date)


#10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. 
##Sample value of n is 5
###Expected Result : 615


#code :

no = int(input("Enter a number: "))
output = no+no*no+no*no*no
print("Output is : ", output)

