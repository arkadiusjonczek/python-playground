while True:
    try:
        number = int(input("Enter your number: "))
        print(number)
        break
    except ValueError:
        print("Bro, this is not a number. Please try again.")
