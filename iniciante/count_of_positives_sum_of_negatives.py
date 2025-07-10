"""
Given an array of integers.
Return an array, where the first element is the count of positives' numbers and the second element is the sum of negative numbers. 0 is neither positive nor negative.
If the input is an empty array or is null, return an empty array.
"""
def count_positives_sum_negatives(arr):
    if arr is None or len(arr) == 0:
        return []

    positive_numbers = []
    negative_numbers = []

    for number in arr:
        if number > 0:
            positive_numbers.append(number)
        elif number < 0:
            negative_numbers.append(number)

    positive_count = len(positive_numbers)
    negative_sum = sum(negative_numbers)

    return [positive_count, negative_sum]