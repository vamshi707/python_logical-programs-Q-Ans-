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

#4. write a python program that checks the strength of user password based on certain criteria ?
print('          welcome to our application please register your password')

while True:
        
    password=input('create  your password strong')

    if len(password)<8:
        print('week password')
    elif password.isalpha():
        print('the char must should in number also')
    elif password.isdigit():
        print('the password should be letter also')
    elif password.isalnum():
        print('password must be in the digits also')
    else:
        print('strong password create done')
        

    m=input('can u create again password yes/no').lower()

    if m=='no':
        print('thankyou')
        break

#5. write a python program that calculate the final price of an itam after applying a discount based on the purchase amount?

print('        welcome to my fashion shop')
print()

while True:
    print(f''' choose the dress:

               1.shirt
               2.pant
               3.sarees''')
    
    choose=input('please enter the option wt u want like 1/2/3 :')
    if choose=='1':
        print('thank you for choosing shirt plzz choose the color and size')
        print()
        n=input('which color s u want please enter the red/blue/green :').lower()
        print()
          
        if n=='red':
            print(' thank you choose the ur feverate color:',n)
        elif n=='blue':
            print(' wow you choose the ur feverate color:',n)
        elif n=='green':
            print(' thank you choose the ur feverate color:',n)

        m=input('please choose the size s/m/xl').lower()
            
            
        if m=='s':
            print('you choosing ',n,' :color shirt and size :',m)
        elif m=='m':
            print('you choosing ',n,' :color shirt and size :',m)
        elif m=='xl':
            print('you choosing ',n,' :color shirt and size :',m)
            
            
            print()
            print('   please bill  total price of the shirt with discount')
            print()
        p=int(input('enter the total prize of the shirt :'))
        d=int(input('plzz enter a shirt discount percentage'))
        
        t=(d/100)* p
        final_price=p-t
        print('Original price:', p)
        print('Discount amount:', t)
        print()
        print('Final price after discount:', final_price)
        
        
    elif choose=='2':
        
        print('thank you for choosing pant plzz choose the color and size')
        print()
        n=input('which color s u want please enter the black/gray/light-blue :').lower()
        print()
          
        if n=='black':
            print(' thank you choose the ur feverate color:',n)
        elif n=='light-blue':
            print(' wow you choose the ur feverate color:',n)
        elif n=='gray':
            print(' thank you choose the ur feverate color:',n)

        m=input('please choose the size s/m/xl').lower()
            
            
        if m=='s':
            print('you choosing ',n,' :color pant and size :',m)
        elif m=='m':
            print('you choosing ',n,' :color pant and size :',m)
        elif m=='xl':
            print('you choosing ',n,' :color pant and size :',m)
            print()
            print('   please bill  total price of the pant with discount')
            print()
        p=int(input('enter the total prize of the pant :'))
        d=int(input('plzz enter a pant discount percentage'))
        
        t=(d/100)* p
        final_price=p-t
        print('Original price:', p)
        print('Discount amount:', t)
        print()
        print('Final price after discount:', final_price)
        
        
    elif choose=='3':
        
        print('thank you for choosing saree plzz choose the color and size')
        print()
        n=input('which colors u want please enter the green/lite-pink/light-blue :').lower()
        print()
          
        if n=='green':
            print(' thank you choose the ur feverate color:',n)
        elif n=='light-blue':
            print(' wow you choose the ur feverate color:',n)
        elif n=='lite-pink':
            print(' thank you choose the ur feverate color:',n)

        m=input('please choose the size s/m/xl').lower()
            
            
        if m=='s':
            print('you choosing ',n,' :color saree and size :',m)
        elif m=='m':
            print('you choosing ',n,' :color saree and size :',m)
        elif m=='xl':
            print('you choosing ',n,' :color saree and size :',m)
            print()
            print('   please bill  total price of the saree with discount')
            print()
        p=int(input('enter the total prize of the saree :'))
        d=int(input('plzz enter a saree discount percentage'))
        
        t=(d/100)* p
        final_price=p-t
        print('Original price:', p)
        print('Discount amount:', t)
        print()
        print('Final price after discount:', final_price)
        print()
    else:
        print('invalide please enter again')
    print()

    z=input('If u want to shopping again please enter yes/exit').lower()
    print()

    if z=='exit':
        print('thankyou  for your shopping have nice day!')
        
        break
    
    print()

#6. write a python program that simulates an ATM machine allowing user to check their balance and withdraw money?
print('      HI CAN I HELP U ')
while True:
    print('  ATM union bank of india')
    print()
    print('1.check balance')
    print('2.withdraw money')
    print('3.exit')
    print()
    blc=5000
    a=input('choose the option 1/2/3 :')
    if a=='1':
        print('your current balance is :',blc)
    elif a=='2':
        print('you choose the withdraw')
        n=int(input('how much money u want to withdraw'))
        if n>blc:
            print('insuffent')
        else:      
            f=blc-n
            print()
            print('your widthdraw money:',n)
            print()
            print('your remaining main balance is:',f)
    elif a=='3':
        print('Thank you for using Union Bank of India ATM!')
        break
    else:
        print('invalid number')
    m=input('if u want to continue please enter yes/no')
    if m=='no':
        print('thankyou using ATM have a nice day!')
        break

#7. write a python program that greets the user differentlybased on the time of day?
while True:
    
    n=int(input('enter the time: 0 to 24 hrs:'))

    if n>=4 and n<=12:
        print ('good morning')
    elif n>=13 and n<=16:
        print('good afternoon')
    elif n>=17 and n<=21:
        print('good evening')
    else:
        print('good night')
    m=input('if u want to wish again press yes/no').lower()
    if m=='no':
        print('thankyou have a grate wishes byee')
        break
   
#8. write a python program that calculates the finel price of an item after applying a discount coupon code?

print('1.tv')

choose=input('choose the option wt u want: 1:')
r=123456
cop=500
if choose=='1':
    print('your are choose the tv')
    n=int(input('enter the price '))
    
    m=int(input('enter the product discount percentage'))
    c=int(input('enter the coupon code'))
    if r==c:
        print('your coupon is verified and successfull added done rs:',cop)
    else:
        print('the coupon id is invalid')
        
        print()

    f=m/100*n
    
    blc=n-f
    total=blc-cop
    print()
    print('the product price =',n)
    print('the discount percentange =',f)
    print('coupon discount =',cop)
    print()
    print('total amount is=',total)
else:
    print('invalide')


#9. write a python program that calculates and prints the grade based on a given score but also validates input score?

score=int(input('enter a score run number 1 to 100'))

if score>=90 and score<=100:
    print('A grade')
elif score>=70 and score<=89:
    
    print('B grade')
elif score>=50 and score<=69:
    print('c grade')
elif score>=20 and score<=49:
    print('D grade')
elif score>=0 and score<=19:
    print('E grade score is low')
else:
    print('invalide score')

  
#10  write python program that determine the number of days in the given months?

n=input('enter a months name')

if n=='january' or n=='march' or n=='may' or n=='july':
    print('31 days in ',n)
elif n=='oct' or n=='december':
    print('31 days in',n)
elif n=='febuary':
    print('28 days in',n)

else:
    print('30 days in',n)
 
    
    
    


        
     















