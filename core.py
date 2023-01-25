from LCP_Reader import LCP_Reader
from npcdatastruc import NPC_Class
from npcdatastruc import NPC_Class_Stats
from npcdatastruc import NPC
from npcdatastruc import load_npc_class, lcpload
from pathlib import Path
import os


loaded_npcs = lcpload()

print(loaded_npcs['CARRIER'].stats.hp)
bob_the_gladiator = NPC("Bob the Gladiator", loaded_npcs['GLADIATOR'], tier=2)
print(bob_the_gladiator.get_HASE())