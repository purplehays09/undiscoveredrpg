# # Three quote marks in a row allow you to auto detect new lines 
# # print("""Customer: Good morning.
# # Owner: Good morning""")

# import json

# question = input("What do you want to do?")
# print(question)

# if question == "Attack":
#     print("Roll")
#     yourTotal = int(input("What is your attack total?"))
#     print(yourTotal)
# else:
#     print("I didn't get that")
from django.db import models

#the combat classes 
COMBAT_CLASS = [
    ("Warrior", "Warrior"), 
    ("Brute", "Brute"), 
    ("Ranger", "Ranger"), 
    ("Rogue", "Rogue"), 
    ("Druid", "Druid"), 
    ("Sorcerer", 
        ("Light", "Light"),
        ("Wind", "Wind"),
        ("Nature", "Nature"),
        ("Water", "Water"),
        ("Earth", "Earth"),
        ("Fire", "Fire"),
        ("Lightning", "Lightning"),
        )
    ("Arcanist", 
        ("Mind", "Mind"),
        ("Matter", "Matter"),
        ("Gravity", "Gracity"),
        ("Spirit", "Spirit"),
        )
    ]

# # character module creator
class PC(models.Model):
    #Basic character information
    Name = models.CharField(max_length=50) #input 
    Combat_Class = models.CharField(max_length=50, choices= COMBAT_CLASS) #select from list
    Race = models.CharField(max_length=50) #select from list 
    Eye_Color = models.CharField(max_length=50) #input 
    Skin_Tone = models.CharField(max_length=50) #input 
    Hair_Color = models.CharField(max_length=50) #input 
    Size = models.IntegerField(max_length=50) # Auto Set to 1
    Weight = models.IntegerField(max_length=50) #input 
    Trademarks = models.CharField(max_length=50) #input 

    #Combat variables
    Health = models.IntegerField(max_length=50) #auto set to full (3)
    Max_Vitality = models.IntegerField(max_length=50, default=3) #Default 3
    Tier_1 = models.IntegerField(max_length=50) #Default 1
    Tier_2 = models.IntegerField(max_length=50) #Default 1
    Tier_3 = models.IntegerField(max_length=50) #Default 1

    # Statuses
    blinded_status_stage = models.IntegerFiield(max_length=50, default=0)
    burning_status_stage = models.IntegerFiield(max_length=50, default=0)
    crippled_arm_status_stage = models.IntegerFiield(max_length=50, default=0)
    crippled_leg_status_stage = models.IntegerFiield(max_length=50, default=0)
    deafened_status_stage = models.IntegerFiield(max_length=50, default=0)
    fatigued_status_stage = models.IntegerFiield(max_length=50, default=0)
    impaled_status_stage = models.IntegerFiield(max_length=50, default=0)
    captivated_status_stage = models.IntegerFiield(max_length=50, default=0)
    confused_status_stage = models.IntegerFiield(max_length=50, default=0)
    frightened_status_stage = models.IntegerFiield(max_length=50, default=0)
    stunned_status_stage = models.IntegerFiield(max_length=50, default=0)
    momentum_status_stage = models.IntegerFiield(max_length=50, default=0)
    prone_status_stage = models.IntegerFiield(max_length=50, default=0)
    restrained_status_stage = models.IntegerFiield(max_length=50, default=0)
    suffocating_status_stage = models.IntegerFiield(max_length=50, default=0)
    surprised_status_stage = models.IntegerFiield(max_length=50, default=0)
    charged_status_stage = models.IntegerFiield(max_length=50, default=0)
    enraged_status_stage = models.IntegerFiield(max_length=50, default=0)
    hastened_status_stage = models.IntegerFiield(max_length=50, default=0)
    petrified_status_stage = models.IntegerFiield(max_length=50, default=0)
    frozen_status_stage = models.IntegerFiield(max_length=50, default=0)
    
    Attack_Bonus = models.IntegerField(max_length=50) #Calculate Muscle + STR mod + weapon
    Dodge_Bonus = models.IntegerField(max_length=50)  #Calculate
    Defend_Bonus = models.IntegerField(max_length=50) #Calculate
    Offensive_Ability = models.CharField(max_length=50) #autoset off class
    Defensive_Ability = models.CharField(max_length=50) #autoset off class
    Movement_Ability = models.CharField(max_length=50) #autoset off class
    Specail_Ability = models.CharField(max_length=50) #autoset off class
    Free_Movement = models.IntegerField(max_length=50) #Calculate on size and armor
    AP = models.IntegerField(max_length=50) #Default 12
    RP = models.IntegerField(max_length=50) #Default 4
    Power_Rank = models.IntegerField(max_length=50) #default 1
    Main_Hand = models.CharField(max_length=50) # Character selects in creation
    Off_Hand = models.CharField(max_length=50) # Default null
    Utility = models.CharField(max_length=50) # Character selects in creation
    Armor = models.CharField(max_length=50) # Character selects in creation
    Combat_Special_Move = models.CharField(max_length=500) # default null

    #Adventuring Variables

    #conditions
    bleeding_condition_stage = models.IntegerFiield(max_length=50, default=0)
    blinded_condition_stage = models.IntegerFiield(max_length=50, default=0)
    crippled_condition_stage = models.IntegerFiield(max_length=50, default=0)
    deafened_condition_stage = models.IntegerFiield(max_length=50, default=0)
    drowsy_condition_stage = models.IntegerFiield(max_length=50, default=0)
    fatigued_condition_stage = models.IntegerFiield(max_length=50, default=0)
    fractured_condition_stage = models.IntegerFiield(max_length=50, default=0)
    sickened_condition_stage = models.IntegerFiield(max_length=50, default=0)
    
    Short_Rest = models.IntegerField(max_length=50) #default 0
    Carry_Weight = models.CharField(max_length=50) # STR Mod + 5 
    Backpack = models.CharField(max_length=5000) #Default 0 + kits & rations and any starting equipment
    Gold = models.IntegerField(max_length=500) # default 0
    Rations = models.IntegerField(max_length=50) #default 5
    Kits = models.CharField(max_length=50) # selected from a list during character creation
    Adventuring_Special_Moves = models.CharField(max_length=500) # default null

    #Role Playing Variiables
    Value_Self = models.CharField(max_length=500) #selected during characer creation
    View_Self = models.CharField(max_length=500) #selected during characer creation
    Value_Others = models.CharField(max_length=500) #selected during characer creation
    View_Others = models.CharField(max_length=500) #selected during characer creation
    Value_Society = models.CharField(max_length=500) #selected during characer creation
    View_Society = models.CharField(max_length=500) #selected during characer creation
    Mission = models.CharField(max_length=500) #selected during characer creation
    Interests = models.CharField(max_length=500) #selected during characer creation
    Talents = models.CharField(max_length=500) #selected during characer creation
    Quirks = models.CharField(max_length=500) #selected during characer creation
    Fears = models.CharField(max_length=500) #selected during characer creation
    Family = models.CharField(max_length=500) #selected during characer creation
    Friends = models.CharField(max_length=500) #selected during characer creation
    Professional = models.CharField(max_length=500) #selected during characer creation
    Nemesis = models.CharField(max_length=500) #selected during characer creation
    Factions = models.CharField(max_length=500) #selected during characer creation
    Home = models.CharField(max_length=500) #selected during characer creation
    Profession = models.CharField(max_length=500) #selected during characer creation
    Skill = models.CharField(max_length=500) # default Null
    Race_Bonus = models.CharField(max_length=500) #selected during characer creation
    Story = models.CharField(max_length=5000) #selected during characer creation
    Roleplaying_Special_Moves = models.CharField(max_length=500) #default null

    #Skills and Attributes
    STR = models.IntegerField(max_length=50) # Pool set during creation
    STR_Mod = models.IntegerField(max_length=50) # auto calculate based on STR
    DEX = models.IntegerField(max_length=50)# Pool set during creation
    DEX_Mod = models.IntegerField(max_length=50)# auto calculate based on DEX
    CON = models.IntegerField(max_length=50)# Pool set during creation
    CON_Mod = models.IntegerField(max_length=50)# auto calculate based on CON
    INT = models.IntegerField(max_length=50)# Pool set during creation
    INT_Mod = models.IntegerField(max_length=50)# auto calculate based on INT
    WIS = models.IntegerField(max_length=50)# Pool set during creation
    WIS_MOD = models.IntegerField(max_length=50)# auto calculate based on WIIS
    CHA = models.IntegerField(max_length=50)# Pool set during creation
    CHA_Mod = models.IntegerField(max_length=50)# auto calculate based on CHA
    Muscle = models.IntegerField(max_length=50)# Pool set during creation, default 0
    Wrestle = models.IntegerField(max_length=50)# Pool set during creation, default 0
    Brawl = models.IntegerField(max_length=50)# Pool set during creation, default 0
    Coordination = models.IntegerField(max_length=50)# Pool set during creation, default 0
    Finesse = models.IntegerField(max_length=50)# Pool set during creation, default 0
    Sleight_of_Hand = models.IntegerField(max_length=50)# Pool set during creation, default 0
    Stealth = models.IntegerField(max_length=50)# Pool set during creation, default 0
    Endurance = models.IntegerField(max_length=50)# Pool set during creation, default 0
    Concentration = models.IntegerField(max_length=50)# Pool set during creation, default 0
    Vitality = models.IntegerField(max_length=50)# Pool set during creation, default 0
    Academic = models.IntegerField(max_length=50)# Pool set during creation, default 0
    Arcana = models.IntegerField(max_length=50)# Pool set during creation, default 0
    Culture = models.IntegerField(max_length=50)# Pool set during creation, default 0
    Analyze = models.IntegerField(max_length=50)# Pool set during creation, default 0
    Nature = models.IntegerField(max_length=50)# Pool set during creation, default 0
    Aggressive = models.IntegerField(max_length=50)# Pool set during creation, default 0
    Suave = models.IntegerField(max_length=50)# Pool set during creation, default 0
    Diplomatic = models.IntegerField(max_length=50)# Pool set during creation, default 0
    Sincere = models.IntegerField(max_length=50)# Pool set during creation, default 0

