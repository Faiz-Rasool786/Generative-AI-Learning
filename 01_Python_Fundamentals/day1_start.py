# Day 1: Python Basics
print('Hello, Faizi! Welcome to your Genrative AI Journey! 🚀')

# --- Variables and Math ---
x = 10
y = 5
print (f'Sum: {x + y}, Difference: {x - y}, Product: {x * y} , Quotient: {x / y}, Division: {x // y}, Modulus: {x % y}, Exponent: {x ** y}')

# --- Loops Example ---
for i in range(1, 6):
    print(f'Loop iteration: {i}')
    
# --- Function Example ---
def factorial(n):
    results = 1
    for i in range(1, n + 1):
        results *= i
    return results
print(f'Factorial pf 5 is: {factorial(5)}')