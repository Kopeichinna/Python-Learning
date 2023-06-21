branch1
"""
Home task 4. If- statements.

Task description:
we have four values w,x,y,z
write if-elif-else statement that will search minimum value and print smth aka "'y' is minimum value'
advice use python debugger and different values to check your algorithm
  """

 main

w, x, y, z = 100, 200, 40, 300

if w < x and w < y and w < z:
    print("'w' is a minimum value")
elif x < w and x < y and x < z:
    print("'x' is a minimum value'")
elif y < w and y < x and y < z:
    print("'y' is a minimum value'")
else:
    print("'z' is a minimum value'")
