from LCP_Reader import LCP_Reader
from pathlib import Path
import os

# 3/7/23: Core assumptions: 1 enemy team, no ally NPCs. Will evolve this later, just need to get something on paper, so to speak
# What this needs to do:
# - List NPCs
# - Indicate balance of opfor regarding roles
# - Indicate structure and action costs
# - Budget ^ according to number of players

class Encounter:
    def __init__(self, name='New Encounter', desc="No description", players=0, sitrep="Deathmatch", budget_mod=1):
        self.name = name
        self.desc = desc
        self.opfor = []
        self.players = players
        self.sitrep = sitrep # Placeholder value, will import later from LCPs
        self.budget_mod = budget_mod

    def structure_cost():
        print("Hi, this feature isn't complete yet")