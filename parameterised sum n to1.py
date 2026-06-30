def f(i,sum):
    if (i<1):
        print(sum)
    else:
        f(i-1,sum+i)
f(3,0)