def factorial(n):
    """
    Calculate the factorial of a number using recursion.
    
    Args:
    - n (int): The number whose factorial is to be calculated
    
    Returns:
    - int: The factorial of the given number
    """
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: factorial of n is n times factorial of (n-1)
    else:
        return n * factorial(n - 1)

# Example usage:
num = 5
print("Factorial of", num, "is:", factorial(num))
