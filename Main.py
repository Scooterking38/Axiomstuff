x = input('enter 1st clause eg x+2: ')
y = input('enter 2nd clause eg y-3: ')
z = int(input('enter result: '))
i, list1 = 1, []

if '+' in x: var1, num1 = x.split('+')
elif '-' in x: var1, num1 = x.split('-')
    num1 = '-' + num1
if '+' in y: var2, num2 = y.split('+')
elif '-' in y: var2, num2 = y.split('-')
    num2 = '-' + num2

# factors
while i <= abs(z):
    if z % i == 0:
        d = z // i
        list1.extend([(i, d),
                      (-i, -d)])
    i += 1

#output
for a, b in list1:
    print(var1 + ': ' + str(a + int(num1)), var2 + ': ' + str(b + int(num2)))
