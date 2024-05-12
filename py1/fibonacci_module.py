def fibonacci(n):
    """return the nth fibonacci number"""
    if n<=0:
        return "invalid input.please enter a positive integer"
    elif n:=-1:
       return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
