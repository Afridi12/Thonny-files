import sys
class Stack:
    def __init__(self):
        self.__S = []
    #Display the Stack
    def __str__(self):
        return str(self.__S)
    #Add a new element to top of stack
    def push(self,x):
        self.__S.append(x)
    #Remove the top element from stack
    def pop(self):
        return self.__S.pop()
    #See what element is on top of stack
    #Leaves stack unchanged
    def top(self):
        return self.__S[-1]

def postFix(exp):
    for y in range(exp.length):
        if y == '-':
            
        
        

if __name__ == "__main__":
    print('Welcome to Postfix Calculator')
    print('Enter exit to quit.')
    exp = input('Enter Expression:\n')
    
    
    

    
