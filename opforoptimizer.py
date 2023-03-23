from LCP_Reader import LCP_Reader
from pathlib import Path
import os

# 3/7/23: Core assumptions: 1 enemy team, no ally NPCs. Will evolve this later, just need to get something on paper, so to speak
# What this needs to do:
# - List NPCs
    # How are we going to count up duplicates? Multiple entries of the same NPC, or just add a number to the entry?
        # Thinking the former for freedom of editing
            # Suggestion - maybe an "add to NPC roster" button
# - Indicate balance of opfor regarding roles
# - Indicate structure and action costs
# - Budget ^ according to number of players
    # Weight attribute important for this!

class Encounter:
    def __init__(self, name='New Encounter', desc="No description", players=0, sitrep="Deathmatch", budget_mod=1):
        self.name = name
        self.desc = desc
        self.opfor = []
        self.players = players
        self.sitrep = sitrep # Placeholder value, will import later from LCPs
        self.budget_mod = budget_mod
        self._structure_cost = 0 # Currently working but needs more improvement

    @property
    def structure_cost(self):
        """Structure Cost of an Encounter"""
        print("getter of structure_cost called")
        return self._structure_cost

    @structure_cost.setter
    def structure_cost(self, value):
        print("setter of structure_cost called")
        self._structure_cost = value

    @structure_cost.deleter
    def structure_cost(self):
        print("deleter of structure_cost called")
        self._structure_cost = 0
    
    def add_NPC(self, NPC):
        self.opfor.append(NPC)
    
    def rm_NPC(self, NPC):
        self.opfor.remove(NPC)