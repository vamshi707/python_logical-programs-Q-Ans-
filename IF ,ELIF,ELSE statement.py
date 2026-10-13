# IF ,ELIF,ELSE statement

#wtite a python program that converts a temperature in calsius to fahrenheit or vice versa based in user input?
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

 

    
    














