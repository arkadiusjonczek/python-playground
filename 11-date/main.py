import datetime

def main():
    x = datetime.datetime.now()
    print(x)
    print(x.strftime("%A"))

if __name__ == "__main__":
    main()