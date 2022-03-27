
with open('recipes.txt', 'r', encoding="utf-8") as file:
    data = file.readlines()
#    print(data)
    i = 0
    keys = []
    values = []

    r = 2
    while i <= len(data) and r <= len(data):
        counter = i + 1
        keys.append(data[i].strip())
        while r - int(data[counter].strip()) < 0:
            values.append(data[r].strip())
            r += 1
        i = counter + int(data[counter].strip()) + 2

#cook_book = dict.fromkeys(keys)
    print(keys)
    print(values)
#print(keys)


