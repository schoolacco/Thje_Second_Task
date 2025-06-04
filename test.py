from Module import Item
class1 = Item(1, 1, 1, 1, 1, 1, 1, 1, 1)
class2 = Item(2,2,2,2,2,2,2,2,2)
list = Item.get_instances()
for item in list:
    print(item.name)