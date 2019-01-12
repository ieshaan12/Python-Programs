def displayInventory(inventory):
    for k in inventory.keys():
        v=inventory[k]
        print('Item:'+k+' Numbers:'+str(v))
def addToInventory(inventory,addedItems):
    for item in addedItems:
        if item not in inventory:
            inventory.setdefault(item,1)
        else:
            inventory[item]+=1
        
    displayInventory(inventory)
i={'dagger':3,'knife':2,'sword':5}
#displayInventory(i)
add=['catapults','sword','sword','sword','sword']
addToInventory(i,add)
