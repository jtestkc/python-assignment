#31. Write a Python program to compute the greatest common divisor (GCD) of two positive integers. 
#code:

x = int(input('Enter first digit : '))
y = int(input('Enter second digit : '))

def gcd(x, y):
   gcd = 1   
   if x % y == 0:
       return y   
   for k in range(int(y / 2), 0, -1):
       if x % k == 0 and y % k == 0:
           gcd = k
           break 
   return gcd

print("GCD of numbers are : ", gcd(x,y))
#32. Write a Python program to get the least common multiple (LCM) of two positive integers.
#code:

x = int(input('Enter first digit : '))
y = int(input('Enter second digit : '))

def lcm(x, y):
  if x > y:
      z = x
  else:
      z = y
  while(True):
      if((z % x == 0) and (z % y == 0)):
          lcm = z
          break
      z += 1
  return lcm

print("LCM of given numbers is ", lcm(x,y))

print("GCD of numbers are : ", gcd(x,y))


#33. Write a Python program to sum of three given integers. However, if two values are equal sum will be zero. 
#code:

x = int(input('Enter first digit : '))
y = int(input('Enter second digit : '))
z = int(input('Enter third digit : '))


if (x==y or y==z or z==x ):
    print("sum is 0")
else:
    print("sum is ", x+y+z)

#34. Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20. 
#code:

x = int(input('Enter first digit : '))
y = int(input('Enter second digit : '))

sum = x+y

if (sum >=15 and sum <=20):
    print("sum is 20")
else:
    print("sum is ", sum )

#35. Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5. 
#code:

x = int(input('Enter first digit : '))
y = int(input('Enter second digit : '))

sum = x+y

if (x==y or sum == 5):
    print("True")

#36. Write a Python program to add two objects if both objects are an integer type.
#code:

def addnum(x,y):
    if isinstance(x,int) and isinstance(y,int):
        return x+y
    else:
        return "Input must be of integer type"

print(addnum(4,6))
print(addnum(4,6.7))
print(addnum(4,'6'))


#37. Write a Python program to display your details like name, age, address in three different lines. 
#code:

name = input("Enter name: ")
age = int(input("Enter age: "))
address = input("Enter address: ")

print (f"Name = {name}\nAge = {age}\nAddress = {address}")

#38. Write a Python program to solve (x + y) * (x + y).
#Test Data : x = 4, y = 3
#Expected Output : (4 + 3) ^ 2) = 49
#code:

x = int(input('Enter first digit : '))
y = int(input('Enter second digit : '))

sum = x+y
result = sum*2

print(result)

#39. Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years. 
#Test Data : amt = 10000, int = 3.5, years = 7
#Expected Output : 12722.79
#code:

amt = 10000
int = 3.5
years = 7
future_value = amt*((1+(0.01*int)) ** years)
print(round(future_value,2))


#40. Write a Python program to compute the distance between the points (x1, y1) and (x2, y2). 
#code:

import math
p1 = [4, 0]
p2 = [6, 6]
distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )

print(distance)