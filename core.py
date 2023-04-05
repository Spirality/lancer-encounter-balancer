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
from saveload import MyEncoder
from pathlib import Path
import json
import os
import code
from consolemenu import *
from consolemenu.items import *

version = "v0.1"
#To do: Load LCPs and pass as an argument to avoid compiling the LCP list three times over
# 3/20/23: I've gotten some advice, and it's better to save myself effort than overcomplicate things. RAM is plentiful. Simplify the bonuses on the feature level.
# 4/3/23: Core will probably contain all the text menu navigation fluff. Working on saveload.py concurrently
# 4/5/23: https://console-menu.readthedocs.io/en/latest/usage.html < documentation for the consolemenu module. Prone to change? Probably?

loaded_features = feat_load()
loaded_templates = template_load(loaded_features)
loaded_npc_classes = npc_load(loaded_features)

phil_the_carrier = NPC("Phil the Carrier", loaded_npc_classes['CARRIER'], tier=1)
joe_the_assault = NPC("Joe the Assault", loaded_npc_classes["ASSAULT"], tier=1)
n_berserker = NPC("Normal Berserker", loaded_npc_classes['BERSERKER'], tier=1)
v_engineer = NPC("Veteran Engineer", loaded_npc_classes['ENGINEER'], tier=1)
n_bastion = NPC("Normal Bastion", loaded_npc_classes['BASTION'], tier=1)
n_archer = NPC("Normal Archer", loaded_npc_classes['ARCHER'], tier=1)
n_ronin = NPC("Normal Ronin", loaded_npc_classes['RONIN'], tier=1)

phil_the_carrier.add_template(loaded_templates["CHAMPION"])
joe_the_assault.add_template(loaded_templates["GRUNT"])
v_engineer.add_template(loaded_templates["VETERAN"])

TestEncounter = Encounter(name="Battle of UwU", players=3)
#print(TestEncounter.structure_cost)
#TestEncounter.structure_cost = 5
#del TestEncounter.structure_cost
print("Champion Superiority structure bonus: {}".format(loaded_features["npc_champion_Superiority"].c_bonus.structure_bonus))
print("Phil's structure bonus: {}".format(phil_the_carrier.calc_bonus("structure")))
print("Phil's Champion Superiority structure bonus: {}".format(phil_the_carrier.features["npc_champion_Superiority"].c_bonus.structure_bonus))
print("Phil's current structure: {}".format(phil_the_carrier.get_stat("structure")))
print("Joe's current HP: {}".format(joe_the_assault.get_stat("hp")))
print("Joe's base HP: {}".format(joe_the_assault.get_basestat("hp")))
print("Joe's combat weight: {}".format(joe_the_assault.weight))
print("Phil's combat weight: {}".format(phil_the_carrier.weight))
#code.interact(local=locals())

main_menu = ConsoleMenu("METAVAULT Main Menu", f"Current version number: {version}", prologue_text="Select your destination:")
balancer_menu = ConsoleMenu("Encounter Balancer Menu", "Unfortunately, there is no Encounter Balancer to blink to. Whoops.")
npc_wizard = ConsoleMenu("NPC Wizard Menu", "Unfortunately, this feature is incomplete. Check back later!")
options_menu = ConsoleMenu("Options Menu", "I'll hopefully have more stuff here later aaaaaa")

goto_encounter_balancer = SubmenuItem("Encounter Balancer", balancer_menu, main_menu)
goto_npc_wizard = SubmenuItem("NPC Wizard", npc_wizard, main_menu)
goto_options = SubmenuItem("Options", options_menu, main_menu)

main_menu.append_item(goto_encounter_balancer)
main_menu.append_item(goto_npc_wizard)
main_menu.append_item(goto_options)

#main_menu.show()

print(json.dumps(phil_the_carrier, indent=4, cls=MyEncoder))