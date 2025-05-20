#Count of Multiples
#Using Python
a=list(map(int,input().split()))
c=[]
for i in range(1,10):
    r=0
    for j in a:
        if j%i==0:
            r+=1
    c.append((i,r))
d=dict(c)
print(d)
