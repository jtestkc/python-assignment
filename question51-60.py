#51. Write a Python program to determine profiling of Python programs.
#Note: A profile is a set of statistics that describes how often and for how long various parts of the program executed.
#These statistics can be formatted into reports via the pstats module.
#code:

import cProfile
def sum():
    print(1+2)
cProfile.run('sum()')

#52. Write a Python program to print to stderr.
#code:


#53. Write a python program to access environment variables. 
#code:

import os
# Access all environment variables 
print('*----------------------------------*')
print(os.environ)                                              # list of all environ.
print('*----------------------------------*')
print(os.environ['COMPUTERNAME'])                              # printing a perticular environ 

#54. Write a Python program to get the current username. 
#code:

import getpass
import os
print(getpass.getuser())

print(os.environ['USERNAME']) 

#55. Write a Python to find local IP addresses using Python's stdlib. 
#code:

import socket
print([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] 
if not ip.startswith("127.")]
[:1], 
[[(s.connect(('8.8.8.8', 53)), 
s.getsockname()[0], s.close()) 
for s in [socket.socket(socket.AF_INET,socket.SOCK_DGRAM)]][0][1]]) if l][0][0])

#56. Write a Python program to get height and width of the console window. 
#code:

import os
size = os.get_terminal_size()
print(size)

# print('Number of columns and Rows: ',terminal_size())
#57. Write a Python program to get execution time for a Python method. 
#code:

import time
def sum_of_n_numbers(n):
    start_time = time.time()
    s = 0
    for i in range(1,n+1):
        s = s + i
    end_time = time.time()
    return s,end_time-start_time

n = int(input("enter a no: "))
print("\nTime to sum of 1 to ",n," and required time to calculate is :",sum_of_n_numbers(n))


#58. Write a Python program to sum of the first n positive integers.
#code:

n = int (input("Enter a no. : "))

sum = (n*(n+1))/2
print(f"Sum of first {n} positive intergers is : {int(sum)}")


#59. Write a Python program to convert height (in feet and inches) to centimeters.
#code:

feet = int(input("Enter height in feets: "))
inches = int(input("Enter height in inches: "))
 
inches += feet*12
print(inches)


h_cm = inches * 2.54

print("heoght in cm : ",int(h_cm))


#60. Write a Python program to calculate the hypotenuse of a right angled triangle.
#code:


from math import sqrt

b = float(input("Enter base length : "))
p = float(input("Enter perpendcular length : "))

h = sqrt( b**2 + p**2 )

print("hypotenuse of a right angled triangle is: ", h)