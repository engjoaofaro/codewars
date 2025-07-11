"""
Description:

Write a function that accepts an integer argument n and generates an array containing the pairs of integers [a, b] that satisfy the condition

0 <= a <= b <= n

The pairs should be sorted by increasing values of a then by increasing values of b.
"""
def generate_pairs(n):
    result = []
    if n == 0:
        result.append([0, 0])
        return result
    for i in range(n):
        for j in range(i, n+1):
            result.append([i, j])
    result.append([n, n])
    return result