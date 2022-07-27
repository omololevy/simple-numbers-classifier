print('THIS PROGRAM REQUEST A LIST OF NUMBERS FROM A USER AND SORTS THEM AS:\n * EVEN.\n * ODD.\n * PRIME.')
size = int(input("Enter the size of your list (i.e a list of size 5 will have five numbers, e.g [20, 2, 70, 4, 63])\n"))
your_list=[]
first_value = int(input('Enter the first number in the list\n'))
your_list.append(first_value)
while len(your_list) < size:
    another_value = int(input('Enter the next number\n'))
    your_list.append(another_value)
    print(your_list)
    odd = []
    even = []
    prime = []
for i in your_list:
    alarm = False
    if int(i)>1:
        for x in range(2, int(i)):
            if int(i)%x == 0:
                alarm = True
                break
        if alarm:
            pass
        else:
            prime.append(i)
    if int(i) % 2 == 0:
        even.append(i)
        
    else:
        odd.append(i)
if len(even) < 2:
    print('Even number is ', len(even)) 
    print('It is ', even)
else:  
    print('Even numbers are ', len(even))
    print('They are: ', even)
if len(odd) < 2:
    print('Odd number is ', len(odd))
    print('It is ', odd) 
else:  
    print('Odd numbers are ', len(odd))
    print('They are: ', odd)
if len(prime) < 2:
    print('Prime number is ', len(prime)) 
    print('It is ', prime)
else:  
    print('Prime numbers are ', len(prime))
    print('They are: ', prime)
