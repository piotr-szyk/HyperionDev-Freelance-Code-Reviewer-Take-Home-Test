'''
HyperionDev Freelance Code Reviewer Take-Home Test
Section C: Code Challenge
Option 4: International Standard Book Numbers
Author: Piotr Szyk
Date: 14 May 2023
'''

'''
The "International Standard Book Number" task description on
https://edabit.com/challenge/DpFmDxcyesPfPoFMn for how the ISBN-13
is calulated in not correct. The statement: "If the sum is divisible by 10,
the ISBN-13 is valid" is not true. It seems that the procedure is missing
one important step. According to the Appendix 1 (Check digit calculation)
of the ISBN International Users Manual - 7th edition, this is Step 2,
which only renders the reminder. In the missing Step 3, that reminder is
substracted from 10. Also, when we line up the digits with alternating
1s and 3s only first 12 digits should be considered, not 13.
The last digit is the check digit. The correct procedure is as follows:
Each of the first 12 digits of the ISBN is alternately multiplied by 1 and 3.
The check digit is equal to 10 minus the remainder resulting from dividing the
sum of the weighted products of the first 12 digits by 10 with one exception.
If this calculation results in an apparent check digit of 10,
the check digit is 0. I have assumed the correct procedure in the program.
'''


def validate_isbn_10(isbn_string):
    '''
    Validate an ISBN-10 number.

    Parameters:
    isbn_string (str): The ISBN-10 number to validate.

    Return:
    bool: True if the ISBN-10 number is valid, False otherwise.
    '''
    # Check if isbn has correct length (10)
    if len(isbn_string) != 10:
        return False

    # Only allow digits or 'X'
    for char in isbn_string:
        if not (char.isdigit() or char.lower() == "x"):
            return False

    # Calculate the checksum
    checksum = 0
    for index, char in enumerate(isbn_string):
        # print(index, char)
        if char not in {"x", "X"}:
            checksum += int(char) * (10 - index)
            # print(checksum)
        else:
            checksum += (10 * (10 - index))
            # print(checksum)
    # Check if the checksum is divisible by 11
    return checksum % 11 == 0


def validate_isbn_13(isbn_string):
    '''
    Check if an ISBN-13 number is valid.

    Parameters:
    isbn_string (str): ISBN-13 number to be validated.

    Return:
    bool: True if the ISBN-13 number is valid, False otherwise.
    '''
    # Check if isbn has correct length (13)
    if len(isbn_string) != 13:
        return False
    # Only allow digits (the exception of allowed X is just for isbn-10)
    if not isbn_string.isdigit():
        return False
    # Calculate the checksum
    checksum = 0
    for index, char in enumerate(isbn_string[:-1]):
        # If the index is even, use 1 as the multiplier
        if index % 2 == 0:
            checksum += int(char) * 1
        # If the index is odd, use 3 as the multiplier
        else:
            checksum += int(char) * 3
    return (10 - checksum % 10) % 10 == int(isbn_string[-1])


def convert_isbn_10_to_isbn_13(isbn_string):
    '''
    Convert an ISBN-10 number to an ISBN-13 number.

    Parameters:
    isbn_string (str): The ISBN-10 number to convert.

    Returns:
    str: The converted ISBN-13 number.
    '''
    # Prepend the prefix "978" (book in english language)
    isbn_13_prefix = "978"
    isbn_13 = isbn_13_prefix + isbn_string[:9]

    # Calculate the check digit for ISBN-13
    checksum = 0
    for index, char in enumerate(isbn_13):
        # If the index is even, use 1 as the multiplier
        if index % 2 == 0:
            checksum += int(char) * 1
        # If the index is odd, use 3 as the multiplier
        else:
            checksum += int(char) * 3
    checksum = (10 - (checksum % 10)) % 10
    isbn_13 += str(checksum)

    return isbn_13


def main(isbn_string):
    if validate_isbn_13(isbn_string):
        return print(f"The number {isbn_string} is a Valid ISBN-13")
    elif validate_isbn_10(isbn_string):
        return print(f"The number {isbn_string} is a Valid ISBN-10. "
                     f"Converting to ISBN-13: "
                     f"{convert_isbn_10_to_isbn_13(isbn_string)}")
    else:
        return print(f"Invalid! Unfortunately the number provided: "
                     f"{isbn_string} in not a valid ISBN-10 nor ISBN-13.")


# An example providing valid ISBN-10 number:
isbn_string = "076790818X"
# An example providing valid ISBN-13 number:
# isbn_string = "9780679760801"
# An example providing invalid number:
# isbn_string = "AB34jj440873"

if __name__ == "__main__":
    main(isbn_string)
