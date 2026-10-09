# IF - else statement

# 1. write a python program that check if a given year leap year ?

year=int(input('enter a year'))

if year%400==0 or (year%4==0 and year%100!=0):
     print('leap year')
else:
     print('not a leap year')

# 2. write a python program that checks if a given char is a vowel or a consonant?

n=input('enter a letter')
s='aeiouAEIOU'
if n in s:
     print('vowel')
else:
     print('consonent')

#3. write a python program that checks if year is a centure year?

year=int(input('enter a year'))

if year%100==0:

     print(year%100,'the year of the centure')

else:
     print('not a centure year')
     
#4. write a python program that checks if a given number is prime or not ?

n=int(input('enter a number'))

cnt=0
 

if n%1==0:
     cnt=cnt+1
if n%2==0:
     cnt=cnt+1
if n%3==0:
     cnt=cnt+1
if n%4==0:
     cnt=cnt+1
if n%5==0:
     cnt=cnt+1

    
if cnt==2:
     print('prime')
else:
     print('not a prime')

#5. write a python program that checks if a person is eligable to vote based on their age?

n=int(input('enter a person age'))

if n>=18:
     print('rights to vote')
else:
     print('he not eliagble for the vote')


#6. write a python program that checks if a number is positive or non-positive('including zero')?

n=int(input('enter a number'))
 
if n>0:
     print('positive')
else:
     if n==0:
          
          print('u typed zero this value not suitable plzz press another value including zero')    
          
     print('not-positive')

#7. write a python program that compares two numbera and prints the largest one?

a=int(input('enter a number'))
b=int(input('enter a another number'))

if a>b:
     print('largest number is=',a)
else:
     print('largest number is=',b)


#8. write a python program that checks the given char is latter or not?

n=input('plzz enter a letter or  not but press enter button')

if n:
     print('the give char is letter')
else:
     print('its not a letter')



#9. write a python program that finds and print the smallest of three number without using inbuilt function method plz write u r own logic?

a=int(input('enter a value 1'))
b=int(input('enter a values 2'))
c=int(input('enter a value 3'))

if a<b and a<c:
     print('smallest number is',a)
if b<c and b<a:
     print('smallest number is',b)
if c<a and c<b:
     print('smallest number is',c)
     
else:
     if a==b and b==c and c==a:
          
          print('the values are equal')
      

 
#10. write a python progrom check if a given string is a pelindrome or not ?

n= str(input('enter a char'))

if  n[ : :-1]==n:
     print('pelindrome')
else:
     print('not a pelindrome')



#11. write a python program that finds and print the largest of four numbers?

a=int(input('enter a number of value='))
b=int(input('enter a number of values='))
c=int(input('enter a number of value='))
d=int(input('enter a number of value='))

if a>b and a>c and a<d:
     print('the largest number is=',a)
if b>a and b>c and b>d:
     print('the largest number is =',b)
if c>a and c>b and c>d:
     print('the largest number is =',c)
if d>a and d>b and d>c:
     print('the largest number is =',d)
else:
     if a==b and b==c and c==d and d==a:
          
          print('the all values are equal plzz choose the another number')
 


#12. write a python program that takes two numbers as input and determine the sign of their difference?

a=int(input('enter a number'))
b=int(input('enter a number'))

if a==b:
     print('sign both number is equal')
else:
     
     if a > b:
     
        print('difference is positive')
     else:
     
        print('difference is negative')


#13.Check whether a year is a leap year (Alternative method)

year = int(input("Enter a year: "))

if year % 400 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("Not a leap year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")


#14. Find the absolute value of a number

n = int(input("Enter a number: "))

if n < 0:
    print("Absolute value:", -n)
else:
    print("Absolute value:", n)


#15 write a program that checks the number multiple of 7 or not?

n=int(input('enter a number'))

if n%7==0:
     print('this number muntiple with 7')
else:
     print('this number not multiple with 7')
