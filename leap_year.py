#!/usr/bin/env python3

# Created By: Amara Tie

# Date: April 3, 2025

# This program caculates if its a year is a leap year


def main():

    # Ask User for year
    year_as_string = input("Enter the year :")
    print("")

    # Check if the user's age matches the grandparents' criteria
    try:
        year_as_number = int(year_as_string)
        if year_as_number % 4 == 0:
            if year_as_number % 100 == 0:
                if year_as_number % 400 == 0:
                    print("The year {} is a leap year".format(year_as_number))
                else:
                    print("The year {} is not a leap year".format(year_as_number))
            else:
                print("The year {} is a leap year".format(year_as_number))
        else:
            print("The year {} is not a leap year".format(year_as_number))
    except Exception:
        print("This is not a year")
    finally:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
