import random




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
class LootTableModel:
    def __init__(self):
        self.loot_table = [
            # Weapons
            {'broken sword': {
                "1 handed weapon": {"rarity": "common", "damage": random.randint(15, 20)}}},
            {'war axe': {
                "1 handed weapon": {"rarity": "rare", "damage": random.randint(30, 40), "armor penetration": 5}}},
            {'magical staff': {
                "2 handed weapon": {"rarity": "epic", "damage": random.randint(25, 30), "mana_bonus": 20}}},
            {'dagger of shadows': {
                "1 handed weapon": {"rarity": "epic", "damage": random.randint(18, 22), "stealth_bonus": 10,
                                    "poison": 5}}},

            # Armor Sets
            {'iron helmet': {"helmet": {"rarity": "common", "defense": 5, "durability": 80}}},
            {'steel chestplate': {"chest plate": {"rarity": "rare", "defense": 15, "durability": 100}}},
            {'reinforced greaves': {"pants": {"rarity": "rare", "defense": 10, "durability": 90}}},

            # Dragon armor set
            {'dragon helm': {
                "helmet": {"rarity": "legendary", "defense": 25, "durability": 200, "fire resistance": 10}}},
            {'dragon chestplate': {
                "chest plate": {"rarity": "legendary", "defense": 50, "durability": 300, "fire resistance": 20}}},
            {'dragon greaves': {
                "pants": {"rarity": "legendary", "defense": 35, "durability": 250, "fire resistance": 15}}},

            # Shields
            {'wooden shield': {"shield": {"rarity": "common", "defense": 10, "durability": 50}}},
            {'steel shield': {"shield": {"rarity": "rare", "defense": 25, "durability": 150, "block chance": 15}}},
            {'tower shield': {"shield": {"rarity": "epic", "defense": 40, "durability": 250, "block chance": 30}}},

            # Consumables
            {'weak healing potion': {"consumable": {"rarity": "common", "heal": 25}}},
            {'strong healing potion': {"consumable": {"rarity": "rare", "heal": 50}}},
            {'resistance potion': {"consumable": {"rarity": "rare", "resistance": 30, "duration": "5 min"}}},
            {'mana potion': {"consumable": {"rarity": "rare", "mana_restore": 50}}},
            {'elixir of strength': {"consumable": {"rarity": "epic", "strength_bonus": 10, "duration": "5 min"}}}
        ]


