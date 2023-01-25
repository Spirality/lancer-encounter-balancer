from LCP_Reader import LCP_Reader
from npcdatastruc import NPC_Class
from npcdatastruc import NPC_Class_Stats
from npcdatastruc import NPC
from npcdatastruc import load_npc_class
from pathlib import Path
import os


loaded_npcs = {}
for filename in Path('LCPs').glob('*.lcp'):
    print(filename)
    lcpr = LCP_Reader(filename)
    npc_class_data = lcpr.npc_classes
    for entry in lcpr.npc_classes:
        # thank you Tetragramm for correcting my foolish ways
        thing = load_npc_class(entry)
        print(thing.name)
        loaded_npcs.update({thing.name: thing})
    x = len(lcpr.npc_classes)
    print(f'{x} NPC Classes loaded from {filename}.')

#print(loaded_npcs['CARRIER'].stats.hp)
bob_the_gladiator = NPC("Bob the Gladiator", loaded_npcs['GLADIATOR'], tier=2)
#print(bob_the_gladiator.get_HASE())