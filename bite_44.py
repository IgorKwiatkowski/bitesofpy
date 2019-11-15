import random
import string


def gen_key(parts=4, chars_per_part=8):
    segments = []
    for num in range(parts):
        segments.append(''.join(random.choices(string.ascii_uppercase + string.digits, k=chars_per_part)))
    return '-'.join(segments)

print(gen_key())