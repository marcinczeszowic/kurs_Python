def sum_positives(numbers):
    total = 0

    for number in numbers:
        if number > 0:
            total += number

    return total


numbers = [1, -2, 3, 0, -4, 5]
print(sum_positives(numbers))


def sum_positives(numbers):
    return sum([number for number in numbers if number > 0])


numbers = [1, -2, 3, 0, -4, 5]
print(sum_positives(numbers))