class Creature(models.Model):

    # Basic Variables
    Names = models.CharFiled(max_length=50) #Creature Name
    Size = models.IntegerField(max_length=50) # Size unit
    Shape = models.IntegerField(max_length=50) # 
    Weight = models.IntegerField(max_length=50)
    Anatomy = models.CharField(max_length=50)
    Material = models.CharField(max_length=50)
    Description = models.IntegerField(max_length=500)

    #Combat Variiables
    Attacks = models.CharField(max_length=50)
    Weapons = models.CharField(max_length=50)
    Abilities = models.CharField(max_length=50)
    Vitality = models.IntegerField(max_length=50)
    Immunities = models.CharField(max_length=50)
    Weaknesses = models.CharField(max_length=50)
    Vitals = models.CharField(max_length=50)
    Reactions = models.CharField(max_length=50)
    Abilities = models.CharField(max_length=50)
    Combat_Role = models.CharField(max_length=50)
    Solo_Tactics = models.CharField(max_length=50)
    Group_Tactics = models.CharField(max_length=50)

    # Role Playing Variables
    Charisma = models.CharField(max_length=50)
    Value = models.CharField(max_length=50)
    Needs = models.CharField(max_length=50)
    Mission = models.CharField(max_length=50)
    Abilities = models.CharField(max_length=50)

    # Base Attributes, Skills and Adventuring abilities
    Stats = models.CharField(max_length=50)
    Skills = models.CharField(max_length=50)
    Speed = models.IntegerField(max_length=50)
    Abilities = models.CharField(max_length=50)

    # Difficulty
    Adventuring_Difficulty = models.IntegerField(max_length=50)
    Role_Playing_Difficulty = models.IntegerField(max_length=50)
    Combat_Difficulty = models.IntegerField(max_length=50)

