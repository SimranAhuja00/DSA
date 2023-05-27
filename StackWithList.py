stack = []
 
# append() function used to push an element onto the stack
stack.append('Hello')
stack.append('Bonjour')
stack.append('Namaste')
 
print('Initial stack') #printing the current stack
print(stack)
 
# pop() function to pop an element from stack in LIFO order
print('\nElements popped from stack:')
print(stack.pop()) #returns the popped element
print(stack.pop())
 
print('\nStack after elements are popped:')
print(stack)
 
