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
# 3/20/23: I've gotten some advice, and it's better to save myself effort than overcomplicate things. RAM is plentiful. Simplify the bonuses on the feature level.
# 4/3/23: Core will probably contain all the text menu navigation fluff. Working on saveload.py concurrently

loaded_features = feat_load()
loaded_templates = template_load(loaded_features)
loaded_npcs = npc_load(loaded_features)

phil_the_carrier = NPC("Phil the Carrier", loaded_npcs['CARRIER'], tier=1)
joe_the_assault = NPC("Joe the Assault", loaded_npcs["ASSAULT"], tier=1)
n_berserker = NPC("Normal Berserker", loaded_npcs['BERSERKER'], tier=1)
v_engineer = NPC("Veteran Engineer", loaded_npcs['ENGINEER'], tier=1)
n_bastion = NPC("Normal Bastion", loaded_npcs['BASTION'], tier=1)
n_archer = NPC("Normal Archer", loaded_npcs['ARCHER'], tier=1)
n_ronin = NPC("Normal Ronin", loaded_npcs['RONIN'], tier=1)

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
print(joe_the_assault.weight)

#code.interact(local=locals())
def start():
    print("Welcome to the Lancer Encounter Balancer, project name METAVAULT!")
    main_menu()

def main_menu():
    desc = """
    Main Menu
    ------------
    Select option:
    1. Encounter Balancer
    2. NPC Wizard
    3. Options
    4. Exit
    ------------
    """
    print(desc)
    selection = int(input("Select an option:"))
    while selection != 0:
        if selection==1:
            print("Blinking to Encounter Balancer...")
            print("Unfortunately, there is no Encounter Balancer to blink to. Whoops.")
            print(desc)
            selection = int(input("Select an option:"))
            ## You can add your code or functions here
        elif selection==2:
            print("Blinking to NPC Wizard...")
            print("Unfortunately, there is no NPC Wizard to blink to. Whoops.")
            print(desc)
            selection = int(input("Select an option:"))
        elif selection==3:
            print("Blinking to Options...")
            print("Unfortunately, there are no options to blink to. Whoops.")
            print(desc)
            selection = int(input("Select an option:"))
        elif selection ==4:
            print("Exiting Blinkspace...")
            selection = 0
        else:
            # Any integer inputs other than values 1-4 we print an error message
            print("Wrong option selection. Enter any key to try again..")
            print(desc)
            selection = int(input("Select an option:"))

start()