
'''colors = ['red', 'blue', 'green']
data = open('file.txt', 'a') # w( удаляет старые записи и перезаписывает) r w+ r+   a (дописывает и сохраняет предыдущие)
data.writelines(colors) #запись списка
data.write('Line 1\n')
data.write('Line 2\n')
data.close()'''

path = 'file.txt'
data = open('file.txt', 'r')
for line in data:
    print(line)
data.close()

exit()