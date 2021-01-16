# !/usr/bin/env python3

# Created by: Mohammad-al-buraiki
# Created on January 2021
# This program is a multiplecation table


def main():
    # this function is to find the multiplecation table
    # of the user's input
    while True:
        user_number = input("Enter the number: ")

        try:
            if user_number != int(user_number):
                print("")
                for loop_counter in range (0, 10 + 1):
                    print("{0} x {1} = {2}.".format(user_number, loop_counter,
                          loop_counter*(int(user_number))))
                    loop_counter = loop_counter + 1
                break

        except Exception:
            print("that is invalid input")
            print("try again")


if __name__ == "__main__":
    main()
