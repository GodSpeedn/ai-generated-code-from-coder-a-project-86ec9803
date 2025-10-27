import math

class ScientificCalculator:
    """
    A scientific calculator class providing basic arithmetic, trigonometric,
    and advanced mathematical functions.
    """

    def add(self, a, b):
        """
        Adds two numbers.
        Args:
            a (float or int): The first number.
            b (float or int): The second number.
        Returns:
            float or int: The sum of a and b.
        """
        return a + b

    def subtract(self, a, b):
        """
        Subtracts the second number from the first.
        Args:
            a (float or int): The first number (minuend).
            b (float or int): The second number (subtrahend).
        Returns:
            float or int: The difference of a and b.
        """
        return a - b

    def multiply(self, a, b):
        """
        Multiplies two numbers.
        Args:
            a (float or int): The first number.
            b (float or int): The second number.
        Returns:
            float or int: The product of a and b.
        """
        return a * b

    def divide(self, a, b):
        """
        Divides the first number by the second.
        Args:
            a (float or int): The numerator.
            b (float or int): The denominator.
        Returns:
            float: The quotient of a and b.
        Raises:
            ValueError: If b is zero (division by zero).
        """
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    def sin(self, x):
        """
        Calculates the sine of an angle (in radians).
        Args:
            x (float or int): The angle in radians.
        Returns:
            float: The sine of x.
        """
        return math.sin(x)

    def cos(self, x):
        """
        Calculates the cosine of an angle (in radians).
        Args:
            x (float or int): The angle in radians.
        Returns:
            float: The cosine of x.
        """
        return math.cos(x)

    def tan(self, x):
        """
        Calculates the tangent of an angle (in radians).
        Args:
            x (float or int): The angle in radians.
        Returns:
            float: The tangent of x.
        """
        return math.tan(x)

    def sqrt(self, x):
        """
        Calculates the square root of a number.
        Args:
            x (float or int): The number.
        Returns:
            float: The square root of x.
        Raises:
            ValueError: If x is negative.
        """
        if x < 0:
            raise ValueError("Cannot calculate square root of a negative number.")
        return math.sqrt(x)

    def power(self, base, exp):
        """
        Calculates the base raised to the power of the exponent.
        Args:
            base (float or int): The base number.
            exp (float or int): The exponent.
        Returns:
            float: The result of base^exp.
        """
        return math.pow(base, exp)

    def log(self, x, base=math.e):
        """
        Calculates the logarithm of a number to a given base.
        Defaults to natural logarithm (base e).
        Args:
            x (float or int): The number.
            base (float or int, optional): The base of the logarithm. Defaults to math.e.
        Returns:
            float: The logarithm of x to the specified base.
        Raises:
            ValueError: If x is non-positive or base is non-positive or equal to 1.
        """
        if x <= 0:
            raise ValueError("Logarithm is not defined for non-positive numbers.")
        if base <= 0 or base == 1:
            raise ValueError("Logarithm base must be positive and not equal to 1.")
        return math.log(x, base)