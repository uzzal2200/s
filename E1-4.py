# Program to calculate GCD using Euclidean Algorithm

def gcd(a, b):
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    return a

# Taking input from user
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("GCD of", x, "and", y, "is:", gcd(x, y))
