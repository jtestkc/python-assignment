#81. Write a Python program to concatenate N strings.
#code:

list_of_colors = ['Red', 'White', 'Black']  
colors = '-'.join(list_of_colors)

print("\nAll Colors: "+colors)


#82. Write a Python program to calculate the sum of all items of a container (tuple, list, set, dictionary). 
#code:

s = sum([10,20,30])
print("\nSum of the container: ", s)
print()


#83. Write a Python program to test whether all numbers of a list is greater than a certain number. 
#code:
num = [2, 3, 4, 5]
intger = int(input("Enter a intger to compare: "))
print(all(x > intger for x in num))


#84. Write a Python program to count the number occurrence of a specific character in a string.
#code:

s = "The quick brown fox jumps over the lazy dog."  
count = 0
l = input("Enter a letter to check it's occourence. : ")
for i in s:
    
    if i==l:
        count += 1
    
print(count)


#85. Write a Python program to check whether a file path is a file or a directory.
#code:

import os  
path="q1.py"  
if os.path.isdir(path):  
    print("\nIt is a directory")  
elif os.path.isfile(path):  
    print("\nIt is a normal file")  
else:  
    print("It is a special file (socket, FIFO, device file)" )


#86. Write a Python program to get the ASCII value of a character.
#code:

letter = input("enter a character: ")
print("Its ASCII code is : " ,ord(letter))


#87. Write a Python program to get the size of a file.
#code:


import os
file_name = input("enter a file name. : ")
file_size = os.path.getsize(file_name)

print("file size is : ", file_size)


#88. Given variables x=30 and y=20, write a Python program to print "30+20=50".
#code:

x=20
y=30
print(f"{x}+{y}={x+y}")


#89. Write a Python program to perform an action if a condition is true.
#Given a variable name, if the value is 1, display the string "First day of a Month!" and do nothing if the value is not equal.
#code:

n=1
if n == 1:
   print("\nFirst day of a Month!")
print()


#90. Write a Python program to create a copy of its own source code. 
#code:

f_open = open("q2.py")
r_open = f_open.read()

w_open = open("ok.txt" , "w")
w_open.write(r_open)
