from LCP_Reader import LCP_Reader
from pathlib import Path
import os

class Template:
    def __init__(self, id, name, description, base_features, opt_features, power):
        self.id = id
        self.name = name
        self.description = description
        self.base_features = base_features
        self.opt_features = opt_features
        self.power = power

def load_npc_template(template_data):
    return Template(id= template_data["id"], name=template_data["name"], description=template_data["description"], base_features=template_data["base_features"], opt_features=template_data["optional_features"], power=template_data["power"])

loaded_templates = {}
def template_load(mode=None):
    if mode == None:
        for filename in Path('LCPs').glob('*.lcp'): # Loop through each LCP file
            #print(filename) # Debug shenanigans, delete later
            lcpr = LCP_Reader(filename) # Load the LCP info and save to a name
            for entry in lcpr.npc_templates: # Loop through each NPC template in the json
                thing = load_npc_template(entry) # Just saving this expression to 'thing' for easy typing
                loaded_templates.update({thing.name: thing}) # Push the NPC entry to the loaded_templates dictionary. Might be an issue if two LCPs have the same name of NPC?
            #x = len(loaded_templates) # More debug
            #print(f'{x} NPC Templates loaded from {filename}.') # More debug
        return loaded_templates # Hand off the master list of templates!
    else:
        return loaded_templates