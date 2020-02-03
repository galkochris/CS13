#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # TODO: Decode digits from binary (base 2)
    # TODO: Decode digits from hexadecimal (base 16)
    # TODO: Decode digits from any base (2 up to 36)
    #number x base to power of index if -1 sort of string
    for i in digits[::-1]:
        if i not in string.digits:
            i = conv_help(i)
        convert = i*(base**(digits.index(i)))
        return convert



#conv_help could also be:
#if val in string.ascii_lowercase or string.ascii_uppercase:
#   val = 10 + index of string.ascii.index(val)

def conv_help(val):
    num = 0
    if val is 'A':
        num = 10
    if val is 'B':
        num = 11
    if val is 'C':
        num = 12
    if val is 'D':
        num = 13
    if val is 'E':
        num = 14
    if val is 'F':
        num = 15
    if val is 'G':
        num = 16
    if val is 'H':
        num = 17
    if val is 'I':
        num = 18
    if val is 'J':
        num = 19
    if val is 'K':
        num = 20
    if val is 'L':
        num = 21
    if val is 'M':
        num = 22
    if val is 'N':
        num = 23
    if val is 'O':
        num = 24
    if val is 'P':
        num = 25
    if val is 'Q':
        num = 26
    if val is 'R':
        num = 27
    if val is 'S':
        num = 28
    if val is 'T':
        num = 29
    if val is 'U':
        num = 30
    if val is 'V':
        num = 31
    if val is 'W':
        num = 32
    if val is 'X':
        num = 33
    if val is 'Y':
        num = 34
    if val is 'Z':
        num = 35
    return num


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    # TODO: Encode number in binary (base 2)
    # ...
    # TODO: Encode number in hexadecimal (base 16)
    # ...
    # TODO: Encode number in any base (2 up to 36)
    for i in number[::-1]:
        if i not in string.digits:
            i = conv_help(i)
        convert = i*(base**(number.index(i)))
        return convert


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    # TODO: Convert digits from base 2 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from base 2 to base 10 (and vice versa)
    # ...
    # TODO: Convert digits from base 10 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from any base to any base (2 up to 36)
    for i in number[::-1]:
        if i not in string.digits:
            i = conv_help(i)
        convert = i*(base**(number.index(i)))
        return convert


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
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()
