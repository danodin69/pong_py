
index = 0

n = ["boy", "girl", "pussy cat"]


while True:
    user_input = input(
        "Press [N] to print the next value or [Q] to quit: ").lower()

    if user_input == 'n':
        if index < len(n):
            print(n[index])
            index += 1
            if index == len(n):
                index = 0
        else:
            print("End of array reached.")
    elif user_input == 'q':
        print("Quitting.")
        break
    else:
        print(
            "Unrecognised input. Press [N] to print the next value or [Q] to quit.")
