def get_index_different_char(chars):
    alpha_counter = 0
    non_alpha_counter = 0
    for char in chars:
        if str(char) == '' or str(char) not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789':
            non_alpha_counter += 1
        else:
            alpha_counter += 1

    if alpha_counter > 1:
        for idx, char in enumerate(chars):
            if str(char) not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789':
                return idx

    else:
        for idx, char in enumerate(chars):
            if str(char) != '' and str(char) in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789':
                return idx

# import string
#
# alphanumeric_chars = list(string.ascii_letters + string.digits)
#
#
# def get_index_different_char(chars):
#     matches, no_matches = [], []
#     for i, char in enumerate(chars):
#         if str(char).lower() in alphanumeric_chars:
#             matches.append(i)
#         else:
#             no_matches.append(i)
#     return matches[0] if len(matches) == 1 else no_matches[0]


# print(get_index_different_char(['A', 'f', '.', 'Q', 2]))
# print(get_index_different_char(['.', '{', ' ^', '%', 'a']))
# print(get_index_different_char([1, '=', 3, 4, 5, 'A', 'b', 'a', 'b', 'c']))
print(get_index_different_char(['=', '=', '', '/', '/', 9, ':', ';', '?', '¡']))
# list(range(1,9)) + ['}'] + list('abcde'),  # noqa E230
# [2, '.', ',', '!']