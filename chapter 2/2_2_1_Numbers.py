
# calculator.py
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
# handle division by zero
if b != 0:
    print("Quotient:", a / b)
else:
    print("Cannot divide by zero.")
