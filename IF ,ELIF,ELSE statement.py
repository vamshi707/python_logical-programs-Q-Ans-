# IF ,ELIF,ELSE statement(basic project)

#1 .wtite a python program that converts a temperature in calsius to fahrenheit or vice versa based in user input?
print(('1.fahrenheit report'))
print(('2.celsius report'))
print()

while True:

    choose=int(input('enter your choice:= '))

    if choose==1:
        n=int(input('enter a fahrenheit number ='))
        f=(n*9/5)+32
        print('the fahrenheit number is :',f)
    elif choose==2:
        k=int(input('enter a celsius number ='))

        c=(k-32)*5/9
        print('celsius number is',c)
    else:
        print('invalid')
        

    m=input('you can enter again yes/no/exit').lower()
    if m=='yes':
        print()
        print('we can choose one ')
    if m=='exit':
        print('tq u so much')
        break

    elif  m=='no':
        
        print('thank you')
        print()
        m=input('this is last choice enter again or press yes/exit').lower()
        if m=='exit':
            print()
            print('thank you so much')

            break
     
#2.write a simple calculator program that performs basic arthmetic operations (+,- *,%)based on the user input?

print('wellcome to the calculator')

 
print()

while True:
    choose=input('calculations .choose the simbles= + - * / %').lower()
    
    if choose=='+':
        a=int(input('enter a first number'))
        b=int(input('plzz enter a another number'))
        c=a+b
        print('the two number addition',c)
    elif choose=='-':
        a=int(input('enter a first number'))
        b=int(input('plzz enter a another number'))
        c=a-b
        print('the two number substraction',c)
    elif choose=='*':
        a=int(input('enter a first number'))
        b=int(input('plzz enter a another number'))
        c=a*b
        print('the two number multiplications',c)
    elif choose=='%':
        a=int(input('enter a first number'))
        b=int(input('plzz enter a another number'))
        c=a%b
        print('the two number division',c)
    elif choose=='/':
        a=int(input('enter a first number'))
        b=int(input('plzz enter a another number'))
        c=a/b
        print('the two number float division',c)
    else:
        print('invalide')
    m=input('enter a another number yes/no/exit').lower()


    if m=='no':
        print('thank you')
    elif m=='exit':
        print('thank you have a nice day')
        break
    k=input('can i calculation on the another symbles yes/exit').lower()
    if k=='exit':
        print('thank you')
        break


#3. write a python program for a simple "guess the number" game generated a random number and have the user guess it?

import random

print('             GUESS THE NUMBER GAME')
print()

num = random.randint(1, 100)

while True:
    print('         WELCOME TO THE GUESSING GAME')
    print()


    guess = int(input('Can you guess the number between 1 and 100: '))

    if guess == num:
        print('Your guess is correct!')
        print('Congratulations! You won the game!')
        break

    elif guess < 40 and guess < num:
        print('Your guessing number is very low. Please choose a higher number.')

    elif guess < num:
        print('Your guessing number is low. Please choose a higher number.')

    elif guess > 80 and guess > num:
        print('Your guessing number is very high. Please choose a lower number.')

    elif guess > num:
        print('Your guessing number is high. Please choose a lower number.')

    else:
        print('Invalid input! Please enter a number between 1 and 100.')

    print()

    m = input('Do you want to continue? Type yes/no: ').lower()

    if m == 'no':
        print()
        print('Thank you for playing this game!')
        break

    print()









        
        
                
                
    
    
    
 
 
        
     





 

    
    














