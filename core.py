from LCP_Reader import LCP_Reader
from featurestruc import Trait_Feature
from featurestruc import Weapon_Feature
from featurestruc import System_Feature
from featurestruc import Reaction_Feature
from featurestruc import Tech_Feature
from featurestruc import load_feature, feat_load
from templatestruc import Template
from templatestruc import template_load
from npcdatastruc import NPC_Class
from npcdatastruc import NPC_Class_Stats
from npcdatastruc import NPC
from npcdatastruc import load_npc_class, npc_load
from pathlib import Path
import os

loaded_features = feat_load()
loaded_templates = template_load()
loaded_npcs = npc_load()
phil_the_carrier = NPC("Phil the Carrier", loaded_npcs['CARRIER'], tier=1)
phil_the_carrier.add_template(loaded_templates["CHAMPION"])
for x in loaded_templates["CHAMPION"].base_feature_data.values():
    print(type(x))
print(phil_the_carrier.templates["CHAMPION"].bonuses)
print(loaded_templates["CHAMPION"].bonuses)