#!/usr/bin/env python3
# Created by: Jonathan Kene
# Created on: May. 17, 2021
# This program asks the user for the number of classes held
# and the number of classes attended
# and tells the user whether or not the student
# is allowed to attend the exam

def main():

    # The program will explain the user about the exam requirements
    # and ask for the amount of classes helded and attended
    print("A student will not be allowed to write the final exam if"
          " his/her attendance is less than 75%.")
    class_held_string = input("Enter the amount of classes helded (m): ")
    class_attended_string = input("Enter the amount of classes attended (m): ")

    # make sure if the user types anything but an integer, it's not valid
    try:
        class_held_int = int(class_held_string)
        print("You entered an integer correctly")
        print("")
    except ValueError:
        print("{} is not a number" .format(class_held_string))
        print("")
        print("Please try again")
    else:
        try:
            class_attended_int = int(class_attended_string)
            print("You entered an integer correctly")
            print("")
        except ValueError:
            print("{} is not a number" .format(class_attended_string))
            print("")
            print("Please try again")
        else:
            percentage_attendence = ((class_attended_int/class_held_int)*100)
            print("")
            print("{:.2f}". format(percentage_attendence))

            # check to see if the integer is postive, negative or just zero
            if percentage_attendence > 75:
                print("Your attendance meets the exam requirements."
                      " Congratulations!")
            elif percentage_attendence == 75:
                print("Your attendance meets the exam requirements."
                      " Congratulations!")
            else:
                print("I'm sorry but the number doesn't meet the requirement")
        finally:
            print("")
            print("Thank you for your input")


if __name__ == "__main__":
    main()
