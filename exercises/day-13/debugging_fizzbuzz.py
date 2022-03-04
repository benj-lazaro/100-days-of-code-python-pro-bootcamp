for number in range(1, 101):
    # Solution: Changed the logical operator from or to and
  if number % 3 == 0 or number % 5 == 0:
    print("FizzBuzz")
    # Solution: Change if statement into elif statement
  if number % 3 == 0:
    print("Fizz")
  if number % 5 == 0:
    print("Buzz")
  else:
    # Reformatted the string into an f-string to property display the number
    print(f"{number}")
