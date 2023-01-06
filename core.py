import json
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
    def __init__(self, armor, hp, evade, edef, heatcap, speed, sensor, save, hull, agility, systems, engineering, size, activations):
      # TODO: Make this list auto-populate instead of all this being written out manually
        self.armor = armor
        self.hp = hp
        assert self.hp is not None, f'{self_name} must have a value for HP!'
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

lcp_data = open('npc_classes.json')
# Later on we're gonna make this populate a list of LCPs and merge all the data before sifting through, or something like that. Just PH for now

loaded_json = json.load(lcp_data)
# for i in loaded_json:
x = len(loaded_json)
print(f'{x} NPC Classes loaded.')

# Most of the above json stuff is placeholder until I can figure out what I'm actually doing with loading files and sorting through info

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

# bob_the_gladiator = NPC("Bob the Gladiator", Gladiator, tier=2)
# print(bob_the_gladiator.get_HASE())
