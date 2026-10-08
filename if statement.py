# 1. write python program that checks if a number is positive ?

n=int(input('enter a number'))
if n>0:
     print('positive')
 

#2.  write a python program that checks if a given string is empty or not ?

x=""

if  x:
     print('not empty')

if not x:
          print('empty')

#3. write a python program that determine if a number is positive ,negative or zero using only if statement?
n=int(input('enter a number'))

if n>0:
     print('positive number')
if n<0:
     print('negative number')
if not n or n==0:
     print('This number is zero, please choose a +ve or -ve value')
     
#4. write a python program that checks if an number is a multiple of both 3 and 5 ?

n=int(input('emter a number'))

if n*5 and n*3:
     print('this number multiply with both numbers | 3 *',n,'= ' ,n*3,' and | 5 *',n, '= ' ,n*5)
     

#5 write a python program that determine if a number is perfect square ?

x=5

if n**2:
     print(n**2,'the number is perfect square')


#6. write a python program that checks if a number is divisiable by both 2 and 3?
n=int(input('enter a  number'))

if n%2==0 and n%3==0:
     print(n%2==0, 'and' ,n%3==0,'both number divisiablity')


#7. write a python program that determain if a number is perfect cube ?

x=2

if x**3:
     print(x**3,'the perfect cube ')

#8. write a python program that checks if a given number is multiply of 4?

n=int(input('enter a number'))

if n*4:
     print(n,'*','4 = ', n*4,'the given number is multiply with 4')







     
