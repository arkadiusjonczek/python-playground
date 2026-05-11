def main():
    try:
        name = input("Enter your name: ")
        output =  hello(name)
        print(output)
    except ValueError as e:
        print("Error using the input value: " + str(e))

def hello(name):
    if name == "":
        raise ValueError("Expected a full name. Got an empty string.")
    return f"Hello {name}"

if __name__ == "__main__":
    main()
