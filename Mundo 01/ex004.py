a = input('Digite algo: ')
print('O tipo primitivo desse valor {} é '.format(a), type(a))
print('O valor {} só tem espaços? '.format(a), a.isspace())
print('O valor {} é um número? '.format(a), a.isnumeric())
print('O valor {} é alfabético? '.format(a), a.isalpha())
print('O valor {} é um alfanumérico? '.format(a), a.isalnum())
print('O valor {} está em maiúsculas? '.format(a), a.isupper())
print('O valor {} está em minúsculas? '.format(a), a.islower())
print('O valor {} é capitalizada? '.format(a), a.istitle())
