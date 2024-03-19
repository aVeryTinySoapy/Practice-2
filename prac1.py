x = input('Enter the first number: ')
y = input('Enter the second number: ')

lim = input('Enter Limit: ')
result = 0
for i in range(0,int(lim)):
    if i%int(x) == 0 or i%int(y) == 0:
        result += i

print (f"The sum of multiples of {x} or {y} up to {lim} is {result}.")