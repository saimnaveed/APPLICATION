a='add'
length=(len(a))
print(length)
i=0
if(length>3):
    for i in range (length):

      if a[length-3:length]=='ing':
           b=a+'ly'
      else:
           b=a+'ing'
      break
else:
    b=a
print(b)
