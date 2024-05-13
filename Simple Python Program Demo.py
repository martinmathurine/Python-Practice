# Title: Basic Calculations, Variable Assignments, and Drawing Grids

# Calculations
print(1 + 1)  # Output: 2
print(2 - 1)  # Output: 1
print(2 / 2)  # Output: 1 (integer division in Python 2, floating-point division in Python 3)
print(2 * 2)  # Output: 4

# Variables
print('Hello, World!')  # Output: Hello, World!
name = "Martin"
print(name)  # Output: Martin
job = "student"
print(job)  # Output: student
experience = 4
print(experience)  # Output: 4
company = "GitHub"
print(company)  # Output: GitHub

# Constructing a message using variables
message = "My name is " + name + ", I am a " + job + " studying at " + company + " for " + str(experience) + " years."
print(message)  # Output: My name is Martin, I am a student studying at Middlesex University for 4 years.

# Function to draw a grid
def print_grid():
    print("+----+----+")
    print("|    |    |")
    print("|    |    |")
    print("|    |    |")
    print("|    |    |")
    print("+----+----+")

def repeat_grid():
    print_grid()
    print_grid()

# Calling the function to draw a grid
repeat_grid()