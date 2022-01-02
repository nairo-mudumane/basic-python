# r - leitura (padrao)
# r+ - leitura e escrita
# w - escrita
# a - append
# b - binarios
# rb - leitura de binarios
# wb - leitura de binarios

file = open('file.txt', 'r+')
# print(type(file))
# print(file)

for i in range(0, 51):
    file.write('Line: ' + str(i) + '\n')
    
for line in file:
    print(line)