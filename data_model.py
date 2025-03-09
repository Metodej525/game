



class Vendor:
    def __init__(self,stage):
        self.vendor = []
        self.loot_table = LootTableModel().loot_table
        self.stage = stage
    def select_items(self):
        if self.stage == 1:
            for item in self.loot_table:
                for item_name, item_info in item.items():
                    for rarity,rarity_type in item_info.items():
                        if item[item_name][rarity] == 'common':
                            self.vendor.append(item)
        print(self.vendor)



class ItemMover:
    def __init__(self, source, target, item_name):
        self.source = source  # Např. player_inventory, vendor_inventory
        self.target = target  # Např. home_storage, player_backpack
        self.item_name = item_name
    def move(self):
        item_move = self.source[self.item_name].pop().copy()
        self.target.append(self.source[item_move])
