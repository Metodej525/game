import random
from dataclasses import dataclass
from typing import List,Dict,Any
from data_models import Vendor, LootManager, PlayerBagTable, Storage, Player, PlayerEquipTable, Encounter, EnemyManager


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
        self.rarity_select = None
    def rarity_table(self):
        rarities = ["common","rare","epic","legendary"]
        self.rarity_select = rarities[self.stage]
    def generate_items(self):
        gen_items = []
        for category in self.loot_table:
            for item in category:
                if item.rarity == self.rarity_select:
                    gen_items.append(item)
        vendor_sample = random.sample(gen_items,4)
        return vendor_sample
@dataclass
class PlayerStatsSetup:
    stats: Player
    equip: PlayerEquipTable
class PlayerStatSum:
    def __init__(self,player: PlayerStatsSetup):
        self.player_stats = player.stats.player_stats
        self.player_equip = player.equip.player_equip_table
    def summarize(self):
        stat_list = ["strenght", "stamina", "agility", "intelligence", "damage", "armor", "healing_per_round"]
        for eq_slot in vars(self.player_equip).values():
            if eq_slot:
                for stat in stat_list:
                    value_to_add = getattr(eq_slot, stat, None)
                    if value_to_add is not None:
                        player_value = getattr(self.player_stats.stats, stat)
                        setattr(self.player_stats.stats, stat, player_value + value_to_add)
@dataclass
class EncounterData:
    encouter: Encounter
    enemies:  EnemyManager
class EncounterGen:
    def __init__(self,encounter_data: EncounterData,stage):
        self.enemy_list = encounter_data.enemies.enemy_list
        self.encounter_list = encounter_data.encouter.encounter
        self.stage = stage
        self.enemy_choice = ["weak","medium","strong"]
        self.enemy_weak = []
        self.enemy_medium = []
        self.enemy_strong = []
        self.enemy_stage = [self.enemy_weak,self.enemy_medium,self.enemy_strong]
    def order_enemies(self):
        for enemy in self.enemy_list.enemy:
            if enemy.strength_type == "weak":
                self.enemy_weak.append(enemy)
            elif enemy.strength_type == "medium":
                self.enemy_medium.append(enemy)
            elif enemy.strength_type == "strong":
                self.enemy_strong.append(enemy)
    def generate_enemies(self):
        if self.enemy_stage[self.stage]:
            for _ in range(2):
                self.encounter_list.append(random.choice(self.enemy_stage[self.stage]))




test_test = PlayerStatsSetup(Player(),PlayerEquipTable())
test = PlayerStatSum(test_test)
test.summarize()