class NPC(models.Model):
    Name = models.CharField(max_length=50)
    Creature = models.CharField(max_length=50) # This should be directly from the Creature model
    Profession = models.CharField(max_length=50)
    Value_Self = models.CharField(max_length=50)
    Value_Others = models.CharField(max_length=50)
    Value_Society = models.CharField(max_length=50)
    View_Self = models.CharField(max_length=50)
    View_Others = models.CharField(max_length=50)
    View_Society = models.CharField(max_length=50)
    Aggressive = models.IntegerField(max_length=50)
    Suave = models.IntegerField(max_length=50)
    Diplomatic = models.IntegerField(max_length=50)
    Sincere = models.IntegerField(max_length=50)
    Core_Desires_1 = models.CharField(max_length=50)
    Core_Desires_2 = models.CharField(max_length=50)
    Core_Desires_3 = models.CharField(max_length=50)
    Secrets_1 = models.CharField(max_length=50)
    Secrets_2 = models.CharField(max_length=50)
    Secrets_3 = models.CharField(max_length=50)
    Fears_1 = models.CharField(max_length=50)
    Fears_2 = models.CharField(max_length=50)
    Fears_3 = models.CharField(max_length=50)
    Family = models.CharField(max_length=50)
    Friends = models.CharField(max_length=50)
    Romantic = models.CharField(max_length=50)
    Work = models.CharField(max_length=50)
    Nemesis = models.CharField(max_length=50)
    Factions = models.CharField(max_length=50)
    Possesions_1 = models.CharField(max_length=50)
    Possesions_2 = models.CharField(max_length=50)
    Possesions_3 = models.CharField(max_length=50)
    Abilities_1 = models.CharField(max_length=50)
    Abilities_2 = models.CharField(max_length=50)
    Abilities_3 = models.CharField(max_length=50)


