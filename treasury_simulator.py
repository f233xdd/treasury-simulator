import re
import sys
import random
from typing import List

debug = True
# if this is True, you can see the correct numbers in total,
# and the true password will be shown at the beginning


def create_password(length=7) -> List[int]:
    passwd = []

    for _ in range(length):
        passwd.append(random.randint(0, 9))

    if debug:
        print(passwd)

    print('\n', end='')

    return passwd


def get_input(true_password, msg) -> str:
    length = len(true_password)

    while True:
        input_password = input(f'[ {length}|{msg} ]> ')
        print('\n', end='')

        try:
            int(input_password)

            if len(input_password) == length:
                return input_password
            else:
                print(f"Length is {length}!")
                print('\n', end='')
                return get_input(true_password, msg)

        except ValueError:
            print("Your input is not numbers!")
            print('\n', end='')


def infer_input_password(true_password, input_password) -> tuple[list[bool | str], list[int]]:
    length = len(true_password)
    sorted_input = re.findall(r'\d', input_password)
    sorted_int_input = [int(i) for i in sorted_input]
    output = []

    for i in range(length):
        if sorted_int_input[i] == true_password[i]:
            output.append(True)
        elif sorted_int_input[i] in true_password:
            output.append('wow')
        else:
            output.append(False)

    return output, sorted_int_input


def main(try_times=5, len_of_passwd=7) -> int:
    true_password = create_password(len_of_passwd)

    for i in range(try_times):
        input_password = get_input(true_password, (try_times-i))
        infer, sorted_int_input = infer_input_password(true_password, input_password)
        correct_numbers = infer.count(True)

        if debug:
            print(f"count: {correct_numbers}")

        if correct_numbers != 7:

            for j in range(len_of_passwd):
                print((sorted_int_input[j], infer[j]), end='--')
            print('\b\b\n')

        else:
            print('\n', end='')
            print("The case is unlocked!")
            print('\n', end='')
            break

    print("The case is locked forever!")

    return 0


if __name__ == "__main__":
    sys.exit(main())
