def displayInventory(inventory):
    item_total = 0
    
    print('Inventory:')
    for k, v in inventory.items():
        item_total += v
        print('{}: {}'.format(k, str(v)))
    
    return print('Total number of items: {}'.format(str(item_total)))

def addToInventory(inventory, addedItems):
    for i in addedItems:
        inventory.setdefault(i, 0)
        inventory[i] = inventory[i] + 1
    
    return inventory
    
myInventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

myInventory = addToInventory(myInventory, dragonLoot)
displayInventory(myInventory)