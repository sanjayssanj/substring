a=[]
a=input("enter string")
h=0
for i in range(0,len(a)):
    h=h+1
    j=0
    while(a[i]==a[j+1]):
        j=j+1
        h=h-1
        break;
print(h)
