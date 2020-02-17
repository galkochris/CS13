#!python

import string
import math

# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace

Mega_String = string.digits + string.ascii_lowercase
decode_dictionary = {digit: val for val, digit in enumerate(Mega_String)}

def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # ALL: Decode digits from binary (base 2)
    # IN: Decode digits from hexadecimal (base 16)
    # ONE: Decode digits from any base (2 up to 36)
    #number x base to power of index if -1 sort of string
    decoded = 0
    for index, digit in enumerate(reversed(digits)):
        decoded += (base**index * decode_dictionary[digit])
    return decoded


    # if base == 10:
    #     return digits
    # else:
    #     convert = 0
    #     for i in digits[::-1]:
    #         if i not in string.digits:
    #             i = conv_help(i)
    #         convert = convert + int(i)*int(base**(len(digits) - digits.index(i) - 1))
    #     return convert



#conv_help could also be:
# def conv_help(val):
#     if val in string.ascii_letters:
#         val = 10 + string.ascii_uppercase.index(val)
#         return val

# def rev_help(num):
#     if num > 9:
#         num = num - 10
#         lett = string.ascii_uppercase[num]
#         return lett



def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    # ALL: Encode number in binary (base 2)
    # IN: Encode number in hexadecimal (base 16)
        # 5 = '0101'
        # 8 = '1000'
        # 16 = '0001 0000'
        # base converts to 10 for every case
    # ONE: Encode number in any base (2 up to 36)

    """
    in all cases the base returns 10, so that statement exists to  break before the loop, else the for loop checks the number from left to right, converting and value above
    or equal to the base into the base values

    """


    if number < base:
        return Mega_String[number]

    quot, remain = divmod(number, base)

    return encode(quot, base) + Mega_String[remain]
    # new_number = ''
    # if base == 2:
    #     while number > 0:
    #         remainder = number % 2
    #         number = math.floor(number / 2)
    #         new_number = str(remainder) + str(new_number)
    #     return new_number
    # if number == base:
    #     return '10'
    # else:
    #     while number > 0:
    #         if number >= base:
    #             power = (number//base)
    #             if power > 9:
    #                 rev_help(power)
    #             new_number = str(power) + str(new_number)
    #             number = number - base*power
    #         else:
    #             if number > 9:
    #                 new_number = new_number + rev_help(number)
    #                 return new_number
    #             else:
    #                 new_number = new_number + str(number)
    #                 number = 0
    #                 return new_number

    # for i in number[::-1]:
    #     if i not in string.digits:
    #         i = conv_help(i)
    #     convert = i*(base**(number.index(i))) + convert
    #     return convert


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    # All: Convert digits from base 2 to base 16 (and vice versa)
    # ...
    # IN: Convert digits from base 2 to base 10 (and vice versa)
    # ...
    # THE: Convert digits from base 10 to base 16 (and vice versa)
    # ...
    # LAST: Convert digits from any base to any base (2 up to 36)
    val = decode(digits, base1)
    new_val = encode(int(val), base2)
    return new_val


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        result = convert(14, 10, 16)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    # main()
    print(convert("72", 10, 16))
    print(convert("72", 10, 2))
    print(convert("1000", 2, 16))
    print(convert("1000", 2, 10))
