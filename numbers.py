print('THIS PROGRAM REQUESTS A LIST OF NUMBERS FROM YOU AND SORTS THEM AS:\n * EVEN.\n * ODD.\n * PRIME.')
size = int(input("Enter the size of your list (i.e a list of size 5 will have five numbers, e.g [20, 2, 70, 4, 63])\n"))
your_list=[]
first_value = int(input('Enter the first number in the list: '))
your_list.append(first_value)
while len(your_list) < size:
    another_value = int(input('Enter the next number: '))
    your_list.append(another_value)
    print(your_list)
    odd = []
    even = []
    prime = []
for i in your_list:
    alarm = False
    if i>1:
        for x in range(2, i):
            if i%x == 0:
                alarm = True
                break
        if alarm:
            pass
        else:
            prime.append(i)
    if i % 2 == 0:
        even.append(i)
        
    else:
        odd.append(i)
    even_count = len(even)
    odd_count = len(odd)
    prime_count = len(prime)
print('\n************SOLUTION************')
print(f'The list is {your_list} of size {size}\n')
if even_count < 2:
    print(f'Even number is {even_count}: {even}\n') 
else:  
    print(f'Even numbers are {even_count}: {even}\n') 
if odd_count < 2:
    print(f'Odd number is {odd_count}: {odd}\n')
else:  
    print(f'Odd numbers are {odd_count}: {odd}\n')
if prime_count < 2:
    print(f'Prime number is {prime_count}: {prime}\n')
else:  
    print(f'Prime numbers are {prime_count}: {prime}\n')
