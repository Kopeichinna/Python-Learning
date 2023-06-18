poem_text = """I wandered lonely as a cloud
That floats on high o'er vales and hills,
When all at once I saw a crowd,
A host, of golden daffodils;
Beside the lake, beneath the trees,
Fluttering and dancing in the breeze. 

Continuous as the stars that shine
And twinkle on the Milky Way,
They stretched in never-ending line
Along the margin of a bay:
Ten thousand saw I at a glance,
Tossing their heads in sprightly dance."""

poem_text.lower()
print('_'*20)
print(f"| {'vowel':^7} | {'count':^7} |")
print('_'*20)


def count_letters(letter, count = 0):
     for item in poem_text.lower():
        if item == letter:
         count += 1
     print(f"| {letter:^7} | {count:^7} |")

count_letters('a')
count_letters('e')
count_letters('i')
count_letters('o')
count_letters('u')
print('_'*20)


poem_text_modified = poem_text.replace('a','à').replace('A','À').replace('e','é').replace('E','É').replace('i','í').replace('I','Í').replace('o','ó').replace('O','Ó').replace('u','ú'
).replace('U','Ú')

print(poem_text_modified)