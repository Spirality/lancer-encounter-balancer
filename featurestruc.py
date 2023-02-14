from LCP_Reader import LCP_Reader
from pathlib import Path
import os

# There are a number of different formats of feature, and my knowledge of python is limited. Making four diff classes is the best I've got
class Trait_Feature:
    def __init__(self, id, name, type, origin, locked, effect, tags=[]):
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
    
    def desc(self):
        print(self.effect)

class Weapon_Feature:
    def __init__(self, id, name, type, weapon_type, origin, locked, damage, range, attack_bonus=[0,0,0], tags=[], effect=None, on_hit=None, on_crit=None):
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
    
    def desc(self):
        print(self.effect)

class System_Feature:
    def __init__(self, id, name, type, origin, locked, effect, tags=[]):
        self.id = id
        self.name = name
        self.type = type
        self.origin = origin
        self.locked = locked
        self.tags = tags
        self.effect = effect
    
    def desc(self):
        print(self.effect)

class Reaction_Feature:
    def __init__(self, id, name, type, origin, locked, trigger, effect, tags=[]):
        self.id = id
        self.name = name
        self.type = type
        self.origin = origin
        self.locked = locked
        self.tags = tags
        self.trigger = trigger
        self.effect = effect
    
    def desc(self):
        print(self.effect)

class Tech_Feature:
    def __init__(self, id, name, type, origin, locked, effect, tech_type, tags=[], attack_bonus=[0,0,0]):
        self.id = id
        self.name = name
        self.type = type
        self.origin = origin
        self.locked = locked
        self.effect = effect
        self.tags = tags
        self.tech_type = tech_type
        self.attack_bonus = attack_bonus
    
    def desc(self):
        print(self.effect)

def load_feature(feature_data):
    category = str.casefold(feature_data["type"])
    # Capitalization matters, apparently
    if category == "trait":
        return Trait_Feature(id=feature_data["id"], name=feature_data["name"], type=feature_data["type"], origin=feature_data["origin"], locked=feature_data["locked"], effect=feature_data["effect"], tags=feature_data.get("tags", []))
    elif category == "weapon":
        return Weapon_Feature(id=feature_data["id"], name=feature_data["name"], type=feature_data["type"], weapon_type=feature_data["weapon_type"], origin=feature_data["origin"], locked=feature_data["locked"], range=feature_data["range"], damage=feature_data.get("damage", [0,0,0]), attack_bonus=feature_data.get("attack_bonus", [0,0,0]), tags=feature_data.get("tags", []), effect=feature_data.get("effect", None), on_hit=feature_data.get("on_hit", None), on_crit=feature_data.get("on_crit", None))
    elif category == "system":
        return System_Feature(id=feature_data["id"], name=feature_data["name"], type=feature_data["type"], origin=feature_data["origin"], locked=feature_data["locked"], effect=feature_data["effect"], tags=feature_data.get("tags", []))
    elif category == "reaction":
        return Reaction_Feature(id=feature_data["id"], name=feature_data["name"], type=feature_data["type"], origin=feature_data["origin"], locked=feature_data["locked"], trigger=feature_data["trigger"], effect=feature_data["effect"], tags=feature_data.get("tags", []))
    elif category == "tech":
        return Tech_Feature(id=feature_data["id"], name=feature_data["name"], type=feature_data["type"], origin=feature_data["origin"], locked=feature_data["locked"], effect=feature_data["effect"], tech_type=feature_data["tech_type"], tags=feature_data.get("tags", []), attack_bonus=feature_data.get("attack_bonus", [0,0,0]))
    else:
        raise ValueError("Not a supported Feature type!")

loaded_features = {}
def featload():
    for filename in Path('LCPs').glob('*.lcp'): # Loop through each LCP file
        print(filename) # Debug shenanigans, delete later
        lcpr = LCP_Reader(filename) # Load the LCP info and save to a name
        for entry in lcpr.npc_features: # Loop through each feature in the json
            thing = load_feature(entry) # Just saving this expression to 'thing' for easy typing
            loaded_features.update({thing.name: thing}) # Push the feature entry to the loaded_features dictionary
        x = len(loaded_features) # More debug
        print(f'{x} NPC Features loaded from {filename}.') # More debug
    return loaded_features # Hand off the master list of features