# Write your solution here
# Let's take the square root of math-module in use
from math import sqrt

# Note that the square root can also be calculated using power.
# sqrt(9) is equivalent to 9 ** 0.5

# Please write a program for solving a quadratic equation of the form ax²+bx+c. The program asks for values a, b and c. It should then use the quadratic formula to solve the equation. 

# The solution:
# x = (-b +- sqrt(b**2 - 4*a*c)) / (2*a)

a = int(input("Value of a: "))
b = int(input("Value of b: "))
c = int(input("Value of c: "))

# discriminant = b**2 - (4 * a * c)
# discriminant is the part under the square root
# if discriminant < 0: 
#     print("No real roots")

s1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
s2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)

print(f"The roots are {s1} and {s2}")
