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
import zipfile as zf
import json

# https://stackoverflow.com/questions/24030284/method-to-serialize-custom-object-to-json-in-python
# This is going to be a slight nightmare but here we go I guess

class MyEncoder(json.JSONEncoder):
    """
    JSONEncoder subclass that leverages an object's `__json__()` method,
    if available, to obtain its default JSON representation. 

    """
    def default(self, obj):
        if hasattr(obj, '__json__'):
            return obj.__json__()
        return json.JSONEncoder.default(self, obj)

#>>> json.dumps(MyClass(), cls=MyEncoder)