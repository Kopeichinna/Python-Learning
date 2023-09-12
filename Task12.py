"""
      Task 12 - Recursion.

      Description:

Given list of list of list etc of integers
write recursive function that will accept as argument target list
and return sum of all integers inside it
Input: [[[[1, 4, 5], [[6, 9],[[[8, 1], 7], 3], 2], 7], 5, 2], 9, [1, 2]]
Output: Target sum = 72
"""

l1 = [[[[1, 4, 5], [[6, 9], [[[8, 1], 7], 3], 2], 7], 5, 2], 9, [1, 2]]


def get_target_sum(obj, target_sum=None):
    """Recursive func retrieving integers from the lists and sum them up."""
    target_sum = [] if target_sum is None else target_sum
    for i in obj:
        if type(i) == int:
            target_sum.append(i)
        else:
            get_target_sum((i), target_sum)
    return sum(target_sum)


print(f'Target sum = {get_target_sum(l1)}')
