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
print("Champion Superiority structure bonus: {}".format(loaded_features["npc_champion_Superiority"].c_bonus.structure_bonus))
print("Phil's structure bonus: {}".format(phil_the_carrier.calc_bonus("structure")))
print("Phil's Champion Superiority structure bonus: {}".format(phil_the_carrier.features["npc_champion_Superiority"].c_bonus.structure_bonus))
print("Phil's current structure: {}".format(phil_the_carrier.get_stat("structure")))
print("Joe's current HP: {}".format(joe_the_assault.get_stat("hp")))
print("Joe's base HP: {}".format(joe_the_assault.get_basestat("hp")))
#code.interact(local=locals())