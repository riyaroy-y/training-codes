N,D=map(int,input().split())
s=0
w=list(map(int,input().split()))
w.sort(reverse=True)
for i in range(D):
    s=w[i]+s
    
print(s)
