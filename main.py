#task1 User input, code output
name = input("Enter your name please: ")
salary = input("Enter your desired salary level:")
if not salary.isdigit():
    print(f"{name}, please enter your desired salary as a digit.")
else:
    taxLevel = int(int(salary) * 0.2)
    print(f"{name}, the tax level you will pay with the salary {salary} is {taxLevel}")

#task2 Using arithmetic, bitwise and logic ops
Addition = lambda a, b : a + b
Multiplication = lambda a, b : a * b
Division = lambda a, b : a / b
Exponentiation = lambda a, b : a ** b
operation = int(input())
print("Please enter two numbers for addition, comma separated")
numbers = input().split(", ")
numbers = [int(i) for i in numbers]
if operation == 1:
    print(Addition(numbers[0], numbers[1]))
elif operation == 2:
    print(Multiplication(numbers[0], numbers[1]))
elif operation == 3:
    print(Division(numbers[0], numbers[1]))
elif operation == 4:
    print(Exponentiation(numbers[0], numbers[1]))
else:
    print("Incorrect Input")

#task3 Loops and iterations
print ("Please enter the length of Fibonacci sequence")
n = int(input())
print (f"the Fibonacci sequence for {n} is")
n1 = 1
n2 = 2
print (n1, end=', ')
for i in range(1, n):
    if i == n-1:
        print(n2)
    else:
        print(n2, end=', ')
    x = n2
    n2 = n1 + n2
    n1 = x

#task4 Tuples and sets
unique = set()
noUnique = {}
print("Please chose the task you want to perform:")
print("1. Enter items")
print("2. Exit")
operation = int(input())
while operation != 2:
    if operation == 1:
        print("Please enter items separated by comma")
        arr = input().lower().split(", ")
        for i in arr:
            if i in unique:
                noUnique[i] = noUnique.get(i, 0) + 1
            else:
                unique.add(i)
        print("Items are saved")
        noUnique = tuple(((i, cnt) for (i, cnt) in noUnique.items()))
        print("Unique items:", unique)
        print("Not unique items: ", noUnique)

#task5 Lists and dictionaries
 print("Please chose the task you want to perform:")
    print("1. Enter items")
    print("2. Exit")
    operation = int(input())