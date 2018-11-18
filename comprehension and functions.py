"""
1. comprehension
2. indentation, scope of variables and section
3. built-in functions- min, max,count, zip, split, types, sum, sorted


Assignemnt:
1) create matrix using comprehension:
output:[[0,1,2],[0,1,2],[0,1,2]]

2) write a program to create dictionary of name ,salary,designation from list
eaxmple:['parth', 2000], 'Programmer']
output: ['name':parth, 'designation':'Programmer', 'salary': 20000]

3) Write a program to create list of dictioanry to store user info
example: ['parth', 2000], 'Programmer'] , ['srikant', 2000], 'Sr. Programmer']
example:
    {'name': , 'designation': , 'salary': }
   {'name': , 'designation': , 'salary': }




*agrs - unknown list
**kwargs- dictionary


"""
dict = {'name': "A", 'name': "b", 'name': "c"}
print(dict)

"""
built-in functions

"""

# print(F"min value {min(x)}")
""" zip is used for zipping to object

"""

d1 = {'x':1, 'y':2}
d2 = {'x':3, 'y':4}

for z,v in zip(d1.items(), d2.items()):
    print(z , v)




