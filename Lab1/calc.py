
# define a method
def say_hello():
    print("Hello from a method")

def sum (op1, op2):
    return op1 + op2

def sub (op1, op2):
    return op1 - op2

def mul (op1, op2):
    return op1 * op2

def div (op1, op2):
    return op1 / op2


def menu():
  print(" Menu ")
  print("[1] - Sum")
  print("[2] - Subtract")
  print("[3] - Multiply")
  print("[4] - Divide")
  print("[x] - EXIT")


print("-" * 30)
print("Welcome to PyCalc")
print("-" * 30)

opc = ""
while(opc != "x"):

  menu()
  opc = input("Select an option: ")
  if(opc == "x"): 
    break #Break the loop

  num1 = float(input("First number: "))
  num2 = float(input("Second number: "))

  if(opc == '1'):
      sum_res = sum(num1, num2)
      print("Sum = " + str(sum_res))

  elif(opc == '2'):
      sub_res = sub(num1, num2)
      print("Subtract = " + str(sub_res))

  elif(opc == '3'):
      mul_res = mul(num1, num2)
      print("Multiply = " + str(mul_res))

  elif(opc == '4'):
      div_res = div(num1, num2)
      print("Divide = " + str(div_res))

  ##elif(opc == '2'):
  ##sub_res == subtract(num1, num2)
  ##print("Subtract = " + str(sub_res))

  input("Press Enter to go back")

print(" Thank you for using PyCalc, Good Bite!!!!!")
