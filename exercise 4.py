# Question 1: Using a for loop with a list

# TODO: Create a list of fruits
fruits = ["stawberry", "bluberry", "kiwi", "grape", "peach"]

# TODO: Use a for loop to print each fruit in the list
for fruit in fruits: 
  print(fruit)

#-------------------------------------------------------------------------
# Question 2: Using a while loop for countdown

# TODO: Use a while loop to create a countdown from 5 to 1
count = 5 
while count >= 1:
   print(count)
   count -= 1

#-------------------------------------------------------------------------
# Question 3: Using a for loop with range()

# TODO: Use a for loop to print the first 10 square numbers
for i in range(1, 11):
   print(i ** 2)

#-------------------------------------------------------------------------

# Question 4: Using the random module

# TODO: Import the random module
import random 
# TODO: Create a list of colors
colors = ["orange", "red", "blue", "green", "purple"]
# TODO: Use a for loop to select and print 3 random colors from the list
for _ in range(3):
 print(random.choice(colors))
#-------------------------------------------------------------------------
# Question 5: Creating and using a custom module

# TODO: Create a new file named 'math_operations.py' with the following content:
"""
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"
"""

# TODO: Import the custom module and use its functions
import maths_operations

# TODO: Use a while loop to create a simple calculator
while True:
   import maths_operations
   
   print(" simple calculator ")
   print("1. add")
   print("2. subtract")
   print("3. multiply")
   print("4. divide")
   print("5. exit")

choice = input("choose operation(1-5): ")
if choice == '5':
   print("exiting calculator. Goodbye!")

if choice not in ['1', '2', '3', '4']:
  a = float(input("enter first number: "))
  b = float(input("enter second number: "))

if choice == '1':
   print(f"result:{math_operations.add(a, b)}")
elif choice == '2':
   print(f"result:{math_operations.subtract(a, b)}")
elif choice == '3':
   print(f"result:{math_operations.multiply(a, b) }")
elif choice =='4':
   print(f"result:{math_operations.divide(a, b)}") 
else:
   print("invalid choice. try again.")