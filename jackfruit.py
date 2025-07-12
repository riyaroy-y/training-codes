n=int(input())
x1=list(map(int,input().split()))
x2=list(map(int,input().split()))
limit=int(input())
x1.sort()
x2.sort(reverse=True)
wages=0
k=0
for i in range(n):
    k=x1[i]+x2[i]
    if k>limit:
        extra=k-limit
        wages=extra*100+wages
print(wages)
