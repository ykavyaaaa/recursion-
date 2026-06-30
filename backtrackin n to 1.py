def f(i,n):
    if i>n:
        return
    else:
        f(i+1,n)
        print(i)
n=5
f(1,n)