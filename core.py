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
    def __init__(self, armor, hp, evade, edef, heatcap, speed, sensor, save, hull, agility, systems, engineering, size, activations):
        self.armor = armor
        self.hp = hp
        assert self.hp is not None, f'{self_name} must have a value for HP!'
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
    stats = NPC_Class_Stats(**npc_data["stats"])
    return NPC_Class(name=npc_data["name"], role=npc_data["role"], info=npc_data["info"], stats=stats, base_features=npc_data["base_features"], opt_features=npc_data["optional_features"])

lcp_data = """{
    "id": "npcc_ace",
    "name": "ACE",
    "role": "striker",
    "info": {
      "flavor": "The first person to embody the “Ace” archetype was Aisling Jensen, an auxiliary pilot active during the liberation of Verdana. Knights of the chassis and sky, Aces like Aisling throw their mechs into battle with high-speed strafing runs, agile maneuvers, and reckless feats of daring. Cocky and self-assured, Aces relish a good duel.",
      "tactics": "Aces are very fast and reactive strikers that can use Evasive Maneuvers to mitigate dangerous or high-damage attacks. Barrel Roll is most effective against heavy weapons. Their Seeking weapons ignore cover and don’t require line of sight, allowing them to deal consistent damage. Relatively low HP makes Aces vulnerable to sustained damage, and they are relatively weak against tech attacks."
    },
    "stats": {
      "armor": [
        0,
        0,
        0
      ],
      "hp": [
        10,
        12,
        14
      ],
      "evade": [
        12,
        15,
        18
      ],
      "edef": [
        8,
        8,
        10
      ],
      "heatcap": [
        8,
        8,
        8
      ],
      "speed": [
        5,
        6,
        7
      ],
      "sensor": [
        10,
        10,
        10
      ],
      "save": [
        10,
        12,
        14
      ],
      "hull": [
        -2,
        -2,
        -2
      ],
      "agility": [
        3,
        4,
        6
      ],
      "systems": [
        1,
        2,
        3
      ],
      "engineering": [
        0,
        1,
        1
      ],
      "size": [
        [
          1
        ],
        [
          1
        ],
        [
          1
        ]
      ],
      "activations": [
        1,
        1,
        1
      ]
    },
    "base_features": [
      "npcf_ssc_flight_system_ace",
      "npcf_missile_launcher_ace",
      "npcf_barrel_roll_ace"
    ],
    "optional_features": [
      "npcf_bombing_bay_ace",
      "npcf_strafe_ace",
      "npcf_missile_swarm_ace",
      "npcf_rapid_response_ace",
      "npcf_chaff_launchers_ace"
    ],
    "power": 100
  } """

loaded_json = json.loads(lcp_data)
Ace = load_npc_class(loaded_json)

# aaaaaaaaaaaaaaaaaaaaaaaaaa

class NPC:
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

bob_the_ace = NPC("Bob the Ace", Ace, tier=2)
print(bob_the_ace.get_HASE())
