from LCP_Reader import LCP_Reader
from pathlib import Path
import os

# 3/7/23: Core assumptions: 1 enemy team, no ally NPCs. Will evolve this later, just need to get something on paper, so to speak
# What this needs to do:
# - Add NPCs to OPFOR
# - List NPCs
    # How are we going to count up duplicates? Multiple entries of the same NPC, or just add a number to the entry?
        # Thinking the former for freedom of editing
            # Suggestion - maybe an "add to NPC roster" button
# - Indicate balance of opfor regarding roles
# - Indicate structure and action costs
# - Budget ^ according to number of players
    # Weight attribute important for this!
# - Save OPFOR to file
# - Load OPFOR from file?

class Encounter:
    def __init__(self, name='New Encounter', desc="No description", players=0, sitrep="Deathmatch", budget_mod=1):
        self.name = name
        self.desc = desc
        self.opfor = []
        self.players = players
        self.sitrep = sitrep # Placeholder value, will import later from LCPs
        self.budget_mod = budget_mod

    # CUSTOM ENCODER CLAUSE
    def __json__(self):
        return {'name': self.name, 
        'class_name': self.npc_class.name, 
        'tier': self.tier, 
        'templates': list(self.templates.keys()), 
        'allowed_features': list(self.allowed_features.keys()), 
        'features': list(self.features.keys()), 
        'activations': self.activations, 
        'weight': self.weight}
        # wow I didn't know you could stratify things like this

    def get_combatcost(self):
        s = 0
        for n in self.opfor:
            s = s + n.weight
        return s
    
    def add_NPC(self, NPC):
        self.opfor.append(NPC)
    
    def rm_NPC(self, NPC):
        self.opfor.remove(NPC)

    def rename_encounter(self, newname):
        self.name = newname

    def set_budgetmod(self, newmod):
        self.budget_mod = newmod

    def rename_desc(self, newdesc):
        self.desc = newdesc

    def set_players(self, new):
        self.players = new

    def get_opfor(self):
        return self.opfor