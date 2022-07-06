#61. Write a Python program to convert the distance (in feet) to inches, yards, and miles. 
#code:


d_ft = int(input("Input distance in feet: "))
d_inches = d_ft * 12
d_yards = d_ft / 3.0
d_miles = d_ft / 5280.0

print("The distance in inches is: " , d_inches)
print("The distance in yards is : " , d_yards)
print("The distance in miles is : ", d_miles)

#62. Write a Python program to convert all units of time into seconds.
#code:

days = int(input("Input days: ")) * 3600 * 24
hours = int(input("Input hours: ")) * 3600
minutes = int(input("Input minutes: ")) * 60
seconds = int(input("Input seconds: "))

time = days + hours + minutes + seconds

print("The  amounts of seconds", time)

#63. Write a Python program to get an absolute file path. 
#code:

import os

filename = input("ENter file Name: ")

print(os.path.abspath(filename))  

#64. Write a Python program to get file creation and modification date/times. 
#code:

import os.path, time
filename = input("ENter file Name: ")
print("Last modified:" , time.ctime(os.path.getmtime(filename)))
print("Created: ", time.ctime(os.path.getctime(filename)))

#65. Write a Python program to convert seconds to day, hour, minutes and seconds. 
#code:

time = float(input("Input time in seconds: "))
day = time // (24 * 3600)
time = time % (24 * 3600)
hour = time // 3600
time %= 3600
minutes = time // 60
time %= 60
seconds = time
print(f"day : {day} , hour : {hour} , minute : {minutes}, seconds : {seconds} ")


#66. Write a Python program to calculate body mass index. 
#code:

height = float(input("Input your height in Feet: "))
weight = float(input("Input your weight in Kilogram: "))
print("Your body mass index is: ", weight / (height * height))


#67. Write a Python program to convert pressure in kilopascals to pounds per square inch, a millimeter of mercury (mmHg) and atmosphere pressure.
#code:

kpa = float(input("Input pressure in in kilopascals> "))
psi = kpa / 6.89475729
mmhg = kpa * 760 / 101.325
atm = kpa / 101.325
print("The pressure in pounds per square inch: %.2f psi"  % (psi))
print("The pressure in millimeter of mercury: %.2f mmHg" % (mmhg))
print("Atmosphere pressure: %.2f atm." % (atm))


#68. Write a Python program to calculate sum of digits of a number. 
#code:

n = int (input("Enter your no.: "))
sum = 0
while n>0:
    a = n%10
    n = int(n/10)
    sum +=a
print(sum)


#69. Write a Python program to sort three integers without using conditional statements and loops. 
#code:

a = int(input("enter first no. : "))
b = int(input("enter second no. : "))
c = int(input("enter third no. : "))

list = []
list.append(a)
list.append(b)
list.append(c)
list.sort()
print(list)

#70. Write a Python program to sort files by date. 
#code:


import glob
from ntpath import join
import os

files = glob.glob("*.py")
files.sort(key=os.path.getmtime)
print("\n".join(files))