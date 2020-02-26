#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    return is_palindrome_iterative(text)
    # return is_palindrome_recursive(text)

def word_cleaner(text):
    '''
    takes a text string and removes unnecessary characters, allows for easy case
    manipulation via lower or upper.
    '''
    clean = ''
    for i in text:
        if i in string.ascii_letters:
            clean = clean + i
    return clean

def is_palindrome_iterative(text):
    # Done: implement the is_palindrome function iteratively here
    clean = word_cleaner(text)
    reverse = ''
    for letter in clean[:: -1]:
            reverse = reverse + letter
    if reverse.lower() == clean.lower():
        return True
    else:
        return False

    '''
    for i in range(0,len(clean)//2):

        if clean[i] == clean[-i - 1]
    '''
    # once implemented, change is_palindrome to call is_palindrome_iterative
    # to verify that your iterative implementation passes all tests


def is_palindrome_recursive(text, left=None, right=None):
    # Done: implement the is_palindrome function recursively here
    clean = word_cleaner(text).lower()
    return is_pal_recursive(clean, 0, -1)


def is_pal_recursive(text, left, right):
    '''
    helper function that allows the palidrome to execute recursively,
    while initializing core elements (lowercasing the word).
    '''
    if  len(text) <= left:
        return True
    else:
        if text[left] == text[right]:
            return is_pal_recursive(text, left+1, right-1)
        else:
            return False
    # once implemented, change is_palindrome to call is_palindrome_recursive
    # to verify that your iterative implementation passes all tests


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
