from LCP_Reader import LCP_Reader
from pathlib import Path
from featurestruc import Trait_Feature
from featurestruc import Weapon_Feature
from featurestruc import System_Feature
from featurestruc import Reaction_Feature
from featurestruc import Tech_Feature
from featurestruc import load_feature, feat_load
import os

loaded_features = feat_load()

#TODO: Maybe instead of just feature names, have initialization actually go look up the features and store them in the template class as the individual feature classes?
class Template:
    def __init__(self, id, name, description, base_features, opt_features, power):
        self.id = id
        self.name = name
        self.description = description
        self.base_features = base_features #list
        self.opt_features = opt_features #list
        self.feature_ids = self.base_features + self.opt_features #list
        self.base_feature_data = {x:loaded_features.get(x) for x in self.base_features if x in loaded_features}
        self.features = {x:loaded_features.get(x) for x in self.feature_ids if x in loaded_features} #dict of ALL features
        # ^ this line is essentially using self.feature_ids as a list of keys to look up in the master feature list, then grabs them and saves them in the Template obj
        self.bonuses = {}
        for f in self.base_feature_data.values(): #in the actual data of the feature
            if f.type == 'Trait': #if the feature is a Trait
                print(f"Heehoo for {f.bonus} from init of {f.id}")
                if (f.bonus != None): #check if it has a bonus
                    print("Something")
                    self.bonuses.update()
        self.power = power

    def get_features(self):
        return self.feature_ids

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