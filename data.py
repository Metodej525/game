import random

from data_model import LootTableModel, Vendor

player_stats = {
    'You':{
        'stats':{'health':100,'armor':5,'healing per round':2,'damage':20},
        'abilities':{}}}

weak_enemy = {
    "slime": {
        "stats": {"health": 30, "armor": 0, "healing per round": 1, "damage": 5},
        "abilities": {"split": {"type": "passive", "effect": "duplicates on death"}}
    },
    "goblin": {
        "stats": {"health": 50, "armor": 5, "healing per round": 2, "damage": 10},
        "abilities": {"quick strike": {"type": "damage", "power": 15}}
    },
    "giant_rat": {
        "stats": {"health": 40, "armor": 2, "healing per round": 1, "damage": 7},
        "abilities": {"infectious bite": {"type": "damage", "power": 10, "effect": "poison"}}
    }
}

medium_enemy = {
    "skeleton_warrior": {
        "stats": {"health": 80, "armor": 10, "healing per round": 0, "damage": 15},
        "abilities": {"bone_shield": {"type": "buff", "power": 10}}
    },
    "orc_grunt": {
        "stats": {"health": 120, "armor": 15, "healing per round": 3, "damage": 20},
        "abilities": {"rage": {"type": "buff", "power": 10, "effect": "increased attack for 3 rounds"}}
    },
    "shadow_assassin": {
        "stats": {"health": 70, "armor": 5, "healing per round": 0, "damage": 25},
        "abilities": {"shadow_step": {"type": "evasion", "effect": "dodges next attack"}}
    }
}

strong_enemy = {
    "fire_elemental": {
        "stats": {"health": 150, "armor": 20, "healing per round": 5, "damage": 30},
        "abilities": {"flame_burst": {"type": "damage", "power": 40, "effect": "burn"}}
    },
    "stone_golem": {
        "stats": {"health": 200, "armor": 50, "healing per round": 2, "damage": 20},
        "abilities": {"earthquake": {"type": "damage", "power": 50, "effect": "stuns target"}}
    },
    "vampire_lord": {
        "stats": {"health": 180, "armor": 15, "healing per round": 10, "damage": 25},
        "abilities": {"life_drain": {"type": "heal", "power": 20, "effect": "heals for damage dealt"}}
    }
}

encounter = {}
vendor = {}
storage = {}
player_equip = {}
player_backpack = {}


all_items = LootTableModel()
vendom_class = Vendor(1)
vendom_class.select_items()