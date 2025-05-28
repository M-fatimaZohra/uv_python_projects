def main():
    BLUE = '\033[94m'
    RESET = '\033[0m'
    counter = {}

    while True:
        enter_number = input(f"{BLUE}Enter a Number to start or just empty enter to exit{RESET}") 

        if enter_number == "":
            break

        try:
            number = int(enter_number)
        except ValueError:
            print("Please enter a valid number.")
            continue

        else:
            
            counter[number] = counter.get(number, 0) + 1  #counter[number] are number i enter,   counter.get(number, 0) + 1 are quantities of that numbers


    for number, count in counter.items():
        print(f"{number} appears {count} times.")


if __name__ == "__main__":
    main()