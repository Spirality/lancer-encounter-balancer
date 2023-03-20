from LCP_Reader import LCP_Reader
from featurestruc import Trait_Feature
from featurestruc import Weapon_Feature
from featurestruc import System_Feature
from featurestruc import Reaction_Feature
from featurestruc import Tech_Feature
from featurestruc import Feature_Bonuses
from featurestruc import Feature_Overrides
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
import code

#To do: Load LCPs and pass as an argument to avoid compiling the LCP list three times over
# 3/20/23: I've gotten some advice, and it's better to save myself effort than overcomplicate things. RAM is plentiful. Simplify the bonuses on the feature level.

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
print(loaded_features["npcf_reinforced_ultra"].get_bonus("structure"))
print(loaded_features["npcf_reinforced_ultra"].get_override("structure"))
print(loaded_features["npcf_reinforced_ultra"].c_bonus.structure_bonus)
code.interact(local=locals())