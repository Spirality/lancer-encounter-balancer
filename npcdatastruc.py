from LCP_Reader import LCP_Reader
from pathlib import Path
import os

# As of 3/2/2023, feature handling will no longer happen within the import space, but will handle the master list as an argument to save memory
class NPC_Class:
    # A class of NPC dictates how it will function in combat
    def __init__(self, name, role, info, stats, base_features, opt_features, loaded_features):
        self.name = name
        self.role = role
        self.info = info
        self.stats = stats
        self.loaded_features = loaded_features
        self.base_features = {x:self.loaded_features.get(x) for x in base_features} #dict
        self.opt_features = {x:self.loaded_features.get(x) for x in opt_features} #dict
        self.class_features = {**self.base_features, **self.opt_features}

    def get_hull(self, tier):
        return self.stats.get_hull(tier=tier)

    def get_agility(self, tier):
        return self.stats.get_agility(tier=tier)

    def get_systems(self, tier):
        return self.stats.get_systems(tier=tier)

    def get_engineering(self, tier):
        return self.stats.get_engineering(tier=tier)


class NPC_Class_Stats:
  # NPC Combat Stats, might not use them but we're collecting them in case we need them later
  # Need to attach a default to most of these, since some LCPs have these defined and some don't
    def __init__(self, armor=None, hp=None, evade=None, edef=None, heatcap=None, speed=None, sensor=None, save=None, hull=None, agility=None, systems=None, engineering=None, size=None, activations=None, stress=[1,1,1], structure=[1,1,1]):
        self.armor = armor
        self.hp = hp
        assert self.hp is not None, f'{self.name} must have a value for HP!'
        # Can't have a unit without HP, but tbh that's basically the only thing you need for a character. See drones.
        self.evade = evade
        self.edef = edef
        self.heatcap = heatcap
        self.speed = speed
        self.sensor = sensor
        self.save = save
        self.hull = hull
        self.agility = agility
        self.systems = systems
        self.engineering = engineering
        self.size = size
        self.activations = activations
        self.stress = stress
        self.structure = structure

    # These are mostly just here for later
    # Between saving all three values of the tier and having a separate class for each tier, I chose to just save the list
    def get_hull(self, tier):
        return self.hull[tier - 1]

    def get_agility(self, tier):
        return self.agility[tier - 1]

    def get_systems(self, tier):
        return self.systems[tier - 1]

    def get_engineering(self, tier):
        return self.engineering[tier - 1]


def load_npc_class(npc_data, loaded_features):
    stats = NPC_Class_Stats(**npc_data["stats"])
    return NPC_Class(name=npc_data["name"], role=npc_data["role"], info=npc_data["info"], stats=stats, base_features=npc_data["base_features"], opt_features=npc_data["optional_features"], loaded_features=loaded_features)
    # Stats is a separate thing because we won't really need much of it for the initial part of the program
    # Also it's a whole different block in the json file so this is just easier to parse

# This is for when we actually make an NPC, not part of the loading process
class NPC:
    # First part, identifications
    def __init__(self, name, npc_class, tier):
        self.name = name
        self.npc_class = npc_class
        self.tier = tier
        self.templates = {}
        self.allowed_features = npc_class.class_features
        self.features = npc_class.base_features
        self.bonuses = {}
        self.activations = npc_class.stats.activations[self.tier - 1]
        self.weight = 1
        # weight is basically the value of fielding the NPC. Grunts will have .25, Elites and Vets get 2 (3 if the templates are stacked), and 4 for Ultras
        # this value will get multiplied/modified if the NPC is fielded with classes that combo with it, like Mirage + Demolisher
    
    # Second part, defining functions. More to come as we need them
    def get_baseHASE(self):
        base_hull = self.npc_class.get_hull(tier=self.tier)
        base_agility = self.npc_class.get_agility(tier=self.tier)
        base_systems = self.npc_class.get_systems(tier=self.tier)
        base_engineering = self.npc_class.get_engineering(tier=self.tier)
        return (base_hull, base_agility, base_systems, base_engineering)
    
    def get_basefeats(self):
        base_features = self.npc_class.base_features
        return base_features
    
    def calc_bonus(self):
        for entry in self.features:
            self.bonuses.update(entry.bonus)

    def add_template(self, template):
        self.templates[template.name] = template
        self.allowed_features.update(template.features.items())
        self.features.update({x:self.npc_class.loaded_features.get(x) for x in template.base_features if x in self.npc_class.loaded_features})

    def rm_template(self, template):
        if template.name in self.templates:
            del self.templates[template.name]
            for entry in template.get_features(): #For each feature of the template
                del self.allowed_features[entry] #remove each feature from the allowed features list
                if entry in self.features:
                    del self.features[entry] #then remove any that have been assigned
                    return True
        else:
            return False

def npc_load(loaded_features):
    loaded_npcs = {}
    for filename in Path('LCPs').glob('*.lcp'): # Loop through each LCP file
        #print(filename) # Debug shenanigans, delete later
        lcpr = LCP_Reader(filename) # Load the LCP info and save to a name
        for entry in lcpr.npc_classes: # Loop through each NPC class in the json
            thing = load_npc_class(entry, loaded_features) # Just saving this expression to 'thing' for easy typing
            loaded_npcs.update({thing.name: thing}) # Push the NPC entry to the loaded_npcs dictionary. Might be an issue if two LCPs have the same name of NPC?
        #x = len(loaded_npcs) # More debug
        #print(f'{x} NPC Classes loaded from {filename}.') # More debug
    return loaded_npcs # Hand off the master list of NPCs!

# Call for specific stats of an NPC like this: loaded_npcs['CARRIER'].stats.hp
# loaded_npcs is the dict of NPCs sorted by name, stats is the list you want, and hp is the value
# Here are two examples for creating an NPC using all this info:
# bob_the_gladiator = NPC("Bob the Gladiator", loaded_npcs['GLADIATOR'], tier=2)
# jane_the_carrier = NPC("Jane the Carrier", loaded_npcs['CARRIER'], tier=1)