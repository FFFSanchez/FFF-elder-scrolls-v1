from collections import namedtuple
from time import perf_counter

def average_time(structure, test_func):
    time_measurements = []
    for _ in range(1_000_000):
        start = perf_counter()
        test_func(structure)
        end = perf_counter()
        time_measurements.append(end - start)
    return sum(time_measurements) / len(time_measurements) * int(10**9)

def time_dict(dictionary):
    'name' in dictionary
    'missing_key' in dictionary
    28 in dictionary.values()
    'missing_value' in dictionary.values()
    dictionary['age']
    #dictionary['height']

def time_namedtuple(named_tuple):
    'name' in named_tuple._fields
    'missing_field' in named_tuple._fields
    28 in named_tuple
    'missing_value' in named_tuple
    named_tuple.age

Person = namedtuple('Person', ['name', 'age', 'height'])

timur = Person('Тимур', 29, 170)
timur_dct = {'name': 'Тимур', 'age': 29, 'height': 170}

print(f'Именованный кортеж: {average_time(timur, time_namedtuple)} наносекунд')
print(f'Словарь: {average_time(timur_dct , time_dict)} наносекунд')