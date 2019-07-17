try:
    a = int(input("Enter a negative integer: "))
    if a >= 0:
        raise ValueError("That is not a negative number!")
except ValueError as ve:
    print(ve)