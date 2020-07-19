from combat_encounter import PC,NPC,Creature,mods,roll_dice,temp_bonus,make_string,make_class,break_stamina,equip,equip_all,unequip,damage,drain,distance,convert_direction,melee_coordinates,force_move,impact,contest,attack,range_action,dc_action,move,weapon_attack,action_cost,stamina,effect,status,open_phase,interrupt,turn,round_mechanics,combat_round,combat_encounter



"""# Trials

This is where I am trying out sections of my code
"""
 
#creating stats  

Dougey = PC("Dougey", "Brute", "Human", "Blue", "Skin_Tone", "Hair_Color", 1, 4, "Trademarks", 25, 15, 20, 5, 10, 15, 2, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 2, 0, 0, 1, 2, 2, 1, 0, 1, 0, 0, 0, 2, 2, 2, "Offensive_Ability", "Defensive_Ability", "Movement_Ability", "Special_Ability", "Long Sword", "Off_Hand", "Utility", "Leather Armor", "Combat_Special_Move", "Backpack", "Gold", "Rations", "Kits", "Adventuring_Special_Moves", "Value_Self", "Value_Others", "Value_Society", "Mission", "Interests", "Talents", "Quirks", "Fears", "Family", "Friends", "Professional", "Nemesis", "Factions", "Home", "Profession", "Skill", "Race_Bonus", "Story", "Roleplaying_Special_Moves")

Guard = Creature("Guard", 1, "1x1", 4, "Human", "Flesh", "Dumb Idiot", "Attacks", "Spear", "Dagger", None, "Chain Mail", "Combat_Special_Moves", 2, 2, 2, "Immunities", "Weaknesses", "Vitals_1", "Vitals_2", "Vitals_3", "Reactions", "Combat_Role", "Tactics_1", "Tactics_2", "Tactics_3", "Value", "Needs", "Mission", "Role_Playing_Special_Moves", 30, 15, 20, 2, 5, 10, 1, 2, 1, 1, 0, 1, 2, 1, 4, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "Adventuring_Special_Moves", "Adventuring_Difficulty", "Role_Playing_Difficulty", "Combat_Difficulty", "Candy", "Paprika", "Health Potion", "Ruby", "Heart of Darkness")


equip_all(Dougey)
equip_all(Guard)


Maincharacter = Dougey.Name
Guard_name = Guard.Name



print(Maincharacter, Guard_name)

print(Dougey.Max_AP)
print(Dougey.HP["Prime"])
print(Dougey.Statuses["Blinded"])
print(Dougey.Equipment["Main Hand"])

print(type(Guard))
print(Guard.visibility["Size"])
print(Dougey.Equipment)

# Dougey = PC("Dougey", "Brute", "Human", "Blue", "Skin_Tone", "Hair_Color", 1, 4, "Trademarks", 25, 15, 20, 5, 10, 15, 2, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 2, 0, 0, 1, 2, 2, 1, 0, 1, 0, 0, 0, 2, 2, 2, "Offensive_Ability", "Defensive_Ability", "Movement_Ability", "Special_Ability", "Long Sword", "Off_Hand", "Utility", "Leather Armor", "Combat_Special_Move", "Backpack", "Gold", "Rations", "Kits", "Adventuring_Special_Moves", "Value_Self", "Value_Others", "Value_Society", "Mission", "Interests", "Talents", "Quirks", "Fears", "Family", "Friends", "Professional", "Nemesis", "Factions", "Home", "Profession", "Skill", "Race_Bonus", "Story", "Roleplaying_Special_Moves")

# Guard = Creature("Guard", 1, "1x1", 4, "Human", "Flesh", "Dumb Idiot", "Attacks", "Spear", None, None, "Chain Mail", "Combat_Special_Moves", 2, 2, 2, "Immunities", "Weaknesses", "Vitals_1", "Vitals_2", "Vitals_3", "Reactions", "Combat_Role", "Tactics_1", "Tactics_2", "Tactics_3", "Value", "Needs", "Mission", "Role_Playing_Special_Moves", 30, 15, 20, 2, 5, 10, 1, 2, 1, 1, 0, 1, 2, 1, 4, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, "Backpack", "Adventuring_Special_Moves", "Adventuring_Difficulty", "Role_Playing_Difficulty", "Combat_Difficulty")


combat_encounter(Dougey,Guard)


# # exec(Guard.Name + "." + actions_dict["Choke"]["Payload"])

# # Guard.suffocating_status_stage += 1
# # print(Guard.suffocating_status_stage)

# # print(Dougey.suffocating_status_stage)

# print(Guard.frightened_status_stage)

# """1.   Update PC and Creature to have positions
# 2.   update actions payloads
# 3.   update effect function to acount for different types of specialty payloads
# 4.   update weapon payloads
# 5.   create techiniques with payloads
# 6.   create features with payloads
# 7.   create status payloads and put them in pc and creature classes
# 8.   figure out combat classes and all of the junk tied to that
# 9.   severe testing for scalability. 
# 10.  add creature ai in combat roles, mortality, and creature tactics
# """

# effect(Dougey,Guard,"Taunt","Success")

# for i in actions_dict:
#   failed_actions = []
#   print(i)
#   try:
#     if actions_dict[i]["Action_Type"] == "Reaction":
#       print(i + " is a reaction")
#     elif actions_dict[i]["Action_Type"] == "Range":
#       effect(Dougey,Guard,i,15)
#     elif actions_dict[i]["Action_Type"] == "Contest":
#       effect(Dougey,Guard,i, "Success")
#     elif actions_dict[i]["Action_Type"] == "Attack":
#       effect(Dougey,Guard,i, "Success")
#     else:
#       effect(Dougey,Guard,i,"Success")
#   except:
#     print("----------" + i + " FAILED TO WORK")
#     failed_actions.append(i)

# print(failed_actions)

# total = 0
# for weapon in weapons_dict:
#   print(weapon)
#   print(weapons_dict[weapon]["Features"])
#   # if len(weapon["Feature"]) > 0:
#   #   for feature in weapon["Features"]:
#   #     print(feature)
  
#   total += 1

# print(total)

# print(weapons_dict["Maul"]["Techniques"])
# print(weapons_dict["Maul"])


"""successfull actions:
Disarm,
Choke,
Grapple,
Strike,
Shove,
Leap,
Lunge,
Hide,
Brace,
Concentrate,
Focus,
Charge Power,
Recover,
Tactics,
Enemy Status,
Bandage,
Aim,
Find Vitals,
Distract,
Pacify

reactions:
Dive,
Dodge,
Parry,
Riposte,
Trip,
Block

failed actions:
Steal,
Encourage

incomplete actions:
Weapon Attack,
Throw,
Tackle,
Climb,
Feint,
Enemy History,
Arcana,
Search,
Battlefield,
Coordinated Attack,
Improvise
"""