start=int(input("Enter"))
end=int(input("End"))
for i in range(start,end+1):
    while  i>0:
        if i%10==4:
            print(i)
        i=i//10