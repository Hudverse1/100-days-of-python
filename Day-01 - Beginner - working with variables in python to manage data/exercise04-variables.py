# This program takes two inputs. The first input is stored in a variable called a.
# The second input is stored in a variable called b.
#
# Write a program that switches the values stored in the variables a and b.

a = input("Digit a number: ")
b = input("Digit another number: ")

c = a
a = b
b = c

print("a: " + a)
print("b: " + b)
