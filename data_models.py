import random
from dataclasses import dataclass

from typing import List, Optional,Dict,Any
##########################################################################
##########################################################################
##########################################################################
##########################################################################
# Item classes
@dataclass
class Item:
    name: str
    item_type: str
    rarity: str

@dataclass
class Weapon(Item):
    damage: int
    armor_penetration: Optional[int] = None
    mana_bonus: Optional[int] = None
    stealth_bonus: Optional[int] = None
    poison: Optional[int] = None
    strenght: Optional[int] = None
    stamina: Optional[int] = None
    agility: Optional[int] = None
    intelligence: Optional[int] = None

@dataclass
class Armor(Item):
    defense: int
    durability: int
    strength: Optional[int] = None
    stamina: Optional[int] = None
    agility: Optional[int] = None
    intelligence: Optional[int] = None
    stealth_bonus: Optional[int] = None
    fire_resistance: Optional[int] = None

@dataclass
class Consumable(Item):
    heal: Optional[int] = None
    resistance: Optional[int] = None
    duration: Optional[str] = None
    mana_restore: Optional[int] = None
    strength_bonus: Optional[int] = None

@dataclass
class LootTable:
    weapons: Dict[int, Weapon]
    armors: Dict[int, Armor]
    consumables: Dict[int, Consumable]

class LootManager:
    def __init__(self):
        self.loot_table = LootTable(
            weapons={
                1: Weapon("Broken Sword", "1 handed weapon", "common", damage=18),
                2: Weapon("War Axe", "1 handed weapon", "rare", damage=35, armor_penetration=5, strenght=2),
                3: Weapon("Magical Staff", "2 handed weapon", "epic", damage=27, mana_bonus=20, intelligence=4),
                4: Weapon("Dagger of Shadows", "1 handed weapon", "epic", damage=20, stealth_bonus=10, poison=5, agility=3),
                5: Weapon("Flaming Sword", "1 handed weapon", "legendary", damage=55, armor_penetration=10, strenght=5),
                6: Weapon("Thunder Hammer", "2 handed weapon", "legendary", damage=65, strenght=5, stamina=3),
                7: Weapon("Elven Bow", "ranged weapon", "rare", damage=30, agility=3),
                8: Weapon("Shadow Spear", "2 handed weapon", "epic", damage=45, stealth_bonus=8, agility=4),
                9: Weapon("Frozen Scythe", "2 handed weapon", "legendary", damage=60, intelligence=5),
                10: Weapon("Orcish Cleaver", "1 handed weapon", "rare", damage=40, strenght=3),
            },
            armors={
                101: Armor("Iron Helmet", "helmet", "common", defense=5, durability=80),
                102: Armor("Steel Chestplate", "chest plate", "rare", defense=15, durability=100, strength=2),
                103: Armor("Reinforced Greaves", "pants", "rare", defense=10, durability=90, stamina=2),
                104: Armor("Dragon Helm", "helmet", "legendary", defense=25, durability=200, fire_resistance=10, strength=3),
                105: Armor("Dragon Chestplate", "chest plate", "legendary", defense=50, durability=300, fire_resistance=20, strength=5),
                106: Armor("Dragon Greaves", "pants", "legendary", defense=35, durability=250, fire_resistance=15, stamina=4),
                107: Armor("Assassin Hood", "helmet", "epic", defense=8, durability=120, agility=4),
                108: Armor("Mystic Robes", "chest plate", "epic", defense=12, durability=90, intelligence=5),
                109: Armor("Shadow Cloak", "cloak", "legendary", defense=15, durability=150, stealth_bonus=10, agility=5),
                110: Armor("Paladin Gauntlets", "gloves", "rare", defense=6, durability=110, strength=2),
            },
            consumables={
                201: Consumable("Weak Healing Potion", "consumable", "common", heal=25),
                202: Consumable("Strong Healing Potion", "consumable", "rare", heal=50),
                203: Consumable("Resistance Potion", "consumable", "rare", resistance=30, duration="5 min"),
                204: Consumable("Mana Potion", "consumable", "rare", mana_restore=50),
                205: Consumable("Elixir of Strength", "consumable", "epic", strength_bonus=10, duration="5 min"),
            }
        )
