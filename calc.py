while True:
   print("Options:")
   print("Enter 'add' to add two numbers")
   print("Enter 'subtract' to subtract two numbers")
   print("Enter 'multiply' to multiply two numbers")
   print("Enter 'divide' to divide two numbers")
   print("Enter 'quit' to end the program")
   user_input = input(": ")

   if user_input == "quit":
      break
   elif user_input == "add":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        sum = num1 + num2
        print(sum)
   elif user_input == "subtract":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        sub = num1 - num2
        print(sub)
   elif user_input == "multiply":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        mul = num1 * num2
        print(mul)
   elif user_input == "divide":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        div = num1 / num2
        print(div)
   else:
      print("Unknown input")