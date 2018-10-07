dictionary = {'key' : 'value','key_2': 'value_2'}
print(dictionary)

nested_dict = {'dictA': {'key_1': 'value_1'},
                'dictB': {'key_2': 'value_2'}}
print(nested_dict['dictA'])
print(nested_dict['dictB'])

people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

print(people)

print(people[1]['name'])
print(people[1]['age'])
print(people[1]['sex'])