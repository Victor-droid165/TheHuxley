def printMultiplos(i,f,x):
    for i in range(i,f+1):
        if i%x == 0:
            print(i)

i, f, x = int(input()), int(input()), int(input())
printMultiplos(i,f,x)