# x=5
# y=2
# print(x//y)
# print(x%y)
# print(x/y)

# fullAP = 12
# playerAP = fullAP
# while playerAP > 0:
#     playerPosition = input("It is the top of your turnWhat positioin would you like to take you take? \nBunker Down\nRush\nAim")
#     if playerPosition == "Bunker Down" or "Bunker" or "Down" or "bunker down" or "bunker" or "down":
#         print("Perfect")
#         playerAction = input("You have " + str(playerAP) + " AP left. What would you like to do? \nSupress Fire\nBandage\nReload")
#         if playerAction == "Supress Fire" or "Supress" or "Fire" or "supress fire" or "supress" or "fire":
#             print("Perfect!\nRoll your skill")
#             playerRoll = input("What is your total?")
#         elif playerAction == "Bandage" or "bandage":
#             print("Perfect!\nRoll your skill")
#             playerRoll = input("What is your total?")

#     else:
#         ap = 0
# print("Your turn is over")

# name = input("What is your name?")
# nameLen = len(name)
# for chr in name:
#     print(chr)
# print(name[3])
# print(name[4])
# while nameLen > 0: 
#     reverseName = [name]
#     print(name[nameLen])
#     nameLen = nameLen - 1
# print("finished")
    

# fullLength = list(range())

# def allTheCalculations(x, y):
#     # print("ADD" + str(x) "+" + str(y) "=" str(x+y))
#     # print("SUB" + str(x) "-" + str(y) "=" str(x+y))
#     # print("MUL" + str(x) "*" + str(y) "=" str(x+y))
#     # print("DIV" + str(x) "/" + str(y) "=" str(x+y))
#     print(x + y)
#     print(x - y)
#     print(x * y)
#     print(x / y)
#     return x

# allTheCalculations(12,4)