# This file is just for me writing junk down. Please ignore, delete from final release, please and thank



#    def calc_bonus(self):
#        working = {}
#        totals = {}
#        for entry in self.features.values():
#            if hasattr(entry, "bonus") == True and entry.type == "trait":
#                for k in entry.keys():
#                    totals[k] = working.get(k, 0) + entry.get(k, 0)
#            else:
#                continue
#        return totals
#
#        for f in self.base_feature_data.values():
#            if hasattr(f, "bonus"): # Making sure it's a trait
#                if f.bonus != None:   # Weeding out the blanks
#                    for k, v in f.bonus.items():    # for key and value,
#                        if self.bonuses.get(k) != None: # if the value exists
#                            self.bonuses[k] = self.bonuses[k] + v   # add the value to the value already in the dict
#                        else:                                       # otherwise,
#                            self.bonuses.update({k: v})             # just add the whole entry

#        for f in self.base_feature_data.values(): #in the actual data of the feature
#            if f.type == 'Trait': #if the feature is a Trait
#                if (f.bonus != None): #check if it has a bonus
#                    self.struc_bonus = self.struc_bonus + f.get_bonus("structure")  #add bonus to dict
#                    self.stress_bonus = self.stress_bonus + f.get_bonus("stress")
#                if (f.override != False):
#                    self.struc_override = f.get_override("structure")
#                    self.stress_override = f.get_override("stress")

#    def calc_bonus(self):
#        self.struc_bonus = 0
#        self.stress_bonus = 0
#        self.struc_override = False
#        self.stress_override = False
#        if self.templates == {}: # In case of empty template dict, set bonuses to 0
#            return # 3/17/23: Retool this to create new bonuses as found in the bonus dict instead of doing it manually
#        else:
#            for entry in self.templates.values():
#                self.struc_bonus = self.struc_bonus + entry.struc_bonus
#                self.stress_bonus = self.stress_bonus + entry.stress_bonus
#                if entry.struc_override != False:
#                    assert self.struc_override is False, f'{self.name} is trying to stack overrides! (Attempting to apply {entry.name})'
#                    self.struc_override = entry.struc_override
#                if entry.stress_override != False:
#                    assert self.stress_override is False, f'{self.name} is trying to stack overrides! (Attempting to apply {entry.name})'
#                    self.stress_override = entry.stress_override