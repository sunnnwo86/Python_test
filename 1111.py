a = [0,1,4,3]
a.sort()
print(a)
i=enumerate(a)
# print(list(i))
# print([len(a)-1])
b=len(a)
c = range(b)    
c = list(c)
f=0
while f <= len(a):
    if a[f] != c[f]:
        print(c[f],"아닙니다")
        break
    elif a == c:
        print(max(a)+1)
        break
    f += 1