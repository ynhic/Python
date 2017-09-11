import re

resultado = re.match('[A-Za-z]y', 'python zython')

print(resultado)
print('---------------------------------')
print(resultado.group())


resultado = re.findall('([A-Za-z]y[A-za-z]+)', 'python zython')

print(resultado)
