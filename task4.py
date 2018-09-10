def remove_duplication(l):
    """Removes those stringd which are repeated"""
    size=len(l)
    i=j=count = 0
    while(i < size):
        while(i <= j < size):
            if (l[j] == l[i]):
                count = count+1
                if(count >1):
                    del(l[j])
                    size=size-1
            j=j+1
        i=i+1
    size=len(l)
    print(l)
    return
l = [1540, 1997, 2000,1999,1540];
remove_duplication(l)