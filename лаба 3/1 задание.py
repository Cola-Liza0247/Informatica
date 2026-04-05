def find_item(items, target):
    for i in range(len(items)):
        if items[i] == target:
            return i
    return None
items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for target_item in ['банан', 'груша', 'персик']:
    index_item = find_item(items_list, target_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{target_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{target_item}' не найден в списке.")