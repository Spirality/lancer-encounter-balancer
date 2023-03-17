from LCP_Reader import LCP_Reader
from featurestruc import Trait_Feature
from featurestruc import Weapon_Feature
from featurestruc import System_Feature
from featurestruc import Reaction_Feature
from featurestruc import Tech_Feature
from featurestruc import feat_load
from templatestruc import Template
from templatestruc import template_load
from npcdatastruc import NPC_Class
from npcdatastruc import NPC_Class_Stats
from npcdatastruc import NPC
from npcdatastruc import npc_load
from opforoptimizer import Encounter
from pathlib import Path
import os

#To do: Load LCPs and pass as an argument to avoid compiling the LCP list three times over

loaded_features = feat_load()
loaded_templates = template_load(loaded_features)
loaded_npcs = npc_load(loaded_features)

phil_the_carrier = NPC("Phil the Carrier", loaded_npcs['CARRIER'], tier=1)
joe_the_assault = NPC("Joe the Assault", loaded_npcs["ASSAULT"], tier=1)

phil_the_carrier.add_template(loaded_templates["CHAMPION"])
joe_the_assault.add_template(loaded_templates["GRUNT"])

TestEncounter = Encounter(name="Battle of UwU", players=3)
#print(TestEncounter.structure_cost)
#TestEncounter.structure_cost = 5
#del TestEncounter.structure_cost
print(loaded_features["npcf_reinforced_ultra"].bonus)
print(loaded_features["npcf_reinforced_ultra"].struc_bonus())
print(loaded_features["npcf_reinforced_ultra"].struc_override())
print(loaded_templates["ULTRA"].struc_bonus)