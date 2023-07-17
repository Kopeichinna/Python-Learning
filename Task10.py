"""
    Task 10.

    Description:

Given the list of integers ( positive , negative, zeros)
Find max multiplication of three values in list

Input: [-1, 1, 2, 0, 3, 12, 4, 5, -1, 6]
Output: Max value = "360". Nums are: (12, 5, 6)

Input: [-7, 1, 2, 0, 3, 12, -24, 5, -1, 6]
Output: Max value = "2016". Nums are: (-7, 12, -24)
"""

l1 = [-1, 1, 2, 0, 3, 12, 4, 5, -1, 6]


# creating a copy of the list for further modification
l2 = l1.copy()

# sorting modified list
list_sorted = sorted(l2)

# getting 3 values from each boundary
max_positive_list = list_sorted[-3:]
max_negative_list = list_sorted[:3]

# checking 1-st option of getting max value
multiply_only_positive = (max_positive_list[0] *
                          max_positive_list[1] * max_positive_list[2])

# checking 2-nd option of getting max value
multiply_negative_positive = (max_negative_list[0] *
                              max_negative_list[1] * max_positive_list[2])

# creating variables to store final numbers
final_numbers_pos = ()
final_numbers_neg = ()

# logic for comparing both products of multiplication
# and printing final result
if multiply_only_positive > multiply_negative_positive:
    final_numbers_pos = tuple(max_positive_list)
    print(f'Max value = "{multiply_only_positive}". '
          f'Nums are: {final_numbers_pos}')
else:
    final_numbers_neg = (max_negative_list[0], max_negative_list[1],
                         max_positive_list[-1])
    print(f'Max value = "{multiply_negative_positive}". '
          f'Nums are: {final_numbers_neg}')

