import random

from data_models import LootTable





player_equip = {}
player_backpack = {}


player = Player().player_stats.abilities.ability_name
if player is None:
    print('There is no ability')