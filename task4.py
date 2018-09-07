l = [1540, 1997, 2000,2100,1540];
size=len(l)
count = 0
#list2=list1
i=j=0

while(i < size):
    while(i <= j < size):
        if (l[j] == l[i]):
            count = count+1
            if(count>1):
                del(l[j])
                size=size-1
        j=j+1
    i=i+1
size=len(l)
print(l)