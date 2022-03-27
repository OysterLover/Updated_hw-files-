#файлы в исходном состоянии, для перезаписи необходимо запустить код
with open('1.txt', encoding='utf-8') as file1:
    len1 = len(file1.readlines())

with open('2.txt', encoding='utf-8') as file2:
    len2 = len(file2.readlines())

with open('3.txt', encoding='utf-8') as file3:
    len3 = len(file3.readlines())

with open('1.txt', encoding='utf-8') as file1:
    text1 = file1.read()

with open('2.txt', encoding='utf-8') as file2:
    text2 = file2.read()

with open('3.txt', encoding='utf-8') as file3:
    text3 = file3.read()

with open('2.txt', 'w', encoding='utf-8') as file:
    file.write(f'file2\n{len2}\n{text2}\nfile1\n{len1}\n{text1}\nfile3\n{len3}\n{text3}')

with open('2.txt', 'r', encoding='utf-8') as file:
    file_new = file.read()

print(file_new)








