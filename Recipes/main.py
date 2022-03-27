from pprint import pprint


def make_cook_book(a_file):

    cook_book = {}

    with open(a_file, 'r', encoding='utf-8') as file:


        while True:

            name_dish = file.readline().strip()

            if name_dish.strip() == '':
                break

            quantity = int(file.readline())

            cook_book[name_dish] = []

            for i in range(quantity):
                data = file.readline().split(' | ')
                ingredients = {'ingredient_name': data[0], 'quantity': int(data[1]), 'measure': data[2].strip()}
                cook_book[name_dish].append(ingredients)

            file.readline()

    return cook_book

cook_book = make_cook_book('recipes.txt')
#pprint(cook_book)


def get_shop_list_by_dishes(dishes, persons:int):
    recipes = {}
    ing_list = []

    for i in range(len(cook_book[dishes])):
        ing_name = cook_book[dishes][i]['ingredient_name']
        ing_list.append(ing_name)
    recipes[dishes] = ing_list

    for i in range(len(recipes[dishes])):
        recipes[dishes][i] = []
        ing_info = {'ingredient_name': cook_book[dishes][i]['ingredient_name'],
                    'measure': cook_book[dishes][i]['measure'],
                    'quantity': cook_book[dishes][i]['quantity'] * persons}
        recipes[dishes][i].append(ing_info)

    return recipes[dishes]

#pprint(get_shop_list_by_dishes('Запеченный картофель', 3))