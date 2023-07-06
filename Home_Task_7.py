"""
    Task 7: String conversion.

    Description:

Convert a non-negative integer num to its English words representation.
Example 1:
Input: num = 123
Output: "One Hundred Twenty Three"

let's take that number always > 100 and only three digits
100 <= num <= 999
"""

ones = {'1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five',
        '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine'}
dozens = {'2': 'Twenty ', '3': 'Thirty ', '4': 'Forty ', '5': 'Fifty ',
          '6': 'Sixty ', '7': 'Seventy ', '8': 'Eighty ', '9': 'Ninety '}
hundreds = {'1': 'One Hundred ', '2': 'Two Hundreds ', '3': 'Three Hundreds ',
            '4': 'Four Hundreds ', '5': 'Five Hundreds ', '6': 'Six Hundreds ',
            '7': 'Seven Hundreds ', '8': 'Eight Hundreds ',
            '9': 'Nine Hundreds '}
teens = {'1': 'eleven', '2': 'Twelve', '3': 'Thirteen', '4': 'Fourteen',
         '5': 'Fifteen', '6': 'Sixteen', '7': 'Seventeen', '8': 'Eighteen',
         '9': 'Nineteen'}


num = 303
num_str = str(num)
num_converted = ''


for k, v in hundreds.items():
    if num_str[0] == k:
        num_converted += v

if num_str[1] == '1':
    for k, v in teens.items():
        if num_str[2] == k:
            num_converted += v
else:
    for k, v in dozens.items():
        if num_str[1] == k:
            num_converted += v
    for k, v in ones.items():
        if num_str[2] == k:
            num_converted += v

print(num_converted)
