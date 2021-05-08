num1 = int(input("What is the first number? "))
num2 = int(input("What is the second number? "))
print("Possible Signs: Addition(+), Subtraction(-), Division(/), Mulitplication(*), Modulo(%), Exponent(**)")
op = input("what is the operator? ").lower()


str_num1 = str(num1)
str_num2 = str(num2)

if op == "+" or "addition": #Addition
  ans = num1 + num2
  ans = str(ans)
  print(str_num1 + "+" + str_num2 + "=" + ans)
elif op == "-" or "subtraction": #Subtraction
  ans = num1 - num2 
  ans = str(ans)
  print(str_num1 + "-" + str_num2 + "=" + ans)
elif op == "*" or "mulitiplication": #Mulitplication
  ans = num1 * num2
  ans = str(ans)
  print(str_num1 + "*" + str_num2 + "=" + ans)
elif op == "/" or "division": #Division
  ans = num1 / num2
  ans = str(ans)
  print(str_num1 + "/" + str_num2 + "=" + ans)
elif op == "%" or "modulo": #Modulo (Finds remainder between the two numbers)
  ans = num1 % num2
  ans = str(ans)
  print(str_num1 + "%" + str_num2 + "=" + ans)
elif op == "**" or "exponent": #Exponent (Mulitplies the main number by the exponenet x amount of times)
  ans = num1 ** num2
  ans = str(ans)
  print(str_num1 + "**" + str_num2 + "=" + ans) 