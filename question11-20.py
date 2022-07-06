#11. Write a Python program to print the documents (syntax, description etc.) of Python
# built-in function(s).
# Sample function : abs()
# Expected Result :
# abs(number) -> number
#Return the absolute value of the argument

#code : 

print(abs.__doc__)


#12. Write a Python program to print the calendar of a given month and year.
# Note : Use 'calendar' module.

#code : 

import calendar
y = int(input("Input the year : "))
m = int(input("Input the month : "))
print(calendar.month(y, m))

#13. Write a Python program to print the following 'here document'. 
#Sample string :
#a string that you "don't" have to escape
#This
#is a ....... multi-line
#heredoc string --------> example

#code :

print("""
a string that you "don't" have to escape
This
is a  ....... multi-line
heredoc string --------> example
""")

#14. Write a Python program to calculate number of days between two dates.
#Sample dates : (2014, 7, 2), (2014, 7, 11)
#Expected output : 9 days

#code : 

from datetime import date

f_date = date(2019, 7, 2)
l_date = date(2016, 7, 11)

difference = l_date - f_date

print(abs(difference.days))


#15. Write a Python program to get the volume of a sphere with radius 6.


#code : 


from django.shortcuts import redirect


from math import pi

radius = float(input("Enter radius of Sphere: "))

volume = 4/3*pi*radius*radius*radius

print("Sphere Volume is : ", volume)


#16. Write a Python program to get the difference between a given number and 17, if the number
# is greater than 17 return double the absolute difference. 

#code : 

no = int(input("Enter a number: "))

if no < 17:
    print("Difference is: ",17-no)
else:
    a = no-17
    b = abs(a)

    print("Given no is greater then 17 hence double of its absoulte difference is " , 2*b)


#17. Write a Python program to test whether a number is within 100 of 1000 or 2000. 


#code : 

no = int(input("Enter a no. "))

if (no >= 900 and no <= 1100):
    print("Given is within 100 of 1000 ")
elif ( no >= 1900 and no <= 2100):
    print("Given is within 100 of 2000 ")
else:
    print("Given is not within 100 of 1000 or 2000 ")


#18. Write a Python program to calculate the sum of three given numbers, if the values are equal
# then return three times of their sum. 

#code :

a = float(input("Enter First no. "))
b = float(input("Enter Second no. "))
c = float(input("Enter Third no. "))

if (a==b and c==b):
    d = a+b+c
    e = d*3
    print("ALL no are equla.\nHence three time of the sunm is :",e)
else:
    print("Sum is ", a+b+c)


#19. Write a Python program to get a new string from a given string where "Is" has been added to
# the front. If the given string already begins with "Is" then return the string unchanged. 
#code : 

string = str(input("Enter a string : "))
if (len(string) >=2 and string[:2] == 'Is'):
    print(string)
else:
    print("Is"+string)

##20. Write a Python program to get a string which is n (non-negative integer) copies of a given string. 

#code : 

string = str(input("Enter a string : "))
rep = int(input("Enter no of rep: "))

ans = ""

for i in range(rep):
    ans = ans + string

print(ans)
