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

if len1 > len2 > len3:
    with open('3.txt', 'w', encoding='utf-8') as file:
        new_file = file.write(f'3.txt\n{len3}\n{text3}\n2.txt\n{len2}\n{text2}\n1.txt\n{len1}\n{text1}')
elif len1 > len3 > len2:
    with open('2.txt', 'w', encoding='utf-8') as file:
        new_file = file.write(f'2.txt\n{len2}\n{text2}\n3.txt\n{len3}\n{text3}\n1.txt\n{len1}\n{text1}')
elif len2 > len1 > len3:
    with open('3.txt', 'w', encoding='utf-8') as file:
        new_file = file.write(f'3.txt\n{len3}\n{text3}\n1.txt\n{len1}\n{text1}\n2.txt\n{len2}\n{text2}')
elif len2 > len3 > len1:
    with open('1.txt', 'w', encoding='utf-8') as file:
        new_file = file.write(f'1.txt\n{len1}\n{text1}\n3.txt\n{len3}\n{text3}\n2.txt\n{len2}\n{text2}')
elif len3 > len1 > len2:
    with open('2.txt', 'w', encoding='utf-8') as file:
        new_file = file.write(f'2.txt\n{len2}\n{text2}\n1.txt\n{len1}\n{text1}\n3.txt\n{len3}\n{text3}')
elif len3 > len2 > len1:
    with open('1.txt', 'w', encoding='utf-8') as file:
        new_file = file.write(f'1.txt\n{len1}\n{text1}\n2.txt\n{len2}\n{text2}\n3.txt\n{len3}\n{text3}')

print(new_file)
