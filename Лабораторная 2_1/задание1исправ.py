# TODO Напишите функцию для поиска индекса товара

def find_item_index(items_list, item_to_find):
    try:
        return items_list.index(item_to_find)
    except ValueError:
        return None

# Пример использования
items = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for item in ['банан', 'груша', 'персик']:
    index = find_item_index(items, item)
    if index is not None:
        print(f"Первое вхождение товара '{item}' имеет индекс {index}.")
    else:
        print(f"Товар '{item}' не найден в списке.")
