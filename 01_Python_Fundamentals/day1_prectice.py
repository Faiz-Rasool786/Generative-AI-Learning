# exercise 1.1
print("Hello, AI World!")

# exercise 1.2
x = 7
y = 9
print(x + y, x * y, x -y, x / y)

# exercise 1.3
x = int(input("Enter your number: "))
print("You entered:", x*2, x*3)

# exercise 1.4
for i in range(1, 21):
    print(f'loop iteration: {i}')
    
#exercise 1.5
print("Even numbers:")
for i in range(1, 50):
    if i % 2 == 0:
        print(i)

# exercise 1.6
print("Odd numbers:")
for i in range(1, 50):
    if i % 2 != 0:
        print(i)

# exercise 1.7
y = int(input("Enter a number to compute its factorial: "))
factorial = 1
for i in range(1, y + 1):
    factorial *= i
print(f'Factorial of {y} is: {factorial}')

# exercise 1.8
a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))
print(f'Sum: {a + b}, Product: {a * b}, Difference: {a - b}, Division: {a // b}')

# exercise 1.9
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = float(input("Enter temperature in Fahrenheit: "))

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

print(f'{celsius} Celsius is {celsius_to_fahrenheit(celsius)} Fahrenheit')
print(f'{fahrenheit} Fahrenheit is {fahrenheit_to_celsius(fahrenheit)} Celsius')

# exercise 1.10
number = 5
for i in range(1, 11):
    print(f'{number} x {i} = {number * i}')

# exercise 1.11
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True