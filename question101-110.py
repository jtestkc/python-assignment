#101. Write a Python program to access and print a URL's content to the console. 
#code:

from http.client import HTTPConnection
conn = HTTPConnection("seasia.com")
conn.request("GET", "/")  
result = conn.getresponse()
# retrieves the entire contents.  
contents = result.read() 
print(contents)


#102. Write a Python program to get system command output.
#code:


import subprocess
# file and directory listing
returned_text = subprocess.check_output("dir",  universal_newlines=True)
print("dir command to list file and directory")
print(returned_text)


#103. Write a Python program to extract the filename from a given path. 
#code:

import os

print(os.path.basename('D:/boto3/ec2.py'))

#104. Write a Python program to get the effective group id, effective user id, real group id, a list of supplemental group ids associated with the current process.
#Note: Availability: Unix.
#code:

# Will excuted only in liux OS
import os
print("\nEffective group id: ",os.getegid())
print("Effective user id: ",os.geteuid())
print("Real group id: ",os.getgid())
print("List of supplemental group ids: ",os.getgroups())

#105. Write a Python program to get the users environment. 
#code:

import os
print()
print(os.environ)


#106. Write a Python program to divide a path on the extension separator. 
#code:

import os.path
for path in [ 'test.txt', 'filename', '/user/system/test.txt', '/', '' ]:
    print(path, os.path.splitext(path))


#107. Write a Python program to retrieve file properties. 
#code:

import os.path
import time

print('File         :', __file__)
print('Access time  :', time.ctime(os.path.getatime(__file__)))
print('Modified time:', time.ctime(os.path.getmtime(__file__)))
print('Change time  :', time.ctime(os.path.getctime(__file__)))
print('Size         :', os.path.getsize(__file__))


#108. Write a Python program to find path refers to a file or directory when you encounter a path name. 
#code:

import os.path

for file in [ __file__, os.path.dirname(__file__), '/', './broken_link']:
    print('File        :', file)
    print('Absolute    :', os.path.isabs(file))
    print('Is File?    :', os.path.isfile(file))
    print('Is Dir?     :', os.path.isdir(file))
    print('Is Link?    :', os.path.islink(file))
    print('Exists?     :', os.path.exists(file))
    print('Link Exists?:', os.path.lexists(file))
    print("#############################")
	


#109. Write a Python program to check if a number is positive, negative or zero. 
#code:

num = float(input("Input a number: "))
if num > 0:
   print("It is positive number")
elif num == 0:
   print("It is Zero")
else:
   print("It is a negative number")


#110. Write a Python program to get numbers divisible by fifteen from a list using an anonymous function. 
#code:

num_list = [45, 55, 60, 37, 100, 105, 220]
# use anonymous function to filter
result = list(filter(lambda x: (x % 15 == 0), num_list))
print("Numbers divisible by 15 are",result)
