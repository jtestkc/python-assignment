#21. Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.
#code:

no = int(input("Enter a number to chaeck its even or odd: "))

if (no%2 == 0):
    print(no,"is even")
else:
    print(no,"is odd")

#22. Write a Python program to count the number 4 in a given list. 
#code:

def list_count_4(nums):
  count = 0  
  for num in nums:
    if num == 4:
      count = count + 1

  return count

print("Total no of 4 found in List are : ",list_count_4([1, 4, 6, 7, 4]))


#23. Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2.
#code:

def substring_copy(str, n):
    s_string = 2
    if s_string > len(str):
        s_string = len(str)
    substr = str[:s_string]
    
    result = ""
    for i in range(n):
        result = result + substr
    return result

print(substring_copy('vikrant', 2))



#24. Write a Python program to test whether a passed letter is a vowel or not. 
#code:

alphabate = str(input("Enter a letter : "))
letter = alphabate.lower()
if (letter =='a' or letter =='e'or letter =='i'or letter =='o' or letter =='u'):
    print("It's a Vowel")
else:
    print("It's not a Vowel")


#25. Write a Python program to check whether a specified value is contained in a group of values. 
#Test Data :
#3 -> [1, 5, 8, 3] : True
#-1 -> [1, 5, 8, 3] : False
#code:

no = int(input("Enter a no: "))

def number(no):
    list = [1,5,8,3]
    for i in list:
        if (no == i):
            return True
    return False

print(number(no))



#26. Write a Python program to create a histogram from a given list of integers. 
#code:

from ast import pattern


patran = "*"
list= [4,3,6,2,4]

for i in list:
    print(patran*i)

#27. Write a Python program to concatenate all elements in a list into a string and return it. 
#code:

list = [1, 5, 12, 2]

answer = ''
for i in list:
    j = str(i)
    answer +=j
print(answer)


#28. Write a Python program to print all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence. 
#Sample numbers list :

#numbers = [    
#    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
#    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
#    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
#    958,743, 527
#    ]
#code:

numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]

for i in numbers:
    if i == 237:
        print(i,"BREAK")
        break
    elif i % 2 == 0:
        print(i, " is a Even no.")

#29. Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2. 
#Test Data :
#color_list_1 = set(["White", "Black", "Red"])
#color_list_2 = set(["Red", "Green"])
#Expected Output :
#{'Black', 'White'}
#code:

color_list_1 = ["White", "Black", "Red"]
color_list_2 = ["Red", "Green"]

color_list_3 = []
for i in color_list_1:
    if (i!=color_list_2[0] and i!=color_list_2[1]):
            color_list_3.append(i)

print(color_list_3)

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print(color_list_1.difference(color_list_2))

#30. Write a Python program that will accept the base and height of a triangle and compute the area.
#code:

base = float(input("Enter the base of triangle: "))
height = float(input("Enter the hight of triangle: "))

area = 1/2*base* height

print(area)