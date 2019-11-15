def sum_numbers(numbers=None):
    if numbers is None:
        return sum(x for x in range(101))

    return sum(numbers)