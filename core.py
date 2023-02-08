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
from pathlib import Path
import os

loaded_npcs = npcload()
loaded_features = featload()
print(loaded_features['MECHANIZED INFANTRY DOCTRINE'].origin['name'])