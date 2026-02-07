x = input('enter 1st clause eg x+2: ')
y = input('enter 2nd clause eg y-3: ')
z = int(input('enter result: '))
i,list1 = 1,[]

if '+' in x:
  test = x.split('+')
  var1 = test[0]
  num1 = '-'.join(test[1])
elif '-' in x:
  test2 = x.split('-')
  var2 = test2[0]
  num2 = test2[1]
  



#factors
while i <= z//2:
  d = z//i
  if d % i == 0 and (z == 2 or not d == 2):
    i1,i2,i3,i4 = (i,d),(d,i),(0-i,0-d),(0-d,0-i)
    list1.extend([i1,i2,i3,i4])
  i += 1
for i in list1:
    print(var1+': '+(i[0] + int(num1)), var2+': '+(i[1] + int(num2))
