def printme( l ):
    """Returns the size of largest string found in the list"""
    ls=''
    SIZE=len(l)
    i=0
    while (i<SIZE):
      l1=str(len(l[i]))
      if(len(l1)>len(ls)):
          ls=l1
      i=i+1
    print(ls)
    return
printme(['physics', 'chemistryoisdfg', 'dentistiryt', 'beautifull'])
