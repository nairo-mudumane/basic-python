import re

test = 'O gato eh bonito'

regex = re.search(r'bo.*', test)

if regex:
    print(regex.group())
else:
    print('Not found!')