def rotate(string, n):
    """Rotate characters in a string.
       Expects string and n (int) for number of characters to move.
    """

    return string[n:] + string[:n]

print(rotate('hello', 2))
print(rotate('hello', -2))