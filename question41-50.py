#41. Write a Python program to check whether a file exists.
#code:

import os.path
filename = input("enter file name")
print(os.path.isfile(filename))

#42. Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS.
#code:

import struct
print(struct.calcsize("P") * 8)

#43. Write a Python program to get OS name, platform and release information. 
#code:

import platform
import os
print("Name of the operating system:",os.name)
print("\nName of the OS system:",platform.system())
print("\nVersion of the operating system:",platform.release())


#44. Write a Python program to locate Python site-packages. 
#code:

import site
print(site.getsitepackages())

#45. Write a Python program to call an external command. 
#code:

from subprocess import call
call(["mkdir", "seasia"])

#46. Write a python program to get the path and name of the file that is currently executing. 
#code:

import os
print("Current File Name : ",os.path.realpath(__file__))


#47. Write a Python program to find out the number of CPUs using. 
#code:


import multiprocessing
print(multiprocessing.cpu_count())

#48. Write a Python program to parse a string to Float or Integer. 
#code:

n = input('enter a number: ')
print(float(n))
print(int(float(n)))


#49. Write a Python program to list all files in a directory in Python. 
#code:

from os import listdir
from os.path import isfile, join
files_list = [f for f in listdir('D:/') if isfile(join('D:/', f))]
print(files_list)


#50. Write a Python program to print without newline or space.
#code:

n = int(input("Enter any no. : "))
for i in range(n):
    print('*',end ="")
