def MDC(A,D):
    if A%D != 0:
        D = MDC(D, A%D)
    return D

N = int(input())
for i in range(N):
    A,D = [int(i) for i in input().split()]
    mdcAD = MDC(A,D)
    print(f"MDC({A},{D}) = {mdcAD}")
