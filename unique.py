s= input("Enter a String:")
d={}
for i in s:
    d[i]=0
for i in s:
    d[i]=d[i]+1
    for i in s:
        if(d[i] == 1):
           
            print(i)