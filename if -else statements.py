# IF - else statement

#1. write a python program that check if a given year leap year ?

year=int(input('enter a year'))

if year%400==0 or (year%4==0 and year%100==0):
     print('leap year')
else:
     print('not a leap year')


