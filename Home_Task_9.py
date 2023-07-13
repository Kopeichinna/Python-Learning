"""
    Task: Operations with files, REs.

    Description:

write script that will read "input.txt" file
and find there all characters from english alphabet
collect these characters and their positions in file
after info collected this info as text
write to "output.txt" file in such format
####################
<first found letter> -> pos1
<next_letter> -> pos2
<next_letter -> pos3
etc
#######################
"""

import re

try:
#opening both input and output files
    with open('input.txt', 'r') as fh, open('output.txt', 'w') as fh2:
        input_data = fh.read()

        # getting the list of letters matching the search criteria
        letters_found = re.findall('[a-z]', string=input_data)

        # getting matches as iterators
        iterables_found = re.finditer('[a-z]', string=input_data)

        # retrieving positions of the matches
        positions_found = [(m.start(0), m.end(0)) for m in iterables_found]

        # matching found letters with the corresponding positions
        regexp3 = dict(zip(letters_found, positions_found))

        # writing matching letters and positions as strings to the output files
        for k, v in regexp3.items():
            result = f'{k} --> {v}'
            fh2.write(result + '\n')

except Exception as g_exc:
    print(g_exc)
