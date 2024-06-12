def factorial(n):
    fact=1
    if n==1:
        return 1
    else:
        for i in range(1,n+1):
            fact*=i
        return fact
def reversed(n):
    rev=0
    while n>0:
        rev=rev*10+n%10
        n//=10
    if rev%2==0:
        return factorial(rev)
    else:
        return -1
n=int(input())
print(reversed(n))
