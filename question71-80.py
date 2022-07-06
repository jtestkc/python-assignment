#71. Write a Python program to get a directory listing, sorted by creation date. 
#code:

from stat import S_ISREG, ST_CTIME, ST_MODE
import os, sys, time

#Relative or absolute path to the directory
dir_path = sys.argv[1] if len(sys.argv) == 2 else r'.'

#all entries in the directory w/ stats
data = (os.path.join(dir_path, fn) for fn in os.listdir(dir_path))
data = ((os.stat(path), path) for path in data)

# regular files, insert creation date
data = ((stat[ST_CTIME], path)
           for stat, path in data if S_ISREG(stat[ST_MODE]))

for cdate, path in sorted(data):
    print(time.ctime(cdate), os.path.basename(path))

#72. Write a Python program to get the details of math module. 
#code:

import math            

math_ls = dir(math)  
print(math_ls)

#73. Write a Python program to calculate midpoints of a line. 
#code:

x1 = float(input("Enter X cordinate of first pofloat : "))
y1 = float(input("Enter Y cordinate of first pofloat : "))

x2 = float(input("Enter X cordinate of second pofloat : "))
y2 = float(input("Enter Y cordinate of second pofloat : "))

x3 = (x1+x2)/2
y3 = (y1+y2)/2

print("Mid pofloat is ", x3,y3)

#74. Write a Python program to hash a word. 
#code:

x1 = float(input("Enter X cordinate of first pofloat : "))
y1 = float(input("Enter Y cordinate of first pofloat : "))

x2 = float(input("Enter X cordinate of second pofloat : "))
y2 = float(input("Enter Y cordinate of second pofloat : "))

x3 = (x1+x2)/2
y3 = (y1+y2)/2

print("Mid pofloat is ", x3,y3)


#75. Write a Python program to get the copyright information and write Copyright information in Python code. 
#code:

print("Python copyright information:\n")
print(copyright)

#76. Write a Python program to get the command-line arguments (name of the script, the number of arguments, arguments) passed to a script. 
#code:

import sys
print("This is the name/path of the script:"),sys.argv[0]
print("Number of arguments:",len(sys.argv))
print("Argument List:",str(sys.argv))


#77. Write a Python program to test whether the system is a big-endian platform or little-endian platform. 
#code:

import sys
print()
if sys.byteorder == "little":
    #intel, alpha
    print("Little-endian platform.")
else:
    #motorola, sparc
    print("Big-endian platform.")
print()


#78. Write a Python program to find the available built-in modules.
#code:

import sys
module_name = ', '.join(sorted(sys.builtin_module_names))
print(module_name)


#79. Write a Python program to get the size of an object in bytes. 
#code:

import sys
str1 = input("Enter any data : ")
size = sys.getsizeof(str1)
print(f"Entered data is of {size} bytes.")


#80. Write a Python program to get the current value of the recursion limit.
#code:

import sys
print("Current value of the recursion limit:")
print(sys.getrecursionlimit())
