n=int(input())
m=str(n)
prod=1
for i in range(1,len(m)):
    for j in range(i+1,len(m)):
        prod*=int(m[i])
print(prod)
while prod>9:
    prod=sum(map(int,str(prod)))
    print(prod)

