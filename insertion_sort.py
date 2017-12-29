N = int(input())
A = list(map(int,input().split()))
print( *A )
# 1-Nまで
for i in range(1,N):

    v = A[i]
    j = i - 1
    # 前の値の方が大きかったら入れ替える
    while j >= 0 and A[j] > v :
        A[j + 1] = A[j]
        j -= 1
    A[j + 1] = v
    print( *A )
