# You have list of tuples. Each tuple represents: name, age, some sum, last name, sex
# Please do such things:
# 1 - sort list by age and sex fields
# 2 - somehow you need to get new list as old list without first two elements and last two elements. Print this new list
# 3 - in new list calculate total numbers of "female"  and "male" and print it as small table.
# Example:
# -----------------
# | sex    | count |
# -----------------
# |  female |  11  |
# |   male  |  23  |
# -----------------
#  advice: female and male calculation can be done vs flat list or you can find your own approach ;)

"""Sorting, Coping and  Calculations in Lists """

people = [
    ('Alice', 32, 100, 'Johnson', 'female'),
    ('Bob', 41, 200, 'Smith', 'male'),
    ('Charlie', 27, 150, 'Jones', 'male'),
    ('David', 52, 75, 'Williams', 'male'),
    ('Eve', 18, 300, 'Davis', 'female'),
    ('Frank', 33, 50, 'Taylor', 'male'),
    ('Grace', 42, 125, 'Clark', 'female'),
    ('Henry', 26, 225, 'Lewis', 'male'),
    ('Ivy', 38, 175, 'Moore', 'female'),
    ('Jack', 20, 140, 'Harris', 'male'),
    ('Kate', 37, 110, 'Miller', 'female'),
    ('Leo', 44, 90, 'Wilson', 'male'),
    ('Mae', 29, 180, 'Brown', 'female'),
    ('Nick', 51, 70, 'Davies', 'male'),
    ('Oliver', 18, 250, 'Collins', 'male'),
    ('Pete', 36, 160, 'Green', 'male'),
    ('Quinn', 20, 230, 'Bell', 'female'),
    ('Remy', 30, 120, 'Foster', 'male'),
    ('Sara', 28, 140, 'Baker', 'female'),
    ('Tom', 47, 80, 'Scott', 'male'),
    ('Ursula', 39, 135, 'Adams', 'female'),
    ('Vivian', 25, 190, 'Ross', 'female'),
    ('Wendy', 46, 90, 'Wright', 'female'),
    ('Xavier', 31, 105, 'Reed', 'male'),
    ('Yuliana', 22, 200, 'Lopez', 'female'),
    ('Zack', 48, 60, 'Mitchell', 'male'),
    ('Adam', 35, 75, 'Davis', 'male'),
    ('Bella', 27, 125, 'Smith', 'female'),
    ('Charlie', 44, 115, 'Johnson', 'male'),
    ('Daisy', 20, 215, 'Miller', 'female'),
    ('Ethan', 33, 100, 'Taylor', 'male'),
    ('Fiona', 40, 150, 'Jones', 'female'),
    ('George', 24, 180, 'Lewis', 'male'),
    ('Hannah', 22, 200, 'Williams', 'female'),
    ('Ivan', 29, 160, 'Brown', 'male'),
    ('Julie', 55, 90, 'Clark', 'female'),
    ('Kenny', 38, 140, 'Harris', 'male'),
    ('Luna', 55, 170, 'Smith', 'female'),
    ('Mike', 55, 55, 'Johnson', 'male')
]
from operator import itemgetter
people.sort(key=itemgetter(1,4))    #sorting by age and sex

new_people = people.copy()   # creating copy of the list
new_people.pop()      # removing last element of the copied list
new_people.pop()      # removing once again last element of the copied list
del new_people[0]     # removing first element of the copied list
del new_people[0]     # removing once again first element of the copied list

#to check the correctness of list items numbers modification
#print(len(people))
#print(len(new_people))

list_of_people = sum(new_people,())     # unpacking all the items into a flat list

list_of_people.count('male')    # counting of 'male'
list_of_people.count('female')      #counting of 'female'

# printing the table with "male" and "female" items counted
print('_' * 20)
print(f"| {'sex': ^7} | {'count':^7} |")
print('_' * 20)
print(f"| {'female':^7} | {list_of_people.count('female') : ^7} |")
print(f"| {'male':^7} | {list_of_people.count('male') : ^7} |")
print('_' * 20)
