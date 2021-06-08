# title here

title = "Smart Calculator"
print("It's me, ", title)

o = input('Enter operation: ')
b = int(input('b = '))
a = int(input('a = '))

print('a = ', a)
print('b = ', b)

if o == '+':
    print('a + b = ', a + b)
elif o == '-':
    print('a - b = ', a - b)
elif o == '/':
    if b != 0:
        print('a / b = ', a / b)
    else:
        print("Oops, division by zero")
else:
    print("I don't know what Tou want" )