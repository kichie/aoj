i=input
N=int(i())
A=list(map(int,i().split()))
c=0
flug = 1
while flug:
    flug = 0
    for j in range(1,N)[::-1]:
        if A[j]<A[j-1]:
            A[j],A[j-1]=A[j-1],A[j]
            flug=1
            c+=1
print(*A)
print(c)
