num1 = int(input("enter num1 : "))
num2 = int(input("enter num1 : "))
operater = input("enter operater ")
if operater == '+' :
  result = num1+num2
elif operater == '-' :
  result = num1-num2
elif operater == '*' :
  result = num1*num2
elif operater == '/' :
  if num2 == 0:
    print("Error: Division by zero")
  else:
    result = num1/num2
else:
    print("Error: invalid operater")
print(f"result= {result}")

if result > 0:
  print("result is positive")
elif result < 0:
  print("result is negative")
else:
  print("result is zero ")