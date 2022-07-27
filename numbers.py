print('THIS PROGRAM REQUEST A LIST OF NUMBERS FROM A USER AND SORTS THEM AS:\n * EVEN.\n * ODD.\n * PRIME.')
size = int(input("Enter the size of your list (i.e a list of size 5 will have five numbers, e.g [20, 2, 70, 4, 63])\n"))
your_list=[]
first_value = (input('Enter the first number in the list\n'))
your_list.append(first_value)
while len(your_list) < size:
    another_value = input('Enter the next number\n')
    your_list.append(another_value)
    print(your_list)
    odd = []
    even = []
    prime = []
