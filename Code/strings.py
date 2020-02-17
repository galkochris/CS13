#!python

def contains(text, pattern):
    
    """Return a boolean indicating whether pattern occurs in text.

    same time complexity cases as find index, as it is directly related to
    find index

    """
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement contains here (iteratively and/or recursively)
    return find_index(text, pattern) != None

def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found.
    
    time complexity: Worst O(p*t): traverses entire string with almost matching ever pattern item;
    Best Case 0(1): breaks early due to if conditions; Average Case, pattern is found sometime during
    the for loop, O(~p*t/2)
    
    
    """
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_index here (iteratively and/or recursively)
    if len(pattern) <= 0:
        return 0
    if len(text) <= 0 or len(pattern) > len(text):
        return None
    else:
        offset = 0
        first = pattern[0]
        for index, start in enumerate(text):
            if start == first:
                if find_index_help(text, pattern, index, offset, index) == index:
                    return index
            

def find_index_help(text, pattern, index, offset, start_index):
    if offset >= len(pattern) -1:
        return start_index
    elif index >= len(text) -1:
        return None
    else:
        if text[index+1] == pattern[offset+1]:
            return find_index_help(text, pattern, index+1, offset+1, start_index)





def find_all_indexes(text, pattern):

    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found.
    
    time and space complexity: Worst Case 0(p*t): everything matches, and the search loops
    over every value; Best Case 0(1): for the two predifined cases that return None; Average Case 0(~p*t):
    the function still needs to loop over every value in text, however the loop ends early, once the pattern
    cannot be satisfied by the remaining text length.
    """
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)
    if len(pattern) <= 0:
        indexes = []
        for index, start in enumerate(text):
            indexes.append(index)
        return indexes
    if len(text) <= 0 or len(pattern) > len(text):
        return None
    else:
        indexes = []
        offset = 0
        first = pattern[0]
        for index, start in enumerate(text):
            if start == first:
                if find_index_help(text, pattern, index, offset, index) == index:
                    indexes.append(index)
        return indexes


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
