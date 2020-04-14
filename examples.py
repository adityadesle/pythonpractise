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
''' 

#6) array from an array

from array import *

vals = array('i',[5,3,-8,9])
 
newArr = array(vals.typecode, (a for a in vals))

for i in newArr:
    print(i)
