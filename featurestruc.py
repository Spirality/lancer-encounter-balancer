from LCP_Reader import LCP_Reader
from pathlib import Path
import os

# There are a number of different formats of feature, and my knowledge of python is limited. Making four diff classes is the best I've got
class Trait_Feature:
    def __init__(self, id, name, type, origin, locked, effect, tags=None):
        self.id = id
        self.name = name
        self.type = type
        # Only seen Trait, System, Weapon, Reaction, and Tech
        self.origin = origin
        # This is a list
        self.tags = tags
        self.locked = locked
        # Only true or false
        self.effect = effect

class Weapon_Feature:
    def __init__(self, id, name, type, weapon_type, origin, locked, damage, range, attack_bonus=None, tags=None, effect=None, on_hit=None, on_crit=None):
        self.id = id
        self.name = name
        self.type = type
        self.weapon_type = weapon_type
        self.origin = origin
        self.locked = locked
        self.effect = effect
        self.on_hit = on_hit
        self.on_crit = on_crit
        self.damage = damage
        self.attack_bonus = attack_bonus
        self.range = range
        self.tags = tags

class System_Feature:
    def __init__(self, id, name, type, origin, locked, effect, tags=None):
        self.id = id
        self.name = name
        self.type = type
        self.origin = origin
        self.locked = locked
        self.tags = tags
        self.effect = effect

class Reaction_Feature:
    def __init__(self, id, name, type, origin, locked, trigger, effect, tags=None):
        self.id = id
        self.name = name
        self.type = type
        self.origin = origin
        self.locked = locked
        self.tags = tags
        self.trigger = trigger
        self.effect = effect

class Tech_Feature:
    def __init__(self, id, name, type, origin, locked, effect, tech_type, tags=None, attack_bonus=None):
        self.id = id
        self.name = name
        self.type = type
        self.origin = origin
        self.locked = locked
        self.effect = effect
        self.tags = tags
        self.tech_type = tech_type
        self.attack_bonus = attack_bonus

def load_feature(feature_data):
    category = str.casefold(feature_data["type"])
    # Capitalization matters, apparently
    if category == "trait":
        return Trait_Feature(id=feature_data["id"], name=feature_data["name"], type=feature_data["type"], origin=feature_data["origin"], locked=feature_data["locked"], effect=feature_data["effect"], tags=feature_data["tags"])
    else:
        print("Not a Trait")
        return False

loaded_features = {}
def lcpload():
    for filename in Path('LCPs').glob('*.lcp'): # Loop through each LCP file
        print(filename) # Debug shenanigans, delete later
        lcpr = LCP_Reader(filename) # Load the LCP info and save to a name
        for entry in lcpr.npc_features: # Loop through each feature in the json
            thing = load_feature(entry) # Just saving this expression to 'thing' for easy typing
            if thing == False:
                continue
            loaded_features.update({thing.name: thing}) # Push the NPC entry to the loaded_features dictionary
        x = len(loaded_features) # More debug
        print(f'{x} NPC Features loaded from {filename}.') # More debug
    return loaded_features # Hand off the master list of features
lcpload()
