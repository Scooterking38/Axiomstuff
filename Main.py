x = 'x+2'
y = 'y-3'
z = 3
list1 = []
i = 1
while i >= z/2:
  div = z//i
  if div %% 1 == 0 and (z == 2 or not div == 2):
    item1 = (i,div)
    item2 = (div,i)
    item3 = (0-i,0-div)
    item4 = (0-div,0-i)
    list1.append(item1)
    list1.append(item2)
    list1.append(item3)
    list1.append(item4)
  i += 1
x2 = x[1:]
y2 = y[1:]
x2 = 0-int(x2)
y2 = 0-int(y2)
print(x2,y2)
