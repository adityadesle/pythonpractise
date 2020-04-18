# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 13:38:25 2020

@author: 66IN
"""


#python examples
'''
#1) add 2 number

x =10
y =20

z=x+y
print(z)


#2) number except number divisible by 3

for i in range(1,10):
    if i%3==0:
        continue
    
    print(i)
    
print("bye")    


#3) patterns 
    
for i in range(5):

    for i in range(5):
        print('# ',end="")
        
    print()    
 
    
for i in range(5):

    for i in range(i):
        print('# ',end="")
        
    print()    
    
  
for i in range(5,0,-1):

    for j in range(i):
        print(j,end="")
        
    print()    


#4) for-else

nums =[12,16,18,21,26]

for num in nums:
    if num%5 == 0:
        print(num)
        
else:
    print("not found")    
    


#5) prime 
num = int(input("enter the number:"))

for i in range(2,num):
    if num % i == 0:
        print("not prime")
        break
else:
    print("prime")    


#6) array from an array

from array import *

vals = array('i',[5,3,-8,9])
 
newArr = array(vals.typecode, (a for a in vals))

for i in newArr:
    print(i)

#7) print array in from user input and search the element's location

from array import *

arr = array('i',[])

n = int(input('enter the length:'))

for i in range(n):
    x = int(input("enter value:"))
    arr.append(x)
    
print(arr)    

val =int(input("enter the value to be searched"))

k=0

for e in arr:
    if e==val:
        print("the position is",k)
        break
    k+=1
    
#can also find index by function 

print("by function ",arr.index(val))    
    
#8) starting with numpy

from numpy import *

arr = array([2,5,6,7.0]) #if any 1 value is float whole array will be float

print(arr.dtype)

print(arr)
   
   
#9) display current-time and date:

import datetime
now = datetime.datetime.now()

print("current date and time")
print(now.strftime("%Y-%m-%d %H:%M:%S"))   



#10) enter user values and convert into list and tuples

values = (input("enter the values"))

list = values.split(",")
tuple = tuple(list)

print("list ",list)
print("tuple ",tuple)


#11) explaining elevator using if statement

user_floor = 6

current_floor = int(input("enter the value here"))

difference = user_floor - current_floor

if difference < 0:
    print("move down")

if difference > 0:
    print("move up")    
'''
