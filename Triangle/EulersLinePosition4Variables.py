import math
import random

A = 2#input("Please enter a Number: ")
B = 2#input("Please enter a Number: ")
C = 1#input("Please enter a Number: ")
D = 0#input("Please enter a Number: ")

a = int(A)
b = int(B)
c = int(C)
d = int(D)

# Orthocentre
Orthocentre_x = a#(-d + b + a * c * (1 / d - 1 / b)) / (-a / b + c / d)
Orthocentre_y = (a-a**2)/b

print(f"Orthocentre x is: {Orthocentre_x}")
print(f"Orthocentre y is: {Orthocentre_y}")

# Centroid
Centroid_x = ((-b*(pow(c,2))) + (d*a*c) + (d*(pow(a,2))) - (b*a*c)) / (3*d*a - 3*b*c)
Centroid_y = (((2 * b - d) / (2 * a - c)) * Centroid_x) - (((2 * b - d) * c) / (2 * (2 * a - c))) + d / 2

print(f"Centroid x is: {Centroid_x}")
print(f"Centroid y is: {Centroid_y}")

# Circumcentre
Circumcentre_x = (pow(c,2)*b - d*pow(a,2) - d*pow(b,2) +pow(d,2)*b) / (2*(c*b - a*d))
Circumcentre_y = ((-a / b) * Circumcentre_x) + ((a**2) / (2 * b)) + (b / 2)

print(f"Circumcentre x is: {Circumcentre_x}")
print(f"Circumcentre y is: {Circumcentre_y}")
