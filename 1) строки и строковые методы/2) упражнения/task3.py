animal_1 = "Animals"
animal_2 = "Badger"
animal_3 = "Honey Bee"

print(animal_1.lower())
print(animal_2.lower())
print(animal_3.lower())

print('\n')

print(animal_1.upper())
print(animal_2.upper())
print(animal_3.upper())

print('\n')

string1 = '       Filet Mignon'
string2 = 'Brix    '
string3 = '       Filet Mignon    '

print(string1.lstrip())
print(string2.rstrip())
print(string3.strip())

print('\n')

strings1 = 'Becomes'
strings2 = 'becomes'
strings3 = 'BEAR'
strings4 = 'bEautiful'

print(strings1.startswith('be'))
print(strings2.startswith('be'))
print(strings3.startswith('be'))
print(strings4.startswith('be'))

print('\n')

print(strings1.lower().startswith('be'))
print(strings3.lower().startswith('be'))
print(strings1.lower().startswith('be'))