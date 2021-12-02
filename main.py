#Calculator
from art import logo

#Add
def add(n1,n2):
  return n1 + n2

#Substract
def subtract(n1,n2):
  return n1 - n2

#Multiply
def multiply(n1,n2):
  return n1 * n2

#Divide
def divide(n1,n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

def calculator():
  print(logo)
  should_continue = True
  num1 = float(input("Whats the first number?: "))

  while should_continue:
    print("Select your operation:")
    for op in operations:
      print(op)
    operation = input("Selection: ")

    num2 = float(input("Whats the second number?: "))

    calculation_function = operations[operation]
    answer = calculation_function(num1, num2)

    print(f"{num1} {operation} {num2} = {answer}")
    if input(f"Type 'y' to keep working with {answer}, type 'n' to start a new calculation: ") == "y":
      num1 = answer
    else:
      should_continue = False
      calculator()

calculator()
