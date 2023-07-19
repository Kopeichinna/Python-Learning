"""
    Task 10: Regex.

    Description:

open input.txt file and find all small english letters
that match such conditions:
target small letter round exactly with three capital english letters
on the left and on the right
Match examples:
sdTRYaUVKn  -> matches "a"
NTRSjARTb   -> no match ( not exactly 3 capital letters on the left)
zDFGbOPNq   -> matches "b"
Print Output as : "Result: "<your_found_human_readable_string">
"""

import re

try:
    with open('input1.txt', 'r') as fh:
        input_data = fh.read()

        # getting the list of letters matching the search criteria
        letters_found = re.findall('[A-Z]{3}([a-z])[A-Z]{3}',
                                   string=input_data)
        print(f'"Result: {letters_found}')

except Exception as g_exc:
    print(g_exc)
