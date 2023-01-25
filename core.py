from LCP_Reader import LCP_Reader
import json
import os
from pathlib import Path

class NPC_Class:
    # A class of NPC dictates how it will function in combat
    def __init__(self, name, role, info, stats, base_features, opt_features):
        self.name = name
        self.role = role
        self.info = info
        self.stats = stats
        self.base_features = base_features
        self.opt_features = opt_features

    def get_hull(self, tier):
        return self.stats.get_hull(tier=tier)

    def get_agility(self, tier):
        return self.stats.get_agility(tier=tier)

    def get_systems(self, tier):
        return self.stats.get_systems(tier=tier)

    def get_engineering(self, tier):
        return self.stats.get_engineering(tier=tier)


class NPC_Class_Stats:
  # These stats are largely unnecessary for the initial project of an "at a glance" combat balancer tool, but we're taking them into account anyway
  # NOTE 1/12/23 - Loading Suldan NPCs gets weird when expecting the default NPC stat table because they added Stress and Structure. More elegant way to do this? v
    def __init__(self, armor, hp, evade, edef, heatcap, speed, sensor, save, hull, agility, systems, engineering, size, activations, stress, structure):
      # TODO: Make this list auto-populate instead of all this being written out manually
        self.armor = armor
        self.hp = hp
        assert self.hp is not None, f'{self.name} must have a value for HP!'
        # Learning error catching :)
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

    def get_hull(self, tier):
        return self.hull[tier - 1]

    def get_agility(self, tier):
        return self.agility[tier - 1]

    def get_systems(self, tier):
        return self.systems[tier - 1]

    def get_engineering(self, tier):
        return self.engineering[tier - 1]


def load_npc_class(npc_data):
  # This is the part where we actually load the json and start organizing it
  # Time to figure out how to make it automatically sort out all the different classes that it finds...
    stats = NPC_Class_Stats(**npc_data["stats"])
    return NPC_Class(name=npc_data["name"], role=npc_data["role"], info=npc_data["info"], stats=stats, base_features=npc_data["base_features"], opt_features=npc_data["optional_features"])

class NPC:
    # Putting the band together
    def __init__(self, name, npc_class, tier):
        self.name = name
        self.npc_class = npc_class
        self.tier = tier

    def get_HASE(self):
        hull = self.npc_class.get_hull(tier=self.tier)
        agility = self.npc_class.get_agility(tier=self.tier)
        systems = self.npc_class.get_systems(tier=self.tier)
        engineering = self.npc_class.get_engineering(tier=self.tier)
        return (hull, agility, systems, engineering)


loaded_npcs = {}
for filename in Path('LCPs').glob('*.lcp'):
    lcpr = LCP_Reader(filename)
    npc_class_data = open('npc_classes.json')
    loaded_json = json.load(npc_class_data)
    for entry in loaded_json:
        # thank you Tetragramm for correcting my foolish ways
        thing = load_npc_class(entry)
        print(thing.name)
        loaded_npcs.update({thing.name: thing})
    x = len(loaded_json)
    print(f'{x} NPC Classes loaded from {filename}.')

#print(loaded_npcs['CARRIER'].stats.hp)
bob_the_gladiator = NPC("Bob the Gladiator", loaded_npcs['GLADIATOR'], tier=2)
#print(bob_the_gladiator.get_HASE())