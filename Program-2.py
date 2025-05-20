# Odd Number Series
# Using Python
a=int(input())
c=[]
for i in range(1,2*a):
    if i%2!=0:
        c.append(i)
print(*c)
