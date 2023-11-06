cook_book = {
    'Омлет': [
        {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
        {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
        {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
    'Утка по-пекински': [
        {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
        {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
        {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
        {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
    'Запеченный картофель': [
        {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
        {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
        {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
}


def print_dish_info(dish_name, dish_data):
    print(dish_name)
    print(f'Ингредиентов: {len(dish_data)}')
    for ingredient in dish_data:
        print(f'{ingredient["ingredient_name"]} | {ingredient["quantity"]} | {ingredient["measure"]}')


for dish_name in cook_book:
    if dish_name in cook_book:
        print_dish_info(dish_name, cook_book[dish_name])
    else:
        print(f'Ингредиентов для блюда "{dish_name}" нет в рецепте')


def print_dish_info(dish_name, dish_data, file):
    file.write(dish_name + '\n')
    file.write(f'Ингредиентов: {len(dish_data)}\n')
    for ingredient in dish_data:
        file.write(f'{ingredient["ingredient_name"]} | {ingredient["quantity"]} | {ingredient["measure"]}\n')


with open('recipes.txt', 'w') as file:
    for dish_name in cook_book:
        file.write('\n')
        if dish_name in cook_book:
            print_dish_info(dish_name, cook_book[dish_name], file)
        else:
            file.write(f'Ингредиентов для блюда "{dish_name}" нет в рецепте\n')

