import random
from dataclasses import dataclass
from typing import List,Dict,Any
from data_models import Vendor, LootManager


@dataclass
class MoveItemSetup:
    source: List[Dict[str, Any]]
    target: List[Dict[str, Any]]
    item: Dict[str, Any]
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

class VendorGen():
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
