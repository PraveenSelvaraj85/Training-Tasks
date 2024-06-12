s=input()
lower=0
upper=0
for i in range(1,len(s)):
    if s[i].islower():
        lower+=1
    else:
        upper+=1
if upper>lower:
    print(s.upper())
else:
    print(s.lower())