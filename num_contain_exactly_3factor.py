def three_factor(n):
    root=0
    i=1
    while i*i<=n:
        if i*i==n:
            root=i
            break
        i+=1
    if root==0:
        return False
    if root<2:
        return False
    for i in range(2,root):
        if root%i==0:
            return "not three factor"
        
    return "exactly three factor"
    
n=int(input("enter the number"))
print(three_factor(n))