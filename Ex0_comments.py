# -------------------------------------------
# Exercise 0: Comments Practice
# -------------------------------------------
# In this exercise, you'll practice writing clear, helpful comments
# to explain Python code.
#
# Good comments should:
# - Explain WHAT the code does (not just repeat it)
# - Be clear and concise
# - Help someone else understand your code
#
# Below you'll find several code snippets.
# Add comments to explain what each section does.
# -------------------------------------------

# -------------------------------------------
# Task 1: Shopping Cart
# -------------------------------------------
print("-------------------------------------------\n"
      + "Task 1: Shopping Cart\n"
      + "-------------------------------------------")

# Add comments to explain this code:
# create a list called variable cart and containing items apple, bread, milk, eggs
cart = ["apple", "bread", "milk", "eggs"]
# give the total items in the list given length of items in variable cart
total_items = len(cart) # give the total items in the list given length of items in cart
# this line refer to printing the total number of items in the cart
print(f"You have {total_items} items in your cart")
#using a for loop create print out each item in the cart
for item in cart:
    print(f"- {item}")

# -------------------------------------------
# Task 2: Grade Calculator
# -------------------------------------------
print("-------------------------------------------\n"
      + "Task 2: Grade Calculator\n"
      + "-------------------------------------------")
#create a heading giving what the Task entails, "Task 2: Grade Calculator\n"
# Add comments to explain this code:
# create a variable called 'score'. It is an integer. Ask the user to 'Enter your test score'
score = int(input("Enter your test score: "))
# create if, else statements about score and grade. The passing grade is greater than or equal to a mark of 70. 
# if the score is greater than or equal to 70 this grade is a pass mark. If not it is a fail.
if score >= 70:
    grade = "Pass"
else:
    grade = "Fail"
#please print "Your grade"
print(f"Your grade: {grade}")

# -------------------------------------------
# Task 3: Password Validator
# -------------------------------------------
print("-------------------------------------------\n"
      + "Task 3: Password Validator\n"
      + "-------------------------------------------")
#print a task entitled 'Task 3: Password Validator\n'
# Add comments to explain this code:
# create a variable called password. Ask the user to create a password.
password = input("Create a password: ")
# create a variable for password. It is considered to be valid if: 
# length of password has to be greater than or equal to 8 characters
# there is at least 1 upper case letter
# there is at least 1 lower case letter
is_long = len(password) >= 8
has_upper = password != password.lower()
has_lower = password != password.upper()
#use .lower()
#use .upper()
is_valid = is_long and has_upper and has_lower
# if the password is valid then print 'Password accepted!' 
if is_valid:
    print("Password accepted!")
else:
    print("Password rejected. Must be 8+ characters with upper and lowercase letters.")
# else print 'Password rejected. Must be 8+ characters with upper and lowercase letters.")
# -------------------------------------------
# Task 4: Even Number Counter
# -------------------------------------------
print("-------------------------------------------\n"
      + "Task 4: Even Number Counter\n"
      + "-------------------------------------------")
# create a title called 'Task4: Even Number Counter\n'
# Add comments to explain this code:
#create a variable called numbers and make a list of numbers.
# remember list uses []
numbers = [12, 7, 18, 5, 22, 9, 14]
even_count = 0
#you are trying to find even numbers in the list of numbers
# increase the count by 1 (ascending) when an even number is found such that no even numbers are left
for num in numbers:
    if num % 2 == 0:
        even_count = even_count + 1

print(f"There are {even_count} even numbers in the list")
# when an even number is found print 'There are even numbers in the list'
# -------------------------------------------
# Task 5: Student Records
# -------------------------------------------
print("-------------------------------------------\n"
      + "Task 5: Student Records\n"
      + "-------------------------------------------")

# Add comments to explain this code:
# create a heading called 'Task 5: Student Records\n'
# create a dictionary called 'student'. 
#remember to use the curly bracers for dictionaries {} to enclose the entire keys, values
#create keys called 'name', 'age', 'grades'. place the grades inside a list remembering to use [] brackets
#find the average of the student grades divided by the length of the student grades
#round up the total by 2 decimal places
#print the student name, student, age, average grade
student = {
    "name": "Alice",
    "age": 20,
    "grades": [85, 92, 78, 88]
}

average = sum(student["grades"]) / len(student["grades"])
average = round(average, 2)

print(f"Student: {student['name']}")
print(f"Age: {student['age']}")
print(f"Average grade: {average}")

# -------------------------------------------
# Task 6: Countdown Timer
# -------------------------------------------
print("-------------------------------------------\n"
      + "Task 6: Countdown Timer\n"
      + "-------------------------------------------")

# Add comments to explain this code:
#create a heading called 'Task 6: Countdown Timer\n'
#create a while loop using a countdown (descending). The countdown commences at 5.
#remember to initialise the countdown
#print the number countdown e.g. 5,4,3,2,1
#print 'Blast off!' when the countdown has ended
countdown = 5

while countdown > 0:
    print(countdown)
    countdown = countdown - 1

print("Blast off!")

# -------------------------------------------
# Task 7: Menu Formatter
# -------------------------------------------
print("-------------------------------------------\n"
      + "Task 7: Menu Formatter\n"
      + "-------------------------------------------")

# Add comments to explain this code:
#create a list of items. use the variable name 'menu_items'
menu_items = ["burger", "pizza", "salad", "pasta"]
counter = 1

for item in menu_items:
    formatted_item = item.upper()
    print(f"{counter}. {formatted_item}")
    counter = counter + 1

# -------------------------------------------
# Submitting Your Work
# -------------------------------------------
# Once you've added comments to all tasks:
# 1. Save your file
# 2. Open the terminal
# 3. Use Git to:
#    - Stage your changes
#    - Commit your changes
#    - Push your changes to the external repository
# Optional: Check GitHub to confirm your changes appear.
# -------------------------------------------
