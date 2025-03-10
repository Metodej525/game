import random
from dataclasses import dataclass

from typing import List, Optional,Dict,Any
##########################################################################
##########################################################################
##########################################################################
##########################################################################
#item classes
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

@dataclass
class Armor(Item):
    defense: int
    durability: int
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
    weapons: List[Weapon]
    armors: List[Armor]
    consumables: List[Consumable]
class LootManager:
    def __init__(self):
        self.loot_table = LootTable(
            weapons=[
                Weapon("broken sword", "1 handed weapon", "common", random.randint(15, 20)),
                Weapon("war axe", "1 handed weapon", "rare", random.randint(30, 40), armor_penetration=5),
                Weapon("magical staff", "2 handed weapon", "epic", random.randint(25, 30), mana_bonus=20),
                Weapon("dagger of shadows", "1 handed weapon", "epic", random.randint(18, 22), stealth_bonus=10, poison=5),
            ],
            armors=[
                Armor("iron helmet", "helmet", "common", 5, 80),
                Armor("steel chestplate", "chest plate", "rare", 15, 100),
                Armor("reinforced greaves", "pants", "rare", 10, 90),
                Armor("dragon helm", "helmet", "legendary", 25, 200, fire_resistance=10),
                Armor("dragon chestplate", "chest plate", "legendary", 50, 300, fire_resistance=20),
                Armor("dragon greaves", "pants", "legendary", 35, 250, fire_resistance=15),
            ],
            consumables=[
                Consumable("weak healing potion", "consumable", "common", heal=25),
                Consumable("strong healing potion", "consumable", "rare", heal=50),
                Consumable("resistance potion", "consumable", "rare", resistance=30, duration="5 min"),
                Consumable("mana potion", "consumable", "rare", mana_restore=50),
                Consumable("elixir of strength", "consumable", "epic", strength_bonus=10, duration="5 min"),
            ]
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
@dataclass
class PlayerAll:
    name:str
    stats: PlaterStats
    abilities:PlayerAbilities

class Player:
    def __init__(self):
        self.player_stats = PlayerAll("Alex",PlaterStats(100,5,2,20),PlayerAbilities())
##########################################################################
#player equip
@dataclass
class PlayerEquipAll:
    weapon: List[Dict[Any,Any]]
    chestplate: List[Dict[Any,Any]]
    pants: List[Dict[Any,Any]]
    helmet: List[Dict[Any,Any]]
    consumables: List[Dict[Any,Any]]
class PlayerEquipTable:
    def __init__(self):
        self.playerEquipTable = PlayerEquipAll(weapon=[],
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