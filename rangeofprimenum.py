def prime(n):
    if n < 2:
        return False
    else:
        for i in range(2,n):
            if n%i==0:
                return False
            return True
s=int(input("start value"))
e=int(input("end value"))
def prime_range(s,e):
    prime_num=[]
    for n in range(s,e):
        if prime(n):
            prime_num.append(n)
    min_num=min(prime_num)
    max_num=max(prime_num)
    sum=min_num+max_num
    print(sum)
prime_range(s,e)