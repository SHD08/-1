def item_func(item, x):# TODO Напишите функцию для поиска индекса товара
    if x in item:
        return item.index(x)

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']


for find_item in ['банан', 'груша', 'персик']:
    index_item = item_func(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
