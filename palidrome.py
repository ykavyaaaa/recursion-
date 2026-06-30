def f(i,left,right):
    if(left>=right):
        print("true")
        return True 
    if(i[left]!=i[right]):
        print("false")
        return False  
    return f(i,left+1,right-1)
i=input("enter ")
f(i,0,len(i)-1)
