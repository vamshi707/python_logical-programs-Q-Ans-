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
 
 

     

























     
