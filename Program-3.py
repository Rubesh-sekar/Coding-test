# Series based on condition
# Using Python
a=int(input())
c=[]
for i in range(1,a*2):
    if i%2!=0:
        c.append(i)
if a%2==0:
    print(*c[:-1])
else:
    print(*c)
