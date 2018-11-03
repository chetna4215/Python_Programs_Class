"""
1. Variables
2. strings, Integers, Boolean types
3. None Types
4. Lists, Dictionary

"""

# ############################################################################
# 1)Variables
# #############################################################################
first_str = 'Python Class'
print(first_str, type(first_str), id(first_str), id(type(first_str)))

first_int = 22
print(first_int, type(first_int), id(first_int), id(type(first_int)))

first_boolean = False
print(first_boolean, type(first_boolean), id(type(first_boolean)))

first_none = None
print(first_none, type(first_none), id(type(first_none)))

x = str()
print(str, type(x), id(x), type(x))


my_list = [
    first_str, first_int, first_boolean, first_none, x,
    ['Chetna', first_str, first_none]
]

print(my_list)
print(my_list[::])
print(my_list[::-1])
print(my_list[11::-1])
print(my_list[0:5])

list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list_numbers[::])
print(list_numbers[1:4:])
print('Odd Numbers are : ',  list_numbers[0:9:2])
print('Even Numbers are : ', list_numbers[1:9:2])

my_dictionary = {
    'Name' : 'Chetna',
    'Surname':'Mudgale',
    'Department' : 'IT Department',
    'Place' : 'Pune'
}

print(my_dictionary)

print(my_dictionary['Name'])
print(my_dictionary['Surname'])

