from LCP_Reader import LCP_Reader
from npcdatastruc import NPC_Class
from npcdatastruc import NPC_Class_Stats
from npcdatastruc import NPC
from npcdatastruc import load_npc_class, npcload
from featurestruc import Trait_Feature
from featurestruc import Weapon_Feature
from featurestruc import System_Feature
from featurestruc import Reaction_Feature
from featurestruc import Tech_Feature
from featurestruc import load_feature, featload
from templatestruc import Template
from templatestruc import templateload
from pathlib import Path
import os

loaded_npcs = npcload()
loaded_features = featload()
loaded_templates = templateload()
print(loaded_features['MECHANIZED INFANTRY DOCTRINE'].origin['name'])
phil_the_carrier = NPC("Phil the Carrier", loaded_npcs['CARRIER'], tier=1)
print(phil_the_carrier.get_baseFeats())
phil_the_carrier.add_Template("CHAMPION")
print(phil_the_carrier.templates)