
from inspect import stack

def f(i,n):
   while(i<len(n)-1):
        if(n[i]<n[i+1]):
         temp=n[i]
         n[i]=n[i+1]
         n[i+1]=temp
         f(0,n)
        i+=1
n=stack=[]
stack.append(6)
stack.append (4)
stack.append (7)
stack.append (8)
stack.append (1)
f(0,n)
print(n)
