import random
from dataclasses import dataclass
from typing import List,Dict,Any
from data_models import Vendor, LootManager, PlayerBagTable, Storage


class SelectMoveItem:
    def __init__(self):
        self.item_select = input("Jaky item chces presunout?").lower()
class SelectMoveSource:
    def __init__(self):
        self.source_select = input("Odkud to chces presunout? backpack/storage").lower()
        if self.source_select == "backpack":
            self.source_select = PlayerBagTable().bag
        elif self.source_select == "storage":
            self.source_select = Storage().storage
        else:
            self.source_select = None
            print("Invalid input")
class SelectMoveTarget:
    def __init__(self):
        self.source_target = input("Kam chces presunout? backpack/storage").lower()
        if self.source_target == "backpack":
            self.source_target = PlayerBagTable().bag
        elif self.source_target == "storage":
            self.source_target = Storage().storage
        else:
            self.source_target = None
            print("Invalid input")
@dataclass
class MoveItemSetup:
    source: List[Dict[str, Any]]
    target: List[Dict[str, Any]]
    item: Dict[str, Any]
    item_select: str
class MoveItem:
    def __init__(self,setup: MoveItemSetup):
        self.source = setup.source
        self.target = setup.target
        self.item = setup.item
    def move(self)-> bool:
        if self.item in self.source:
            item_index = self.source.index(self.item)
            item_move = self.source[item_index].copy()
            self.source.pop(item_index)
            self.target.append(item_move)
            return True
        return False

class VendorGen:
    def __init__(self,stage):
        self.vendor_table = Vendor().vendor
        self.loot_table = LootManager().loot_table
        self.stage = stage
    def generate_items(self):
        gen_items = []
        for category in self.loot_table:
            for item in category:
                if item.rarity == "common":
                    gen_items.append(item)
        vendor_sample = random.sample(gen_items,4)
        return vendor_sample
