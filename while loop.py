n = int(input("Enter input name:"))

fact = 1
if n < 0:
  print("Factorial does not exist for negetive numbers")
elif n == 0:
  print("The factorial of 0 is 1 ")
else:
  while(n>0):
    fact = fact * n
    n = n-1
    print("The factorial is",fact)