##########################################################################
##########################################################################
##########################################################################
##########################################################################
#enemy data classes
@dataclass
class EnemyStats:
    health: int
    armor: int
    healing_per_round: int
    damage: int

@dataclass
class EnemyAbilities:
    ability_name: Optional[str] = None
    type: Optional[str] = None
    effect_info: Optional[str] = None
    power: Optional[int] = None
@dataclass
class EnemyData:
    name: str
    strength_type: str
    stats: EnemyStats
    abilities: EnemyAbilities
@dataclass
class EnemyTable:
    enemy : List[EnemyData]
class EnemyManager:
    def __init__(self):
        self.enemy_list = EnemyTable(enemy =[
            EnemyData("slime", "weak", EnemyStats(30, 0, 1, 5),
                      EnemyAbilities("split", "passive", "duplicates on death")),
            EnemyData("goblin", "weak", EnemyStats(50, 5, 2, 10),
                      EnemyAbilities("quick strike", "damage", "", 15)),
            EnemyData("giant_rat", "weak", EnemyStats(40, 2, 1, 7),
                      EnemyAbilities("infectious bite", "damage", "poison", 10)),
            EnemyData("skeleton_warrior", "medium", EnemyStats(80, 10, 0, 15),
                      EnemyAbilities("bone_shield", "buff", "", 10)),
            EnemyData("orc_grunt", "medium", EnemyStats(120, 15, 3, 20),
                      EnemyAbilities("rage", "buff", "increased attack for 3 rounds", 10)),
            EnemyData("shadow_assassin", "medium", EnemyStats(70, 5, 0, 25),
                      EnemyAbilities("shadow_step", "evasion", "dodges next attack")),
            EnemyData("fire_elemental", "strong", EnemyStats(150, 20, 5, 30),
                      EnemyAbilities("flame_burst", "damage", "burn", 40)),
            EnemyData("stone_golem", "strong", EnemyStats(200, 50, 2, 20),
                      EnemyAbilities("earthquake", "damage", "stuns target", 50)),
            EnemyData("vampire_lord", "strong", EnemyStats(180, 15, 10, 25),
                      EnemyAbilities("life_drain", "heal", "heals for damage dealt", 20))])
##########################################################################
##########################################################################
##########################################################################
##########################################################################
#encounter,vendor,storage data classes
class Encounter:
    def __init__(self):
        self.encounter = []
class Vendor:
    def __init__(self):
        self.vendor = []
class Storage:
    def __init__(self):
        self.storage = []
##########################################################################
##########################################################################
##########################################################################
##########################################################################
#player stats data classes
@dataclass
class PlayerAbilities:
    ability_name: Optional[str] = None
    type: Optional[str] = None
    effect_info: Optional[str] = None
    power: Optional[int] = None
@dataclass
class PlaterStats:
    health:int
    armor:int
    healing_per_round:int
    damage:int
    strenght: int
    stamina: int
    agility: int
    intelligence: int
@dataclass
class PlayerAll:
    name:str
    stats: PlaterStats
    abilities:PlayerAbilities

class Player:
    def __init__(self):
        self.player_stats = PlayerAll("Alex",PlaterStats(100,5,2,20,strenght=10,stamina=10,agility=10,intelligence=10),PlayerAbilities())

##########################################################################
#player equip
@dataclass
class PlayerEquipAll:
    weapon: List[Weapon]
    chestplate: List[Armor]
    pants: List[Armor]
    helmet: List[Armor]
    consumables: List[Consumable]
class PlayerEquipTable:
    def __init__(self):
        self.player_equip_table = PlayerEquipAll(weapon=[],
                                               chestplate=[],
                                               pants=[],
                                               helmet=[],
                                               consumables=[])
##########################################################################
# player bag class
@dataclass
class PlayerBag:
    bag: List[Dict[Any, Any]]
class PlayerBagTable:
    def __init__(self):
        self.bag = PlayerBag(bag=[])
