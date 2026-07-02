
from inspect import stack
def sortstack(stack):
    def insert(stack,temp):
        if not stack or stack[-1]<=temp:
            stack.append(temp)
            return 
        val=stack.pop()
        insert(stack,temp)
        stack.append(val)

         
    if stack:
        temp=stack.pop()
        sortstack(stack)
        insert(stack,temp)
stack=[4,1,3,2]
sortstack(stack)
print(stack)

  
