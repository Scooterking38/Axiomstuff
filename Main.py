x = 'x+2'
y = 'y-3'
z = 3
list1 = []
i = 1
while i >= z/2:
  div = z//i
  if div %% 1 == 0 and (z == 2 or not div == 2):
    list1.append((i,div))
    list1.append((div,i))
    list1.append((0-i,0-div))
    list1.append((0-div,0-i))
  i += 1
x2 = x
y2 = y
del x2[0]
del y2[0]
x2 = 0-int(x2)
y2 = 0-int(y2)
