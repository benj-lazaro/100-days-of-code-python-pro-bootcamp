# Arguments with default values
def add(a=1, b=2, c=3):
    return a + b + c


print(f"Ths sum is {add(a=4, b=5, c=6)}")


# Unlimited positional arguments using *args (*args stored as a tuple)
def add(*args):
    print(f"\nContent of *args: {args}")
    print("------")

    total_sum = 0

    for n in args:
        total_sum += n

    return total_sum


print(f"The sum is {add(1, 2, 3, 4, 5, 6, 7, 8, 9)}.")
print(f"The sum is {add(123898, 38906, 343098)}.")


# Unlimited keyword arguments (**kwargs stored as a dictionary)
def calculate(num, **kwargs):
    print(f"\nContent of **kwargs: {kwargs}")
    print("------")

    for key, value in kwargs.items():
        print(key)
        print(value)

    num += kwargs["add"]
    num *= kwargs["multiply"]
    return num


print(f"\nCalculate() returns the value of {calculate(2, add=3, multiply=5)}\n")


# Class definition with **kwargs
class Car:

    def __init__(self, **kwargs):
        # Using .get() method returns None if no corresponding argument value is passed
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.colour = kwargs.get("colour")
        self.seats = kwargs.get("seats")


my_car = Car(make="Nissan", model="GT-R", colour="Black", seats=2)
print("\nClass using **kwargs")
print(f"Car manufacturer: {my_car.make}")
print(f"Car model: {my_car.model}")
print(f"Car colour: {my_car.colour}")
print(f"Car seat number: {my_car.seats}")

my_car2 = Car(make="Volkswagen", colour="Hot Pink", seats=3)
print("\nClass using **kwargs")
print(f"Car manufacturer: {my_car2.make}")
print(f"Car model: {my_car2.model}")
print(f"Car colour: {my_car2.colour}")
print(f"Car seat number: {my_car2.seats}")
