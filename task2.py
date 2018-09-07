def printme( l ):
   ls=''
   size=len(l)
   i=0
   while (i<size):
       l1=str(len(l[i]))
       if(len(l1)>len(ls)):
           ls=l1
       i=i+1
   print(size)
   print(ls)
   return
printme(['physics', 'chemistryoisdfg', 'dentistiryt', 'beautifull'])
