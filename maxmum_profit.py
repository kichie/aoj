import sys
i=input
n = int(i())
r0 = int(i())
r1 = int(i())
mx = r1-r0
mn = min(r1,r0)
for i in map(int,sys.stdin.readlines()):
    a=i-mn
    if mx<a:
        mx=a
        if 0>a:mn=i
    elif mn>i:mn=i
print(mx)
