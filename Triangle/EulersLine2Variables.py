import math
import random

A = input("Please enter a Number: ")
B = input("Please enter a Number: ")

a = int(A)
b = int(B)

# Orthocentre
Orthocentre_x = a
Orthocentre_y = a / b - pow(a, 2) / b

print(f"Orthocentre x is: {Orthocentre_x}")
print(f"Orthocentre y is: {Orthocentre_y}")

# Centroid
Centroid_x = (a + 1) / 3
Centroid_y = b / 3

print(f"Centroid x is: {Centroid_x}")
print(f"Centroid y is: {Centroid_y}")

# Circumcentre
Circumcentre_x = 0.5
Circumcentre_y = (pow(a, 2) + pow(b, 2) - a) / (2 * b)

print(f"Circumcentre x is: {Circumcentre_x}")
print(f"Circumcentre y is: {Circumcentre_y}")

m = (pow(b, 2) - 3 * a + 3 * pow(a, 2)) / (b * (-2 * a + 1))
y_1 = m * -a
c = y_1 + (a - pow(a, 2)) / b

print(f"The equation of the Eulerian Line is: {m}x + {c}")








