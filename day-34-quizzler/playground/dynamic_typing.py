# Declare data type instead of assigning it an initial value; makes it less error-prone
# age: int
# name: str
# height: float
# is_human: bool


# Uses Type Hints: expects to receive a parameter value of int data type & return a bool data type
def police_check(age: int) -> bool:
    """Check age if user is old enough to drive"""
    if age > 18:
        can_drive = True
    else:
        can_drive = False

    return can_drive


if police_check(19):
    print("You may pass.")
else:
    print("Pay a fine.")
