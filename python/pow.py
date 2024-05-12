class PowerCalculator:
    def pow(self, x, n):
        """
        Calculate the power of a number.
        
        Args:
        - x (int or float): The base
        - n (int): The exponent
        
        Returns:
        - int or float: The result of x raised to the power of n
        """
        if n == 0:
            return 1
        elif n < 0:
            return 1 / self.pow(x, -n)
        elif n % 2 == 0:
            return self.pow(x * x, n // 2)
        else:
            return x * self.pow(x, n - 1)

# Example usage:
calculator = PowerCalculator()
base = 2
exponent = 3
result = calculator.pow(base, exponent)
print(f"{base} raised to the power of {exponent} is:", result)
