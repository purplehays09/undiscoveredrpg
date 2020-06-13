import random
import json
import math
import numpy as np

null = None

class PC:
    def __init__(self, Name, Combat_Class, Race, Eye_Color, Skin_Tone, Hair_Color, Size, Weight, Trademarks, STR, DEX, CON, INT, WIS, CHA, Muscle, Wrestle, Brawl, Jump, Coordination, Finesse, Sleight, Stealth, Endurance, Concentration, Vitality, Academic, Arcana, Culture, Search, Nature, Insight, Interaction, Medicine, Perception, Survival, Aggressive, Suave, Diplomatic, Sincere, Prime, Wounded, Bloodied, Offensive_Ability, Defensive_Ability, Movement_Ability, Special_Ability, Main_Hand, Off_Hand, Utility, Armor, Combat_Special_Move, Backpack, Gold, Rations, Kits, Adventuring_Special_Moves, Value_Self, Value_Others, Value_Society, Mission, Interests, Talents, Quirks, Fears, Family, Friends, Professional, Nemesis, Factions, Home, Profession, Skill, Race_Bonus, Story, Roleplaying_Special_Moves): 
        # Basic information and appearance
        self.Name = Name
        self.Combat_Class = Combat_Class
        self.Race = Race
        self.Eye_Color = Eye_Color
        self.Skin_Tone = Skin_Tone
        self.Hair_Color = Hair_Color
        self.Size = Size
        self.Weight = Weight
        self.Trademarks = Trademarks

                # STATS and SKILLS
        self.STR = STR
        self.DEX = DEX
        self.CON = CON
        self.INT = INT
        self.WIS = WIS
        self.CHA = CHA
        self.Muscle = Muscle
        self.Wrestle = Wrestle
        self.Brawl = Brawl
        self.Jump = Jump
        self.Coordination = Coordination
        self.Finesse = Finesse
        self.Sleight = Sleight
        self.Stealth = Stealth
        self.Endurance = Endurance
        self.Concentration = Concentration
        self.Vitality = Vitality
        self.Academic = Academic
        self.Arcana = Arcana
        self.Culture = Culture
        self.Search = Search
        self.Nature = Nature
        self.Insight = Insight
        self.Interaction = Interaction
        self.Medicine = Medicine
        self.Perception = Perception
        self.Survival = Survival
        self.Aggressive = Aggressive
        self.Suave = Suave
        self.Diplomatic = Diplomatic
        self.Sincere = Sincere
        
        #Health information
        self.Prime = Prime
        self.Wounded = Wounded
        self.Bloodied = Bloodied
        self.Max_HP = Prime + Wounded + Bloodied
        self.Max_AP = 6
        self.Max_RP = 6
        self.Max_MP = 6
        
        self.Stamina = "Prime"
        
        self.HP = {
            "Prime":Prime, 
            "Wounded":Wounded, 
            "Bloodied":Bloodied
        }
        self.AP = 6
        self.RP = 6
        self.MP = 6

        
        #Statuses - always start at 0 and can be added during combat
        self.blinded_status_stage = 0
        self.burning_status_stage = 0
        self.crippled_arm_status_stage = 0
        self.crippled_leg_status_stage = 0
        self.deafened_status_stage = 0
        self.fatigued_status_stage = 0
        self.impaled_status_stage = 0
        self.captivated_status_stage = 0
        self.confused_status_stage = 0
        self.frightened_status_stage = 0
        self.stunned_status_stage = 0
        self.momentum_status_stage = 0
        self.prone_status_stage = 0
        self.restrained_status_stage = 0
        self.suffocating_status_stage = 0
        self.surprised_status_stage = 0

        self.misc_bonus = 0
        self.crit_threshold = 20
        self.crit_fail_threshold = 1

        # Combat stats 
        # self.Attack_Bonus = Muscle + STR_Mod
        # self.Dodge_Bonus = Coordination + DEX_Mod
        # self.Defend_Bonus = Endurance + CON_Mod
        self.Offensive_Ability = Offensive_Ability
        self.Defensive_Ability = Defensive_Ability
        self.Movement_Ability = Movement_Ability
        self.Special_Ability = Special_Ability
        

        self.Power_Rank = 0

        #equipment
        self.Main_Hand = Main_Hand
        self.Off_Hand = Off_Hand
        self.Utility = Utility
        self.Armor = Armor
        self.Combat_Special_Move = Combat_Special_Move

        # adventuring conditions - set at 0 until added to after combat or during adventuring
        self.bleeding_condition_stage = 0
        self.blinded_condition_stage = 0
        self.crippled_condition_stage = 0
        self.deafened_condition_stage = 0
        self.drowsy_condition_stage = 0
        self.fatigued_condition_stage = 0
        self.fractured_condition_stage = 0
        self.sickened_condition_stage = 0

        self.Short_Rest = 0
        self.Carry_Weight = 10
        self.Backpack = Backpack
        self.Gold = Gold
        self.Rations = Rations
        self.Kits = Kits
        self.Adventuring_Special_Moves = Adventuring_Special_Moves


        self.Value_Self = Value_Self
        self.Value_Others = Value_Others
        self.Value_Society = Value_Society
        self.Mission = Mission
        self.Interests = Interests
        self.Talents = Talents
        self.Quirks = Quirks
        self.Fears = Fears
        self.Family = Family
        self.Friends = Friends
        self.Professional = Professional
        self.Nemesis = Nemesis
        self.Factions = Factions
        self.Home = Home
        self.Profession = Profession
        self.Skill = Skill
        self.Race_Bonus = Race_Bonus
        self.Story = Story
        self.Roleplaying_Special_Moves = Roleplaying_Special_Moves

#  for NPC
class NPC:
    def __init__(self, Name, Creature, Profession, Value_Self, Value_Others, Value_Society, Aggressive, Suave, Diplomatic, Sincere, Core_Desires_1, Core_Desires_2, Core_Desires_3, Secrets_1, Secrets_2, Secrets_3, Fears_1, Fears_2, Fears_3, Family, Friends, Romantic, Work, Nemesis, Factions, Possesions_1, Possesions_2, Possesions_3, Abilities_1, Abilities_2, Abilities_3):
        self.Name = Name
        self.Creature = Creature
        self.Profession = Profession
        self.Value_Self = Value_Self
        self.Value_Others = Value_Others
        self.Value_Society = Value_Society
        self.Aggressive = Aggressive
        self.Suave = Suave
        self.Diplomatic = Diplomatic
        self.Sincere = Sincere
        self.Core_Desires_1 = Core_Desires_1
        self.Core_Desires_2 = Core_Desires_2
        self.Core_Desires_3 = Core_Desires_3
        self.Secrets_1 = Secrets_1
        self.Secrets_2 = Secrets_2
        self.Secrets_3 = Secrets_3
        self.Fears_1 = Fears_1
        self.Fears_2 = Fears_2
        self.Fears_3 = Fears_3
        self.Family = Family
        self.Friends = Friends
        self.Romantic = Romantic
        self.Work = Work
        self.Nemesis = Nemesis
        self.Factions = Factions
        self.Possesions_1 = Possesions_1
        self.Possesions_2 = Possesions_2
        self.Possesions_3 = Possesions_3
        self.Abilities_1 = Abilities_1
        self.Abilities_2 = Abilities_2
        self.Abilities_3 = Abilities_3




#creatures
class Creature:
    def __init__(self, Name, Size, Shape, Weight, Anatomy, Material, Description, Attacks, Weapons, Armor, Combat_Special_Moves, Prime, Wounded, Bloodied, Immunities, Weaknesses, Vitals_1, Vitals_2, Vitals_3, Reactions, Combat_Role, Tactics_1, Tactics_2, Tactics_3, Value, Needs, Mission, Role_Playing_Special_Moves, STR, DEX, CON, INT, WIS, CHA, Muscle, Wrestle, Brawl, Jump, Coordination, Finesse, Sleight, Stealth, Endurance, Concentration, Vitality, Academic, Arcana, Culture, Search, Nature, Insight, Interaction, Medicine, Perception, Survival, Aggressive, Suave, Diplomatic, Sincere, Speed, Equipment, Backpack, Adventuring_Special_Moves, Adventuring_Difficulty, Role_Playing_Difficulty, Combat_Difficulty):
        
        
        self.visibility = {
            "Name":False,
            "Size":False,
            "Shape":False,
            "Weight":False,
            "Anatomy":False,
            "Material":False,
            "Description":False,
            "Attacks":False,
            "Weapons":False,
            "Armor":False,
            "Combat_Special_Moves":False,
            "Max_Health":False,
            "Prime_HP":False,
            "Wounded_HP":False,
            "Bloodied_HP":False,
            "Immunities":False,
            "Weaknesses":False,
            "Vital_1":False,
            "Vital_2":False,
            "Vital_3":False,
            "Reactions":False,
            "Combat_Role":False,
            "Tactics_1":False,
            "Tactics_2":False,
            "Tactics_3":False,
            "Statuses":False,
            "Values":False,
            "Needs":False,
            "Mission":False,
            "Role_Playing_Special_Moves":False,
            "Stats":False,
            "Skills":False,
            "Speed":False,
            "Adventuring_Special_Moves":False,
            "Combat_Difficulty":False,
            "Role_Playing_Difficulty":False,
            "Adventuring_Difficulty":False            
        }

        self.Name = Name
        self.Size = Size
        self.Shape = Shape
        self.Weight = Weight
        self.Anatomy = Anatomy
        self.Material = Material
        self.Description = Description

        #Combat = #Combat


        self.Attacks = Attacks
        self.Weapons = Weapons
        self.Armor = Armor
        self.Combat_Special_Moves = Combat_Special_Moves
        self.Prime = Prime
        self.Wounded = Wounded
        self.Bloodied = Bloodied
        self.Immunities = Immunities
        self.Weaknesses = Weaknesses
        self.Vitals_1 = Vitals_1
        self.Vitals_2 = Vitals_2
        self.Vitals_3 = Vitals_3
        self.Reactions = Reactions
        self.Combat_Role = Combat_Role
        self.Tactics_1 = Tactics_1
        self.Tactics_2 = Tactics_2
        self.Tactics_3 = Tactics_3

        self.Max_HP = Prime + Wounded + Bloodied
        self.Max_AP = 6
        self.Max_RP = 6
        self.Max_MP = 6
        
        self.Stamina = "Prime"
        
        self.HP = {
            "Prime":Prime, 
            "Wounded":Wounded, 
            "Bloodied":Bloodied
        }
        self.AP = 6
        self.RP = 6
        self.MP = 6

        self.misc_bonus = 0
        self.crit_threshold = 20
        self.crit_fail_threshold = 1


        self.blinded_status_stage = 0
        self.burning_status_stage = 0
        self.crippled_arm_status_stage = 0
        self.crippled_leg_status_stage = 0
        self.deafened_status_stage = 0
        self.fatigued_status_stage = 0
        self.impaled_status_stage = 0
        self.captivated_status_stage = 0
        self.confused_status_stage = 0
        self.frightened_status_stage = 0
        self.stunned_status_stage = 0
        self.momentum_status_stage = 0
        self.prone_status_stage = 0
        self.restrained_status_stage = 0
        self.suffocating_status_stage = 0
        self.surprised_status_stage = 0


        #Charisma = #Charisma
        self.Value = Value
        self.Needs = Needs
        self.Mission = Mission
        self.Role_Playing_Special_Moves = Role_Playing_Special_Moves

                # STATS and SKILLS
        self.STR = STR
        self.DEX = DEX
        self.CON = CON
        self.INT = INT
        self.WIS = WIS
        self.CHA = CHA
        self.Muscle = Muscle
        self.Wrestle = Wrestle
        self.Brawl = Brawl
        self.Jump = Jump
        self.Coordination = Coordination
        self.Finesse = Finesse
        self.Sleight = Sleight
        self.Stealth = Stealth
        self.Endurance = Endurance
        self.Concentration = Concentration
        self.Vitality = Vitality
        self.Academic = Academic
        self.Arcana = Arcana
        self.Culture = Culture
        self.Search = Search
        self.Nature = Nature
        self.Insight = Insight
        self.Interaction = Interaction
        self.Medicine = Medicine
        self.Perception = Perception
        self.Survival = Survival
        self.Aggressive = Aggressive
        self.Suave = Suave
        self.Diplomatic = Diplomatic
        self.Sincere = Sincere

        self.Speed = Speed
        self.Equipment = Equipment
        self.Backpack = Backpack
        self.Adventuring_Special_Moves = Adventuring_Special_Moves

        self.Combat_Difficulty = Combat_Difficulty
        self.Role_Playing_Difficulty = Role_Playing_Difficulty
        self.Adventuring_Difficulty = Adventuring_Difficulty

        #actions
actions_dict = {
    "Name": {
            "Type": "Type",
            "Stat": "Stat",
            "Skill": "Skill",
            "Speed": "Speed",
            "Range": "Range",
            "Description": "Description",
            "Dice_Roll": "Dice_Roll",
            "Action_Type": "Action_Type",
            "Reaction": "Reaction",
            "Payload": "Payload"
        },
    "Weapon Attack":{
            "Type": "Action",
            "Stat": "STR",
            "Skill": "Muscle",
            "Speed": "~",
            "Range": "~",
            "Description": "\u2022Standard attacks vary by weapon and spell. See your attacks for information.\n\u2022You can choose to replace your Muscle mod with a -2 Finesse mod\n\u2022If the weapon has a Balance tag, you can ignore the -2 penalty to your Finesse mod",
            "Dice_Roll": "d20",
            "Action_Type": "Special",
            "Reaction": "Standard_Reactions",
            "Payload": "Weapon"
        },
    "Disarm":{
            "Type": "Action",
            "Stat": "STR",
            "Skill": "Muscle",
            "Speed": "2",
            "Range": "1",
            "Description": "\u2022Grab an object held by a target and attempt to pull it away. Make a Disarm contest against the target\u2019s +8 Muscle Check.  On a success, the target is disarmed of the item. \n\u2022Attempting to Disarm a weapon gives the target an opportunity attack against you on a fail.\n\u2022Each Debuff status affecting the target\u2019s arm gives them an additional -3 toward the check. ",
            "Dice_Roll": "d20",
            "Action_Type": "Contest",
            "Reaction": "Muscle",
            "Payload": "eval(str(target) + '.Weapons') = None"
        },
    "Throw":{
            "Type": "Action",
            "Stat": "STR",
            "Skill": "Muscle",
            "Speed": "2",
            "Range": "Skill check/5 Force Units",
            "Description": "\u2022Make a Throw check on a held object against a target within range. On a hit, the target takes 1 damage or status according to the GM's discretion. \n\u2022You can choose to replace your Muscle mod with a -2 Finesse mod\n\u2022If the object is Weight and < Size 1 you can ignore the -2 penalty to your Finesse mod",
            "Dice_Roll": "d20",
            "Action_Type": "Special",
            "Reaction": "Standard_Reactions",
            "Payload": "Throw"
        },
    "Choke":{
            "Type": "Action",
            "Stat": "STR",
            "Skill": "Wrestle",
            "Speed": "4",
            "Range": "1",
            "Description": "\u2022Make a Choke check contested against the target\u2019s Muscle check. On a success the target takes a stage of Suffocating",
            "Dice_Roll": "d20",
            "Action_Type": "Contest",
            "Reaction": "Wrestle",
            "Payload": "suffocating_status_stage += 1"
        },
    "Grapple":{
            "Type": "Action",
            "Stat": "STR",
            "Skill": "Wrestle",
            "Speed": "4",
            "Range": "1",
            "Description": "\u2022Make a Grapple check contested against the target\u2019s Muscle check. On a success the target takes a stage of Restrained",
            "Dice_Roll": "d20",
            "Action_Type": "Contest",
            "Reaction": "Wrestle",
            "Payload": "restrained_status_stage +=1"
        },
    "Strike":{
            "Type": "Action",
            "Stat": "STR",
            "Skill": "Brawl",
            "Speed": 1,
            "Range": "1",
            "Description": "\u2022Make a Strike check against a target\u2019s choice of reaction. On a hit, the target takes a stage of Stunned for every 2 hits they have taken during your turn (Attack, special move, or another Strike).",
            "Dice_Roll": "d20",
            "Action_Type": "Special",
            "Reaction": "Standard_Reactions",
            "Payload": "stunned_status_stage +=1"
        },
    "Shove":{
            "Type": "Action",
            "Stat": "STR",
            "Skill": "Brawl",
            "Speed": "2",
            "Range": "1",
            "Description": "\u2022Make a Shove check contested against the target\u2019s Muscle check. On a success the target takes a stage of Prone",
            "Dice_Roll": "d20",
            "Action_Type": "Contest",
            "Reaction": "Muscle",
            "Payload": "prone_status_stage +=1"
        },
    "Tackle":{
            "Type": "Action",
            "Stat": "STR",
            "Skill": "Brawl",
            "Speed": "4",
            "Range": "1",
            "Description": "\u2022Make a Tackle check contested against the target\u2019s Muscle check. On a success the target takes a stage of Prone and Grappled. You also take a stage of Prone",
            "Dice_Roll": "d20",
            "Action_Type": "Contest",
            "Reaction": "Muscle",
            "Payload": "Tackle"
        },
    "Leap":{
            "Type": "Movement",
            "Stat": "STR",
            "Skill": "Jump",
            "Speed": "1",
            "Range": "Jump",
            "Description": "\u2022Declare a distance you want to Leap. Make a Leap check and add your Momentum stages if applicable. \n\u2022Your horizontal range = (Leap check/5) + Momentum Stage \n\u2022Your vertical range =  (Leap check/10) + Momentum Stage\n\u2022If the declared distance is less than the range, you must succeed in a Coordination Check or take a stage of Prone \n\u2022DC = Range * 5\n\u2022You can choose to replace your Jump mod with a -2 Coordination mod",
            "Dice_Roll": "d20",
            "Action_Type": "Range",
            "Reaction": "",
            "Payload": "Leap"
        },
    "Lunge":{
            "Type": "Movement",
            "Stat": "STR",
            "Skill": "Jump",
            "Speed": "1",
            "Range": "1",
            "Description": "\u2022Make a Lunge check to gain stages of Momentum.\n\u2022Momentum stage = Lunge check / 10 ",
            "Dice_Roll": "d20",
            "Action_Type": "Range",
            "Reaction": "",
            "Payload": "momentum_status_stage += (total//10)"
        },
    "Climb":{
            "Type": "Movement",
            "Stat": "STR",
            "Skill": "Jump",
            "Speed": "1",
            "Range": "1",
            "Description": "\u2022Make a Climb check to scale up a surface or creature. \n\u2022DC = 5 + (2 * Total climbing range)\n\u2022On a fail, you fall from your height and suffer any applicable effects.",
            "Dice_Roll": "d20",
            "Action_Type": "Range",
            "Reaction": "",
            "Payload": "Climb"
        },
    "Dive":{
            "Type": "Reaction",
            "Stat": "DEX",
            "Skill": "Coordination",
            "Speed": "2",
            "Range": "Jump",
            "Description": "\u2022Trigger - An Attack is declared against you or you are in the Area of Effect of an Attack or Special Move.\n*Dive automatically fails if Attacks or Special Moves targeting you fill the Area of Effect you are in and you are not within Jumping range of the border of that Attack\u2019s Area of Effect IE: Earthquake\nEffect:\n\u2022Move up to the Range away to gain a +10 on a Dodge Check but land Prone \n\u2022Prone stage = 0 to 8 Stage 3; 9 to 14 stage 2; 15+ Stage 1",
            "Dice_Roll": "d6",
            "Action_Type": "Reaction",
            "Reaction": "",
            "Payload": "prone_status_stage +=1"
        },
    "Dodge":{
            "Type": "Reaction",
            "Stat": "DEX",
            "Skill": "Coordination",
            "Speed": "1",
            "Range": "0",
            "Description": "\u2022Trigger - An Attack is declared against you or you are in the Area of Effect of an Attack or Special Move.\n*Dodge automatically fails if Attacks or Special Moves targeting you fill the Area of Effect you are in and you are not on the border of that Attack\u2019s Area of Effect IE: Earthquake\nEffect:\n\u2022Roll 1d6 and add your Dodge bonus (base + armor) to contest the Attack or evade the effect. On success, you take no damage.",
            "Dice_Roll": "d6",
            "Action_Type": "Reaction",
            "Reaction": "",
            "Payload": ""
        },
    "Parry":{
            "Type": "Reaction",
            "Stat": "DEX",
            "Skill": "Finesse",
            "Speed": "2",
            "Range": "1",
            "Description": "\u2022Trigger - You are selected for the target of a physical or weapon attack\nEffect:\n\u2022Meet an enemies attack with your own. Make a melee Attack roll contest against an incoming physical Attack. The winner of the contest deals damage to the loser if within range. If outside range, the loser\u2019s attack counted as miss\n\u2022You can choose to replace your Finesse mod with a -2 Muscle mod",
            "Dice_Roll": "d20",
            "Action_Type": "Reaction",
            "Reaction": "",
            "Payload": ""
        },
    "Riposte":{
            "Type": "Reaction",
            "Stat": "DEX",
            "Skill": "Finesse",
            "Speed": "2",
            "Range": "1",
            "Description": "\u2022Trigger - After a successful Parry \nEffect:\n\u2022Counter attack an enemy. Make a Riposte check against the opponents Parry. On a success, the target takes the effect of an Attack action\n\u2022You can choose to replace your Finesse mod with a -2 Muscle mod",
            "Dice_Roll": "d20",
            "Action_Type": "Reaction",
            "Reaction": "",
            "Payload": "Weapon"
        },
    "Feint":{
            "Type": "Action",
            "Stat": "DEX",
            "Skill": "Sleight",
            "Speed": "2",
            "Range": "Weapon",
            "Description": "\u2022Roll a Feint contest against a target\u2019s Insight check. On a success you deceive a target of your intended attack, and they must roll their intended reaction to the attack. The target cannot use the same reaction against your next attack ",
            "Dice_Roll": "d20",
            "Action_Type": "Contest",
            "Reaction": "Insight",
            "Payload": "Feint"
        },
    "Steal":{
            "Type": "Action",
            "Stat": "DEX",
            "Skill": "Sleight of Hand",
            "Speed": "2",
            "Range": "1",
            "Description": "\u2022An attempt to take an equipped weapon or item from an equipment slot of the Target (not from a hand). Make a Steal contest against the target\u2019s +8 Perception check. On a success, you take the item, on a fail the target is given a free opportunity attack against you\n\u2022Each stage of the Concealed status you have against the target gives you an additional +3 toward the Steal check",
            "Dice_Roll": "d20",
            "Action_Type": "Contest",
            "Reaction": "Perception",
            "Payload": "Steal"
        },
    "Trip":{
            "Type": "Reaction",
            "Stat": "DEX",
            "Skill": "Sleight of Hand",
            "Speed": "2",
            "Range": "1",
            "Description": "\u2022Trigger - A target moves through a space adjacent to you\nEffect:\n\u2022Make a Trip check contested against a target\u2019s +3 Coordination check. On a success the target takes a stage of Prone \n\u2022Prone stage = Contest difference/5 rounded down\n\u2022Each Momentum stage -3 from the target\u2019s Coordination check",
            "Dice_Roll": "d20",
            "Action_Type": "Reaction",
            "Reaction": "",
            "Payload": "prone_status_stage += 1"
        },
    "Hide":{
            "Type": "Movement",
            "Stat": "DEX",
            "Skill": "Stealth",
            "Speed": "2",
            "Range": "0",
            "Description": "\u2022Attempt to hide away from view. Make a Hide check. DC determined by the GM. On a success, you gain 1 stage of Hidden",
            "Dice_Roll": "d20",
            "Action_Type": "DC",
            "Reaction": "",
            "Payload": "Hide"
        },
    "Block":{
            "Type": "Reaction",
            "Stat": "CON",
            "Skill": "Endurance",
            "Speed": "1",
            "Range": "0",
            "Description": "\u2022Trigger - An Attack or special move is declared against you or you are in the Area of Effect of an Attack or special move.\nEffect:\n\u2022Roll 1d6 and add your Block bonus (base + armor) to contest the Attack or evade the effect. On success, you take no damage",
            "Dice_Roll": "d6",
            "Action_Type": "Reaction",
            "Reaction": "",
            "Payload": ""
        },
    "Brace":{
            "Type": "Action",
            "Stat": "CON",
            "Skill": "Endurance",
            "Speed": "2",
            "Range": "0",
            "Description": "\u2022Roll a Brace check to give yourself an additional d6's to use on reactions until the start of your next turn. \n\u2022Number of d6's = the Brace check /5 (rounded down)",
            "Dice_Roll": "d20",
            "Action_Type": "Range",
            "Reaction": "",
            "Payload": "RP += total // 5"
        },
    "Charge Power":{
        "Type": "Action",
        "Stat": "CON",
        "Skill": "Concentration",
        "Speed": "2",
        "Range": "0",
        "Description": "\u2022Roll a Charge Power check to gain momentum towards your next Power Rank \n\u2022DC = 10 + Power Rank",
        "Dice_Roll": "d20",
        "Action_Type": "Range",
        "Reaction": "",
        "Payload": "power_rank += 1"
        },
    "Concentrate":{
            "Type": "Action",
            "Stat": "CON",
            "Skill": "Concentration",
            "Speed": "2",
            "Range": "0",
            "Description": "\u2022Maintain Concentration on the spell or effect. DC = 8 + power rank of spell + number of turns concentrated.",
            "Dice_Roll": "d20",
            "Action_Type": "DC",
            "Reaction": "",
            "Payload": "Concentrate"
        },
    "Focus":{
            "Type": "Action",
            "Stat": "CON`",
            "Skill": "Concentration",
            "Speed": "2",
            "Range": "0",
            "Description": "\u2022Focus can be applied before any action to raise the minimum roll value. \n\u2022Roll a Focus check and divide it in half to make a focus value. On your following action, any dice roll below this focus value will be treated as the focus value instead of the dice value (except for Crit fails).",
            "Dice_Roll": "d20",
            "Action_Type": "Range",
            "Reaction": "",
            "Payload": "Focus"
        },
    "Recover":{
            "Type": "Action",
            "Stat": "CON",
            "Skill": "Vitality",
            "Speed": "0",
            "Range": "2",
            "Description": "\u2022Roll a Recover Check to regain a damaged health block or mental status. DC = 8 + 1 per Debuff status currently affecting you AND Missing Health Block",
            "Dice_Roll": "d20",
            "Action_Type": "Range",
            "Reaction": "",
            "Payload": "Current_Health_Tier += total // 10"
        },
    "Enemy History":{
            "Type": "Action",
            "Stat": "INT",
            "Skill": "Academic",
            "Speed": "1",
            "Range": "24",
            "Description": "\u2022Tap knowledge of any historical record or mentions of this specific group. DC is determined by the GM",
            "Dice_Roll": "d20",
            "Action_Type": "DC",
            "Reaction": "",
            "Payload": ""
        },
    "Arcana":{
            "Type": "Action",
            "Stat": "INT",
            "Skill": "Arcane",
            "Speed": "1",
            "Range": "24",
            "Description": "\u2022Tap knowledge of what magic is being used and what effects it has. DC is determined by the GM",
            "Dice_Roll": "d20",
            "Action_Type": "DC",
            "Reaction": "",
            "Payload": ""
        },
    "Tactics":{
            "Type": "Action",
            "Stat": "INT",
            "Skill": "Culture",
            "Speed": "1",
            "Range": "24",
            "Description": "\u2022Roll a Tactics check to tap knowledge of any specific tactics used by the enemy's Stat Block. DC is determined by the GM",
            "Dice_Roll": "d20",
            "Action_Type": "DC",
            "Reaction": "",
            "Payload": ""
        },
    "Search":{
            "Type": "Action",
            "Stat": "INT",
            "Skill": "Investigation",
            "Speed": "2",
            "Range": "1",
            "Description": "",
            "Dice_Roll": "d20",
            "Action_Type": "DC",
            "Reaction": "",
            "Payload": ""
        },
    "Battlefield":{
            "Type": "Action",
            "Stat": "INT",
            "Skill": "Nature",
            "Speed": "1",
            "Range": "24",
            "Description": "\u2022Tap knowledge of any advantages or weaknesses presented on the battlefield. DC is determined by the GM",
            "Dice_Roll": "d20",
            "Action_Type": "DC",
            "Reaction": "",
            "Payload": ""
        },
    "Enemy Status":{
            "Type": "Action",
            "Stat": "WIS",
            "Skill": "Insight",
            "Speed": "1",
            "Range": "24",
            "Description": "\u2022Roll an Enemy Status contested by a target's Sleight to read an enemies' health and difficulty.",
            "Dice_Roll": "d20",
            "Action_Type": "Contest",
            "Reaction": "Sleight",
            "Payload": "print(eval(target + '.Max_Vitality'))"
        },
    "Coordinated Attack":{
            "Type": "Action",
            "Stat": "WIS",
            "Skill": "Interaction",
            "Speed": "6",
            "Range": "12",
            "Description": "\u2022Roll a Coordinated Attack check to invite an ally within range to perform actions (with you) in succession. \n\u2022You and your ally spend their 12 AP for the round to share a single turn and with a total combined AP for both of you equal to your Coordinated Attack check\n\u2022You are limited to movement and one action each.",
            "Dice_Roll": "d20",
            "Action_Type": "Special",
            "Reaction": "",
            "Payload": "Coordinated Attack"
        },
    "Improvise":{
            "Type": "Action",
            "Stat": "WIS",
            "Skill": "Interaction",
            "Speed": "1",
            "Range": "-",
            "Description": "\u2022Find a branch for a quick weapon, kick dirt to put out a fire, or use your ingenuity to solve a quick problem. DC set by GM.",
            "Dice_Roll": "d20",
            "Action_Type": "DC",
            "Reaction": "",
            "Payload": "Improvise"
        },
    "Bandage":{
            "Type": "Action",
            "Stat": "WIS",
            "Skill": "Medicine",
            "Speed": "2",
            "Range": "1",
            "Description": "\u2022Aid an ally by Healing a Health Block or 1 status (if applicable). DC determined by Status or GM",
            "Dice_Roll": "d20",
            "Action_Type": "DC",
            "Reaction": "",
            "Payload": "Bandage"
        },
    "Aim":{
            "Type": "Action",
            "Stat": "WIS",
            "Skill": "Perception",
            "Speed": "2",
            "Range": "Attack Range",
            "Description": "\u2022Roll an Aim check to improve the accuracy of your next attack (action or special move) against a single target you can see. Add your Aim Check total divided by 4 to your following attack roll. ",
            "Dice_Roll": "d20",
            "Action_Type": "Range",
            "Reaction": "",
            "Payload": "eval(str(source.Name) + '.misc_bonus') += total // 4"
        },
    "Find Vitals":{
            "Type": "Action",
            "Stat": "WIS",
            "Skill": "Survival",
            "Speed": "2",
            "Range": "24",
            "Description": "\u2022Roll a Find Vitals contested against a target's Insight to determine an enemies Vital points. On a success, the vital stage you learn is equal to your Find Vitals check divided by 10",
            "Dice_Roll": "d20",
            "Action_Type": "Contest",
            "Reaction": "Insight",
            "Payload": "eval(target + '.visibiity[Vitals_1]') = True"
        },
    "Taunt":{
            "Type": "Action",
            "Stat": "CHA",
            "Skill": "Aggressive",
            "Speed": "2",
            "Range": "24",
            "Description": "\u2022Roll a Taunt check against a target's Concentration to inflict the Captivated or Frightened status to a target.",
            "Dice_Roll": "d20",
            "Action_Type": "Contest",
            "Reaction": "Concentration",
            "Payload": "captivated_status_stage += 1"
        },
    "Distract":{
            "Type": "Action",
            "Stat": "CHA",
            "Skill": "Suave",
            "Speed": "2",
            "Range": "24",
            "Description": "\u2022Roll a Distract check against a target's Concentration to give a target a level of Flanked.",
            "Dice_Roll": "d20",
            "Action_Type": "Contest",
            "Reaction": "Concentration",
            "Payload": "flanked_position_stage += 1"
        },
    "Pacify":{
            "Type": "Action",
            "Stat": "CHA",
            "Skill": "Diplomatic",
            "Speed": "2",
            "Range": "24",
            "Description": "\u2022Roll a Pacify check against a target's Diplomatic check to try and convince a them to withdraw from combat. On a success, initiative is paused.",
            "Dice_Roll": "d20",
            "Action_Type": "Contest",
            "Reaction": "Diplomatic",
            "Payload": ""
        },
    "Encourage":{
            "Type": "Action",
            "Stat": "CHA",
            "Skill": "Sincere",
            "Speed": "2",
            "Range": "24",
            "Description": "\u2022Roll an Encourage check against a target to give an ally one stage of the Bolstered status. DC determined by GM",
            "Dice_Roll": "d20",
            "Action_Type": "DC",
            "Reaction": "",
            "Payload": ""
        }
  }


  #armors

armors_dict = {
    "armor_name": {
        "Type": "string(armor types)",
        "Defend": "int",
        "Block_Bonus": "float(.5, 1, or 0)",
        "Dodge_Base": "int",
        "Dodge_Bonus": "float(.5, 1, or 0)",
        "Mobility": "int",
        "Durability": "int",
        "Features": "string",
        "Techniques": "string",
        "Vital1": "string",
        "Vital2": "sting",
        "Vital3": "string"
    },
    "Unarmored": {
        "Type": "Light",
        "Defend": 6,
        "Block_Bonus": 1,
        "Agility": 10,
        "Dodge_Bonus": 1,
        "Mobility": 6,
        "Durability": 0,
        "Features": "Unburdened 1",
        "Techniques": "Unburdened 3",
        "Vital1": "1d6",
        "Vital2": "1d6 + 1/2 Dodge",
        "Vital3": "1d6 + Dodge"
    },
    "Leather Armor": {
        "Type": "Light",
        "Defend": 8,
        "Block_Bonus": 0,
        "Agility": 12,
        "Dodge_Bonus": .5,
        "Mobility": 5,
        "Durability": "6",
        "Features": "Utility 1",
        "Techniques": "Utility 2, Nimble 1",
        "Vital1": "1d6",
        "Vital2": "2d6",
        "Vital3": "2d6 + 1/2 Dodge"
    },
    "Gambeson": {
        "Type": "Light",
        "Defend": 10,
        "Block_Bonus": 0,
        "Agility": 10,
        "Dodge_Bonus": .5,
        "Mobility": 5,
        "Durability": 6,
        "Features": "Nimble 1",
        "Techniques": "Nimble 2",
        "Vital1": "1d6",
        "Vital2": "2d6",
        "Vital3": "2d6 + 1/2 Dodge"
    },
    "Chain Mail": {
        "Type": "Medium",
        "Defend": 12,
        "Block_Bonus": .5,
        "Agility": 12,
        "Dodge_Bonus": .5,
        "Mobility": 4,
        "Durability": 8,
        "Features": "Fortified 1",
        "Techniques": "Fortified 2",
        "Vital1": "1d6",
        "Vital2": "2d6",
        "Vital3": "2d6 + 1/2 Dodge or 1/2 Block"
    },
    "Splint Mail": {
        "Type": "Medium",
        "Defend": 13,
        "Block_Bonus": .5,
        "Agility": 10,
        "Dodge_Bonus": 0,
        "Mobility": 4,
        "Durability": 8,
        "Features": "Fortified 1",
        "Techniques": "Fortified 2",
        "Vital1": "1d6",
        "Vital2": "2d6 + 1/2 Block",
        "Vital3": "3d6 + 1/2 Block"
    },
    "Breast Plate": {
        "Type": "Medium",
        "Defend": 9,
        "Block_Bonus": 0,
        "Agility": 11,
        "Dodge_Bonus": .5,
        "Mobility": 5,
        "Durability": 8,
        "Features": "Nimble 1",
        "Techniques": " Nimble 2",
        "Vital1": "1d6 + 1/2 Dodge",
        "Vital2": "2d6 + 1/2 Block",
        "Vital3": "3d6 + 1/2 Block"
    },
    "Scale Mail": {
        "Type": "Heavy",
        "Defend": 13,
        "Block_Bonus": .5,
        "Agility": 8,
        "Dodge_Bonus": 0,
        "Mobility": 4,
        "Durability": 7,
        "Features": "Fortified 1",
        "Techniques": "Fortified 2",
        "Vital1": "1d6 + 1/2 Block",
        "Vital2": "2d6 + 1/2 Block",
        "Vital3": "3d6 + 1/2 Block"
    },
    "Plate Mail": {
        "Type": "Heavy",
        "Defend": 14,
        "Block_Bonus": .5,
        "Agility": 7,
        "Dodge_Bonus": 0,
        "Mobility": 3,
        "Durability": 9,
        "Features": "Fortified 1, Braced 1",
        "Techniques": "Fortified 2, Braced 2",
        "Vital1": "1d6 + 1/2 Block",
        "Vital2": "2d6 + 1/2 Block",
        "Vital3": "3d6 + Block"
    },
    "Full Plate": {
        "Type": "Heavy",
        "Defend": 15,
        "Block_Bonus": 1,
        "Agility": 6,
        "Dodge_Bonus": 0,
        "Mobility": 2,
        "Durability": 10,
        "Features": "Fortified 1, Braced 1",
        "Techniques": "Fortified 2, Braced 2",
        "Vital1": "1d6 + Block",
        "Vital2": "2d6 + Block",
        "Vital3": "3d6 + Block"
    }
}


# weapons
weapons_dict = {
    "weapon_name":{
        "Type": "string(handed)",
        "Damage_Type": "string(damage types)",
        "Crit_Damage": "int",
        "Range": "int",
        "AP": "int",
        "Features": "strings(list from weapons key)",
        "Techniqiues": "strings(list from weapons key)",
        "Description": "string(long form)"
    },
    "Dagger":{
        "Type": "One Handed",
        "Damage_Type": "Piercing",
        "Crit_Damage": "2",
        "Range": "1",
        "AP": "2",
        "Features": "Dual Wielding 1",
        "Techniqiues": "Balance 2, Dual Weilding 2",
        "Description": ""
    },
    "Flail":{
        "Type": "One Handed",
        "Damage_Type": "Bludgeoning",
        "Crit_Damage": "2",
        "Range": "2",
        "AP": "3",
        "Features": "Momentum 1, Grappling 1",
        "Techniqiues": "Momentum 2 Grappling 2",
        "Description": ""
    },
    "War Hammer":{
        "Type": "One Handed",
        "Damage_Type": "Bludgeoning",
        "Crit_Damage": "2",
        "Range": "1",
        "AP": "3",
        "Features": "Crippling 1",
        "Techniqiues": "Crippling 2",
        "Description": ""
    },
    "Hand Axe":{
        "Type": "One Handed",
        "Damage_Type": "Slashing",
        "Crit_Damage": "2",
        "Range": "1",
        "AP": "3",
        "Features": "Cleave 1",
        "Techniqiues": "Cleave 2",
        "Description": ""
    },
    "Katana":{
        "Type": "One Handed",
        "Damage_Type": "Slashing",
        "Crit_Damage": "2",
        "Range": "1",
        "AP": "3",
        "Features": "Balance 1, Cleave 1, Dueling 1",
        "Techniqiues": "Balance 2; Dual Wielding 1; Cleave 2; Dueling 2",
        "Description": ""
    },
    "Long Sword":{
        "Type": "One Handed",
        "Damage_Type": "Slashing",
        "Crit_Damage": "2",
        "Range": "1",
        "AP": "3",
        "Features": "Versatile 1",
        "Techniqiues": "Versatile 2 Cleave 1, Dueling 1",
        "Description": ""
    },
    "Mace":{
        "Type": "One Handed",
        "Damage_Type": "Bludgeoning",
        "Crit_Damage": "2",
        "Range": "1",
        "AP": "3",
        "Features": "Crippling 1, Momentum 1",
        "Techniqiues": "Crippling 2; Momentum 2; Dueling 1",
        "Description": ""
    },
    "Rapier":{
        "Type": "One Handed",
        "Damage_Type": "Piercing",
        "Crit_Damage": "2",
        "Range": "1",
        "AP": "2",
        "Features": "Dueling 1, Balance 1",
        "Techniqiues": "Balance 2; Dual Wielding 2; Dueling 2",
        "Description": ""
    },
    "Short Sword":{
        "Type": "One Handed",
        "Damage_Type": "Slashing",
        "Crit_Damage": "2",
        "Range": "1",
        "AP": "3",
        "Features": "Balance 1 Versatile 1",
        "Techniqiues": "Balance 2, Dual Wielding 1, Versatile 2",
        "Description": ""
    },
    "Whip":{
        "Type": "One Handed",
        "Damage_Type": "Slashing",
        "Crit_Damage": "2",
        "Range": "3",
        "AP": "3",
        "Features": "Grappling 1",
        "Techniqiues": "Grappling 2",
        "Description": ""
    },
    "Maul":{
        "Type": "Two Handed",
        "Damage_Type": "Bludgeoning",
        "Crit_Damage": "3",
        "Range": "1",
        "AP": "4",
        "Features": "Heavy 2, Momentum 1, Crippling 1",
        "Techniqiues": "Momentum 2, Crippling 2",
        "Description": ""
    },
    "Great Sword":{
        "Type": "Two Handed",
        "Damage_Type": "Slashing",
        "Crit_Damage": "3",
        "Range": "1",
        "AP": "4",
        "Features": "Heavy 1, Versatile 1, Rend 1, Cleave 1",
        "Techniqiues": "Cleave 2, Rend 2, Versatile 2",
        "Description": ""
    },
    "Battle Axe":{
        "Type": "Two Handed",
        "Damage_Type": "Slashing",
        "Crit_Damage": "3",
        "Range": "1",
        "AP": "4",
        "Features": "Heavy 1, Cleave 1, Rend 1",
        "Techniqiues": "Cleave 2, Rend 2",
        "Description": ""
    },
    "Spear":{
        "Type": "Two Handed",
        "Damage_Type": "Piercing",
        "Crit_Damage": "3",
        "Range": "2",
        "AP": "3",
        "Features": "Balance 1, Momentum 1",
        "Techniqiues": "Balance 2, Momentum 2",
        "Description": ""
    },
    "Lance":{
        "Type": "Two Handed",
        "Damage_Type": "Piercing",
        "Crit_Damage": "3",
        "Range": "2",
        "AP": "4",
        "Features": "Momentum 2",
        "Techniqiues": "Momentum 3",
        "Description": ""
    },
    "Glaive":{
        "Type": "Two Handed",
        "Damage_Type": "Slashing",
        "Crit_Damage": "3",
        "Range": "2",
        "AP": "4",
        "Features": "Balance 1, Momentum 1, Versatile 1",
        "Techniqiues": "Balance 2, Momentum 2, Versatile 2",
        "Description": ""
    },
    "Heavy Crossbow":{
        "Type": "Ranged",
        "Damage_Type": "Piercing",
        "Crit_Damage": "3",
        "Range": "15",
        "AP": "1",
        "Features": "Crippling 1",
        "Techniqiues": "Crippling 2",
        "Description": ""
    },
    "Javelin":{
        "Type": "Ranged",
        "Damage_Type": "Piercing",
        "Crit_Damage": "3",
        "Range": "5",
        "AP": "3",
        "Features": "Momentum 1",
        "Techniqiues": "Momentum 2",
        "Description": ""
    },
    "Light Crossbow":{
        "Type": "Ranged",
        "Damage_Type": "Piercing",
        "Crit_Damage": "2",
        "Range": "5",
        "AP": "1",
        "Features": "",
        "Techniqiues": "Balance 1",
        "Description": ""
    },
    "Longbow":{
        "Type": "Ranged",
        "Damage_Type": "Piercing",
        "Crit_Damage": "2",
        "Range": "15",
        "AP": "3",
        "Features": "Momentum 1",
        "Techniqiues": "Momentum 2",
        "Description": ""
    },
    "Recurve Bow":{
        "Type": "Ranged",
        "Damage_Type": "Piercing",
        "Crit_Damage": "2",
        "Range": "5",
        "AP": "3",
        "Features": "Balance 1",
        "Techniqiues": "Balance 2",
        "Description": ""
    },
    "Throwing Knives":{
        "Type": "Ranged",
        "Damage_Type": "Piercing",
        "Crit_Damage": "3",
        "Range": "5",
        "AP": "2",
        "Features": "Balance 1",
        "Techniqiues": "Balance 2",
        "Description": ""
    }
}

#classes

classes_dict = {
    "Name":{
        "Description": "string",
        "Offense Ability": "string",
        "Defense Ability": "string",
        "Mobility Ability": "string",
        "Special Ability": "string"
        },
    "Warrior":{
        "Description": "The warrior is a master battlefield technician. They specialize in bringing the fight to them and using defense as a weapon.\n\u2022 A group of minotaurs surround a single fighter. The leader charges in, confident he can overpower the small framed woman with nothing but a sword and shield. He raises back his maul and charges forward with a sure hit in his eye. The woman tilts forward and like a well timed dance, glances the maul off her shield and burries her sword in its unprotected abdomen. The three other minotaurs fume at her as she plants her sword through their leader's haunch, confirming her kill. They rush forward at once to avenge their fallen comrade, the woman raises her shield again lowers her frame. The last thing they see is fire in her eye and a smirk on her lips. ",
        "Offense Ability": "Bring It On - Unused AP is automatically converted to RP until the beginning of your next turn. ",
        "Defense Ability": "Expanded Reactions - You can perform any action as a reaction (using RP instead of AP) if the trigger is either:\n    \u2022 A target moves through a space adjacent to you OR\n    \u2022 You are selected for the target of an attack",
        "Mobility Ability": "Center of Attention - +1 to all your reactions reactions for each enemy adjacent to you.",
        "Special Ability": "Improved Taunt - You can Taunt 2 targets with a single action"
        },
    "Brute":{
        "Description": "A chaotic powerhouse on the battlefield, a brute fears nothing and knows that the strongest defense is a good offense. They are savages on the battlefield, dealing damage as much as possible as strong as possible.\n\u2022 The witch doctor lies on an army of corpses. Only one man opposes him. He believes that the single axe is no match for his army of undead and raises the horde to send a wave in.  One after another they fall, slit in half by the axe, He summons more, and more but the barbarian keeps swinging, and he is moving toward the mage. Corpse after corpse after corpse, battered broken and beaten. Inch by inch, swing by swing, the man moves closer. The undead are in a perpetual state of raising themselves back up from their remade graves. The axe is moving faster with each strike and the berserker wielding it now taking down multiple with with each swing. The necromancer starts to understand the gravity of the situation. Their is no army that can stop him.",
        "Offense Ability": "Relentless - Each consecutive attack lowers the Crit Threshold by 1. Crit Threshold restores to 20 on a Crit or missed attack.",
        "Defense Ability": "Grit - As a reaction, you can move a health tier by the Capacity of the incoming attack. Your health tiers restore at the start of your next turn (before healing).",
        "Mobility Ability": "Unstoppable Force - You can +1 to your Size (in the Force equation) for each stage of Momentum you have.",
        "Special Ability": "Opportunity Attack - You can replace the Trip Effect with an Attack action (STR Mod)\n    \u2022 Altered Trip"
        },
    "Ranger":{
        "Description": "Mobility is a Ranger's life. It is their primary weapon and their focus of their attack on their enemies. A ranger doesn't fire at the heart, but at the legs, surgically removing them as a threat on the battlefield.\n\u2022 A young pirate hauls his spoils to shore with his fellow marauders. Suddenly, an arrow breaks their concentration, piercing through a comrade's leg. The group turns to see a lone ranger up the shore. Racing forward the pirates charge the assailant. One by one arrows pick off the chargers until only the young pirate and 4 others remain. The archer stows his bow and draws twin blades before rushing toward the last of them. His movement is water in a bowl, sliding under one and spinning around another. The young man sees the futility of the fight and turns to flee for his life. The battlefield is strewn with crawling soon to be corpses trying to drag them selves away. He doesn't get 10 steps before a thrown dagger plunges in his thigh. He turns to see the avatar of his fate casually cleaning up what is left of the pirates. There is no escape.",
        "Offense Ability": "Stunt Attacks - If you use Maneuver while attacking, you can add 1 stage of any Position to either you or the target (your choice) for the duration of the attack.",
        "Defense Ability": "Safe Distance - If an enemy moves within their Attack range of you, you can move away as a reaction (1 RP per yard).",
        "Mobility Ability": "Maneuver - You can move while performing other actions. The free movement can be up to half the action's AP Cost.",
        "Special Ability": "Expanded Equipment Slots - You gain three additional slots to have equipped in combat."
        },
    "Rogue":{
        "Description": "A Rogue doesn't mince words, movement, or attacks. They target the vital points of their targets, slip into the shadows, and strike with lethal precision on their unsuspecting victims.\n\u2022 The cyclops swings its mighty club at the nimble assailant, leveling a building with his missed attack. He looks around for the remnants of the thief but sees nothing but a cloud of black smoke. 'You and your eye share a common weakness.' The cyclops pivots to see his enemy standing up the hill from him. 'That size makes gives you an advantage.' Enraged and rampant, the behemoth charges at him. The rogue draws his bow and waits as the cyclops fills his view. At the last moment, he lets loose his arrow, sinking it deep in the giant's eye. His body goes limp and he falls on the stagnant rogue, smothering the spot where he stood and blowing out another cloud of black smoke and dust. 'You see a strength,' The rogue jests as he steps out of a nearby shadow, 'I see a target.'",
        "Offense Ability": "Dead Eye - You gain double effect from the Aim Action. On a success, you also gain the benefit of Enemy Status or Vital Scan on a single target.\n    \u2022 Altered Aim",
        "Defense Ability": "Tuck and Roll - After a Dive, you can perform a Coordination(DC 10) check to avoid landing Prone.\n    \u2022 Altered Dive",
        "Mobility Ability": "Back Stab - You can move behind a target to give the target an additional stage of Flanked",
        "Special Ability": "Shadow Step - If you are Hidden 3 to all enemies, you can use the Acrobatics check to teleport to another hidden location. \n    \u2022 Altered Acrobatics"
        },
    "Druid":{
        "Description": "A Druid is one who has an inseparable connection to nature and life. They are gifted with animal forms, the controlling weather, and calling bestial spirits to aid them.\n\u2022 The wind whips past the trees almost making a pitch, like an ancient whistle from an unknown age. 'We can always smoke you out!' The three wild men call out. They stand at the edge of a forest with lit torches. A stag steps forward. 'Now you'll come with us peaceably so we won't have to resort to fire.' The stag charges at them ramming its points into the first man, who coughs up blood as he drops to the floor. His torch begins to light the brush on fire. The second man fires an arrow that rips into the deer. Instantaneously it transforms into a falcon what dives after him, shifting into a bear that slams into him, his claws make sort work of the archer. The bear lifts its blood soaked head from the corpse to see the final man who is raising his torch above a barrel. The fire blazed behind the bear as it shifts into a youthful woman, the arrow still in her side. She sings a peaceful note that seems to be carried on the wind as her eyes flood in a bright white hue. The warrior moves his hand to the barrel but he is cut off as spectral wolves rip his body apart. The druid's song ends as the rain picks up where she left off, dousing the growing flames back to ash.",
        "Offense Ability": "Hunter Form - You gain a Hunter Form for Transform",
        "Defense Ability": "Defender Form - You gain a Defender Form for Transform. You can use the Transform action to transform into your Defender form as a reaction for 4 RP",
        "Mobility Ability": "Sprinter Form - You gain a Sprinter Form for Transform. If you are moving in a straight line, you can Transform into your Sprinter form for 4 movement and or AP.",
        "Special Ability": "Partial Polymorph - You can perform an Improvise(DC 10) check to gain one of the actions or bonuses from one of your forms for the following action."
        },
    "Sorcerer":{
        "Description": "A Sorcerer is a wielder of elemental power able to cast spells and attacks from one of the elements they are attuned to: Light, Wind, Nature, Water, Earth, Fire, and Lightening. They can either bend the element to their will turning the battled field against their opponents, or create it them selves in ever greater and more powerful ways\n\u2022 The ship tossed violently on the water, the merfolk glared their thin razor teeth at the crew as they clawed aboard. The passengers huddled together and prayed, not knowing what could save them. A scarred woman stepped forward. Burned skin from the years of mistakes trace down to her hands that seem to be holding chaotic orbs of fire, barely able to be contained. The Merfolk rush in, not afraid of the fire in such a place. The Sorceress lets out a flare of fire at the first, melting its skin on contact. A fiery figure of a hand from the first to the second, mirroring the movement of her own hand as the flames consume the second. The final merfolk races toward her trying to throw her off guard, but is met with a fiery dagger that impales it. Stepping back, it realizes that the wound is not that deep and regains its confidence. It is about to lunge forward when the sorceress snaps her fingers causing an explosion to set off from the dagger that impaled still lodged in the assailant. Whats left of his corpse drops to the ground.",
        "Light":{
            "Offense Ability": "Light - Emboldening Light - You can amplify a light source to perform a Light attack against all targets looking at it\nDark - Amplified Shadows - You can amplify the darkness in any shadow or not directly lit area giving a stage of Blinded and Hidden to all targets within",
            "Defense Ability": "Light - Mirage -  You can bend light around a target within your attack range to make them harder to see. Perform a Feint check and replace the effect. New effect: Target gains a stage of Cover and all attackers against the target gain a stage of Confused.",
            "Mobility Ability": "Light - Pinpoint - You can perform Find Vitals check to illuminate the vital points of a target as long as you maintain eyesight on them. On a success, all Vital Attacks against the target can add your CHA Mod\nDark - Pitch Black- For each stage of Cover you have within range of a Blinded 3 target, the target minuses your CHA Mod from their reactions.",
            "Special Ability": "Light - Revitalize - You can perform a Encourage check to heal a target up to the top of its current Health Tier\nDarkness - Long Night - You can perform a Pacify check to prevent a target from Healing at the top of their turn."
        },
        "Wind":{
            "Offense Ability": "Gust - If you have 2 Elemental Weapons, you can create a constant wind between the two while you are within range. And creature moving through or ending their turn in this wind will take the Shove action and any object between passing between the two will take the Throw action with your CHA mod worth of Force units. Once either weapon performs another action, the Gust ends.",
            "Defense Ability": "Head wind - You can perform a Parry check to veer an incoming attack with wind. On a success, the target subtracts the difference from their attacks for the rest of their turn.",
            "Mobility Ability": "Tailwind - When you Lunge, you gain 2 stages of Momentum and can move up to 5 yards away.",
            "Special Ability": "Billow - You can perform a Battlefield(DC=10) to increase the Momentum of Wind by 1 stage in a direction for 1 turn. (Diagonally or Orthogonally only)"
        },
        "Nature":{
            "Offense Ability": "Seeded - On a successful attack from your Elemental Weapon, you can seed a target. At the start of the players 2nd turn from this, you can attempt a Grapple check for 0 AP against the targeted area",
            "Defense Ability": "Trees - Adaptive armor that adds your CHA Mod to Defend and on saves verse External status effects",
            "Mobility Ability": "Vines - You can animate a vine to perform a grapple check. On a success (or a willing target), the target can be pulled to any spot within the vine's range.",
            "Special Ability": "Brush - You can plant a delayed effect through seeds. In two turns the seeds will sprout to perform 2 +5 Wrestle checks. "
        },
        "Water":{
            "Offense Ability": "Water - Water Torture - After a successful attack, you can perform a Choke check for 2 AP.\nIce - Numbing - On every successful attack, the target must make a (DC 10 + number of attacks in combat) Vitality check. On a fail they take a stage of Fatigued",
            "Defense Ability": "Water - Fluid movement - Can use water to perform a Dive check but without moving outside your current position.\nIce - Slick - Can perform a Trip check by putting ice in a targets path out to a range of 4 yards.",
            "Mobility Ability": "Walk on water- You can move on the surface of water.",
            "Special Ability": "Flash Freeze - You can use an Improvise check to instantly turn one Size unit of any Freezable material to ice."
        },
        "Earth":{
            "Offense Ability": "Shaky Ground - Every successful attack against an enemy allows you to make a Shove check for 2 AP",
            "Defense Ability": "Stone - Stone Shield - You can Encase yourself in stone to receive +5 on a Defend check.",
            "Mobility Ability": "Sand - Sand Surfing - You can move through sand while maintaining Hidden.",
            "Special Ability": "Turf - Earthen Clay - Can mold 5 cubic feet of earth within range to perform any STR or DEX Action (except for coordination checks) but using your CHA Mod."
        },
        "Fire":{
            "Offense Ability": "Blaze - You can consume Burning statuses to fuel a stronger Attack. For each stage stage of Burning you consume within range, your next attack can have +1 Capacity \n     \u2022Additionally you can fuel higher power rank special moves equal to 1 power rank per Burning status",
            "Defense Ability": "Burning Rebuke - You can replace the Parry Effect to add a stage of Burning to the attacker for every damage or status you take in the attack.\n    \u2022 Altered Parry",
            "Mobility Ability": "Heart of the Fire - Each Burning status within 3 yards of you adds one success toward your power rank. If they are extinguished, you lose 1 power rank for each square extinguished.",
            "Special Ability": "Detonate - You can perform an Improvise(DC 10) consume one Burning status within attack range to charge an inanimate object you touch with energy which will explode in 1 turn consuming the object and propelling your CHA mod worth of Force Units in a radius."
        },
        "Lightning":{
            "Offense Ability": "Chain Lightning - On a successful Attack (or if the target uses Defend) you can perform a Taunt check to turn the target into an Elemental weapon.",
            "Defense Ability": "On a successful Defend or Parry against a melee attack, you can add a stage of Stunned to the target.",
            "Mobility Ability": "You can charge your elemental weapon by moving 3 yards.",
            "Special Ability": "You can charge a Conductive object within your range. The first three targets that walk through the range of the object must roll a Concentration check or become an Elemental Weapon."
        }
    
    },
    "Arcanist":{
        "Description": "Unlike sorcerers who bend the elements after being imbued with power from them, Arcanists hunt for magic to command the dormant power in everything from the human mind to gravity itself. They are accustomed to seeing unorthodox solutions to problems by manipulating the forces of matter, gravity, mind, and spirit.\n\u2022 The drake stares down the only enemy left, a feeble scholarly looking young man holding only a dagger. The man's four companions lie on the ground around him. The drake circles him, almost toying with his prey. Bringing the blade to his hand, the man tears it into his own flesh. Blood glows a faint red on the blade as the scholar's eyes light in an incandescent hue. The four compatriots rise from their grave and rush at the drake, their undead forms racing forward with vicious speed. Battering them away, the drake preps his fiery breath. An unearthly chanting can be heard, speaking from the ground as the dragonling's fire blasts out incinerating one of the undead. It screams in pain as another's spear slashes into its side. It can barely react before milky dark tentacles erupt from the ground, binding it as they coil around its limbs. Looking at the scholar now walking to it calmly, fear floods over its pinned frame. The feeble man utters an unknown tongue as he jabs the blade into his stomach, never flinching. Ghostly fingers wreath the man's hand in a spectral flame as he plants it on the skull of the beast. It's hatred slowly burns away, replaced with apathy, and then eventually, loyalty and love. The tentacles fade away, as they are no longer needed. The beast bows to its new master.",
        "Mind":{
            "Offense Ability": "Mental Torture - You can perform an altered Distract check to attempt to damage a target with a mental status. On a success, erase the mental status of the target. For each stage of statuses erased, the target takes 1 damage.",
            "Defensive Ability":"Illusionary Duplicate - You can perform an altered Dive check that leaves an illusionary copy of yourself in your place. This copy can only perform the Taunt action and Dodge reaction. Once this illusion is hit with an attack, it disappears. You can only have one duplicate at a time. a successful Defend or Parry against a melee attack, you can add a stage of Stunned to the target.",
            "Mobility Ability": "Dominate Mind - You can perform a Pacify/Taunt check to dominate the mind of one living creature you touch. On a success, the target is gains a stage of Confused  and it under your control until they Crit Fail. As long as the target is Confused, their stage of confused is equal to their distance from you in yards (max 3)\n    \u2022 Altered Pacify/Taunt",
            "Special Ability": "Memory Loss - You can replace the Effect of Feint  to make a character forget the last round of combat and they take the Mental statuses and disposition they had at the beginning of their previous round."
        },
        "Matter":{
            "Offense Ability": "Transmutation - You can perform an Improvise(DC 10) check to change the physical matter of one inanimate object that you touch as long as you maintain touch with it. It retains its shape but upon letting go it will revert to the original material and location.",
            "Defensive Ability":"Enlarge - You can replace the Effect of Dive  with an Enlarge reaction to double the size of any inanimate object you touch (doubled size must be no more than 1 size unit). This grants you at least 1 stage of Cover while behind it. The target reverts at the beginning of your next turn.",
            "Mobility Ability": "Phase - You can Phase through solid objects. You can Phase through 1 size unit of material for each stage of Momentum that you have. If the size is too large, you will collide with the exterior of the object and take Damage from the Impact.",
            "Special Ability": "Partial Transmutation - You can perform an Improvise check to transmute a material you touch with one property of another material you see within range. The change lasts for the turn."
        }, 
        "Gravity":{
            "Offense Ability": "Propel - You can Shove/Throw a target in range with your INT mod worth of Force Units. On a success, the target is considered Thrown.",
            "Defensive Ability":"Hold - You can Parry  with gravity to stop a physical attack against you. On a success you can evade the attack and, if it is a weapon attack, attempt a free Disarm check. If the Disarm is successful, you can pull the weapon to you and equip it in a free hand.",
            "Mobility Ability": "Hover - If you Levitate yourself, you can Leap to move yourself up to your INT mod worth of yards and gaining a Momentum stage for every 2 squares moved.",
            "Special Ability": "Levitate - You can replace the Effect of Grapple to lift a target with your INT Mod +2 worth of Force Units until the start of their next turn (replace Range with your Attack range). On a success, gravity no longer affects the target and its weight units are reduced to 1 for the purpose of Impact. Additionally the target can only move by performing Acrobatics checks on objects within reach or by external Force being pushed against it. \n    \u2022 Altered Grapple"
        }, 
        "Spirit":{
            "Offense Ability": "Possession - You can use an Encourage check send a willing spirit into a lifeless form to possess it and operate through it.",
            "Defensive Ability":"Retribution - You can perform a Parry check to take any damage and/or status you suffer and mirror it back on the attacker two fold.",
            "Mobility Ability": "Graveyard - You can perform a Bandage check on a creature that died in the past minute and heal all of your missing Health Blocks (broken Health tiers are unaffected).",
            "Special Ability": "Not Forgotten - You can perform a Pacify/Taunt check on the spirit of any creature that died in the past minute. On a success, they become a willing spirit."
        }
    }
}


# statuses

statuses_dict = {
    "Name":{
        "Type": "string(status types)",
        "Description":"string",
        "Stage1": "string",
        "Stage2": "string",
        "Stage3": "string"
    },
    "Bleeding":{
        "Type": "Physical",
        "Description":"Losing Blood\n  \u2022 Removal - Bandage(self/ally) check to douse. RDC",
        "Stage1": "\u2022 Take 1 damage at the beginning of the next turn (after regen)",
        "Stage2": "\u2022 Take 2 damage at the beginning of the next turn. (after regen)",
        "Stage3": "\u2022 Take 3 damage at the beginning of the next turn. (after regen)"
    },
    "Blinded":{
        "Type": "Physical",
        "Description":"Impaired vision\n  \u2022 Removal - Bandage(ally)/Recover(self) check RDC.",
        "Stage1": "\u2022 -2 Attack",
        "Stage2": "\u2022 -5 Attack\n  \u2022 -5 Reactions vs Ranged attacks",
        "Stage3": "\u2022 -10 Attack\n  \u2022 -10 Reactions vs Ranged attacks"
    },
    "Burning":{
        "Type": "Physical",
        "Description":"On Fire\n  \u2022  *Flammable objects adjacent to anything Burning must roll a reaction, if applicable (RDC), or take stages of burning equal to the origin of the status - 1. \nRemoval - Auto decrease\n Improvise (self/ally) check to douse. DC determined by GM",
        "Stage1": "\u2022 Take 1 damage at the beginning of the next turn (after regen)",
        "Stage2": "\u2022 Take 2 damage at the beginning of the next turn. (after regen)",
        "Stage3": "\u2022 Take 3 damage at the beginning of the next turn. (after regen)"
    },
    "Cripppled":{
        "Type": "Physical",
        "Description":"Damaged Limbs\n  \u2022 Removal - Bandage(self/ally) check RDC",
        "Stage1": "ARM \u2022 -2 on all actions/reactions with arm\nLEG \u2022 -2 MP and Dodge",
        "Stage2": "ARM \u2022 -5 on all actions/reactions with arm\n\u2022 Ever attack against arm adds a Disarm action\nLEG \n\u2022Double movement Cost and -5 Dodge\n\u2022 Every attack against leg adds a Trip action",
        "Stage3": "ARM \u2022 -10 on all actions/reactions with arm\n\u2022 Ever attack against arm adds a +5 Disarm action\nLEG \n\u2022 Triple movement Cost and -10 Dodge \n\u2022 Every attack against leg adds a +5 Trip action"
    },
    "Deafened":{
        "Type": "Physical",
        "Description":"Impaired hearing\n  \u2022Removal - Bandage(ally)/Recover(self) check RDC.",
        "Stage1": "\u2022 -1 RP",
        "Stage2": "\u2022 -2 RP\n  \u2022 Attacks from out of sight add a stage of Surprised.",
        "Stage3": "\u2022 -4 RPs. Cannot hear allies or enemies.\n\u2022 Attacks from out of sight add two stages of Surprised"
    },
    "Fatigues":{
        "Type": "Physical",
        "Description":"Soreness and lack of stamina\n  \u2022 Removal - Recover (self) check RDC",
        "Stage1": "\u2022 +1 AP cost on all actions",
        "Stage2": "\u2022 +2 AP cost on all actions",
        "Stage3": "\u2022 +3 AP cost on all actions"
    },
    "Impaled":{
        "Type": "Physical",
        "Description":"Lodged fragments or shrapnel in body\n  \u2022 Removal - Bandage(self/ally) check RDC\n    \u2022 Failed Bandage Check Adds a stage of Bleeding or Crippled",
        "Stage1": "\u2022 Take 1 damage for every 2 actions of the impaled limb",
        "Stage2": "\u2022 Take 1 damage for every action of the impaled limb",
        "Stage3": "\u2022 Take 2 damage for every action of the impaled limb"
    },
    "Captivated":{
        "Type": "Mental",
        "Description":"Antagonized or focussed on a specific enemy\n  \u2022 Removal - Focus (self)/Encourage (ally) check RDC",
        "Stage1": "\u2022 +1 AP on all actions and movement not directed to the source of the status",
        "Stage2": "\u2022 +2 AP on all actions and movement not directed to the source of the status",
        "Stage3": "\u2022 +3 AP on all actions and movement not directed to the source of the status"
    },
    "Confused":{
        "Type": "Mental",
        "Description":"Lack of clear thinking or blurred understanding.\n  \u2022 Removal - Focus (self)/Encourage (ally) check RDC",
        "Stage1": "\u2022 Crit Fail threshold raises by 1 each turn\n\u2022 Resets on Crit Fail",
        "Stage2": "\u2022 Crit Fail threshold raises by 2 each turn\n\u2022 Resets on Crit Fail",
        "Stage3": "\u2022 Crit Fail threshold raises by 3 each turn\n\u2022 Resets on Crit Fail"
    },
    "Frightened":{
        "Type": "Mental",
        "Description":"Antagonized or focussed on a specific enemy\n  \u2022 Removal - Focus (self)/Encourage (ally) check RDC",
        "Stage1": "\u2022 +1 AP on all actions and movement directed to the source of the status",
        "Stage2": "\u2022 +2 AP on all actions and movement directed to the source of the status",
        "Stage3": "\u2022 +3 AP on all actions and movement directed to the source of the status"
    },
    "Stunned":{
        "Type": "Mental",
        "Description":"A state of inaction or delayed mental composure\n*If initiative position is knocked below the bottom of the round, you lose a turn but gain the first initiative position the next round.*\n\u2022 Removal - Focus (self)/Encourage (ally) check RDC",
        "Stage1": "\u2022 Move back 1 position in the initiative order",
        "Stage2": "\u2022 Move back 3 position in the initiative order",
        "Stage3": "\u2022 Move back 5 position in the initiative order\n\u2022 Gain 1 stage of Prone."
    },
    "Momentum":{
        "Type": "Situational",
        "Description":"Additional force added to attacks\n  \u2022 adds Impact equation\n\u2022 * Gain stages through Positioning and/or charging at enemies in a straight line. \n\u2022 Stage 1= 5 consecutive yards \n\u2022 Stage 2 = 10 consecutive yards \n\u2022 Stage 3 = 20 consecutive yards",
        "Stage1": "\u2022 -1 Crit threshold in the momentum direction\n\u2022 On hit, target Armor -2 Durability",
        "Stage2": "\u2022 -2 Crit threshold in the momentum direction\n\u2022 On hit, target Armor -3 Durability",
        "Stage3": "\u2022 -3 Crit threshold in the momentum direction\n\u2022 On hit, target Armor -5 Durability"
    },
    "Prone":{
        "Type": "Situational",
        "Description":"Degrees of being knocked down or not in a readied combat stance\n\u2022 Removal - using AP to stand. 2 AP per stage",
        "Stage1": "\u2022 -2 on reactions",
        "Stage2": "\u2022 -5 on reactions",
        "Stage3": "\u2022 -10 on reactions"
    },
    "Restrained":{
        "Type": "Situational",
        "Description":"Limbs or body that are unable to move freely or are bound by an external force\n\u2022 Removal - Contest your Muscle check against their Grapple check to break free.\n  \u2022 Muscle check is made with a -5 per stage",
        "Stage1": "\u2022 Any restrained limb is considered Crippled 1",
        "Stage2": "\u2022 Any restrained limb is considered Crippled 2",
        "Stage3": "\u2022 Any restrained limb is considered Crippled 3"
    },
    "Suffocating":{
        "Type": "Situational",
        "Description":"Restricted breathing\n *When CON Mod reaches -3 target is Unconscious\n\u2022 Removal - Contest your Muscle check against their Choke check to break free.\n  \u2022 Muscle check is made with a -5 per stage",
        "Stage1": "\u2022 -1 CON Mod per turn",
        "Stage2": "\u2022 -3 CON Mod per turn",
        "Stage3": "\u2022 -5 CON Mod per turn"
    },
    "Surprised":{
        "Type": "Situational",
        "Description":"Unaware or unprepared for an attack \n\u2022 Removal - CAll stages lost after the the target is aware of the source of the status",
        "Stage1": "\u2022 Replace the reaction roll with a d20 + Dodge/Defend Respectively",
        "Stage2": "\u2022 Replace the reaction roll with a d20",
        "Stage3": "\u2022 Replace the reaction roll with a d20\n \u2022 Crit fails count as vital 2"
    }
  }


# positions
positions_dict = {
    "Name":{
    "Description":"string",
    "Stage1": "string",
    "Stage2": "string",
    "Stage3": "string"
    },
    "Cover":{
        "Description":"Partly obscured from attacks",
        "Stage1": "\u2022 +5 reactions behind cover",
        "Stage2": "\u2022 +10 reactions behind cover",
        "Stage3": "\u2022 Cannot be targeted by attacks that require sight"
    },
    "Flanked":{
        "Description":"Attacks from the target's peripherals or behind their view",
        "Stage1": "\u2022 Attacks against the target have a -1 Crit threshold",
        "Stage2": "\u2022 Attacks against the target have a -2 Crit threshold",
        "Stage3": "\u2022 Attacks against the target have a -5 Crit threshold"
        },
    "Hidden":{
        "Description":"Unable to be seen or unable to be targeted for attacks",
        "Stage1": "\u2022 First attack from hidden gives the target Surprised 1",
        "Stage2": "\u2022 First attack from hidden gives the target Surprised 2",
        "Stage3": "\u2022 First attack from hidden gives the target Surprised 3"
    },
    "High Ground":{
        "Description":"Being above the targets and gaining power behind attacks",
        "Stage1": "\u2022 Being above a target giving 1 stage of Momentum",
        "Stage2": "\u2022 Being above a target giving 2 stage of Momentum",
        "Stage3": "\u2022 Being above a target giving 3 stage of Momentum"
        },
    "Unbalanced":{
        "Description":"Being above the targets and gaining power behind attacks",
        "Stage1": "\u2022 Failed reactions give you a stage of Prone",
        "Stage2": "\u2022 Failed reactions give you a stage of Prone\n\u2022Every Physical Action against you can add a Shove Check for 0 AP",
        "Stage3": "\u2022 Failed reactions give you a stage of Prone\n\u2022Every Physical Action against you can add a Shove Check for 0 AP\n\u2022 Movement provokes a Trip action against you DC 15"
        }
    }


# Damage Types

damage_types_dict = {
    "Name":
    {
        "Type": "string",
        "Description": "string",
        "Mechanics": "string",
        "Effect": "string",
        "Statuses": 
        [
            "string",
            "string"
        ]
    },
    "Piercing":
    {
        "Type": "Physical",
        "Description": "A physical attack meant to impale the point of a weapon in a target",
        "Mechanics": "\u2022 -1 Crit threshold vs Vitals\n\u2022 Can choose to damage a target or give the target a stage of:\n     \u2022 Impaled\n     \u2022 Blinded",
        "Effect": "Crit Threshold -1",
        "Statuses": 
        [
            "Blinded",
            "Impaled"
        ]
    },
    "Slashing":
    {
        "Type": "Physical",
        "Description": "A physical attack that sweeps a bladed edge against a target",
        "Mechanics": "\u2022 Can Dismember a limb that is Crippled 3\n\u2022 Can choose to damage a target or give the target a stage of:\n     \u2022 Bleeding\n     \u2022 Blinded\n     \u2022 Crippled",
        "Effect": "if target_crippled_stage == 3: ",
        "Statuses": 
        [
            "Damage",
            "Bleeding",
            "Blinded",
            "Crippled"
        ]
    },
    "Bludgeoning":
    {
        "Type": "Physical",
        "Description": "A physical attack that impacts a blunt weapons against a target",
        "Mechanics": "\u2022 Double Damage against armor\n\u2022 Can choose to damage a target or give the target a stage of:\n     \u2022 Fatigued\n     \u2022 Deafened\n     \u2022 Crippled\n     \u2022 Confused\n     \u2022 Stunned",
        "Effect": "target_armor_durability = - 2 ",
        "Statuses": 
        [
            "Damage",
            "Fatigued",
            "Deafened",
            "Crippled",
            "Confused",
            "Stunned"
        ]
    },
    "Fire":
    {
        "Type": "Elemental",
        "Description": "A fire damage that gives a target stages of Burning",
        "Mechanics": "\u2022 Can be boosted by Flammable materials\n\u2022 Can choose to damage a target or give the target a stage of:\n     \u2022 Burning",
        "Effect": "",
        "Statuses": 
        [
            "Damage",
            "Burning"
        ]
    },
    "Freezing":
    {
        "Type": "Elemental",
        "Description": "A cold damage that can damage and give a target stages of Frozen",
        "Mechanics": "\u2022 Can be boosted by Freezable materials\n\u2022 Can choose to damage a target or give the target a stage of:\n     \u2022 Frozen",
        "Effect": "",
        "Statuses": 
        [
            "Damage",
            "Frozen"
        ]
    },
    "Lightning":
    {
        "Type": "Elemental",
        "Description": "An electric damage that damages and turn a target into an Elemental Weapon",
        "Mechanics": "\u2022 Can be boosted by Conductive materials",
        "Effect": "",
        "Statuses": 
        [
            "Damage"
        ]
    },
    "Acid":
    {
        "Type": "Arcane",
        "Description": "A corrosive attack that burns and dissolves organic matter",
        "Mechanics": "\u2022 Only effects Animal and Vegetable materials\n\u2022 Can choose to damage a target or give the target a stage of:\n     \u2022 Burning",
        "Effect": "",
        "Statuses": 
        [
            "Damage",
            "Burning"
        ]
    },
    "Chaos":
    {
        "Type": "Arcane",
        "Description": "A corrosive attack that burns and dissolves organic matter",
        "Mechanics": "",
        "Effect": "",
        "Statuses": 
        [
            "Damage",
            "Burning"
        ]
    },    
    "Necrotic":
    {
        "Type": "Arcane",
        "Description": "Arcane energy that decreases the very life force of a target",
        "Mechanics": "\u2022 Does not effect non living targets",
        "Effect": "",
        "Statuses": 
        [
            "Damage"
        ]
    }
}


      #creating stats  



Dougey = PC("Dougey", "Brute", "Human", "Blue", "Skin_Tone", "Hair_Color", 1, 4, "Trademarks", 25, 15, 20, 5, 10, 15, 2, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 2, 0, 0, 1, 2, 2, 1, 0, 1, 0, 0, 0, 2, 2, 2, "Offensive_Ability", "Defensive_Ability", "Movement_Ability", "Special_Ability", "Long Sword", "Off_Hand", "Utility", "Leather Armor", "Combat_Special_Move", "Backpack", "Gold", "Rations", "Kits", "Adventuring_Special_Moves", "Value_Self", "Value_Others", "Value_Society", "Mission", "Interests", "Talents", "Quirks", "Fears", "Family", "Friends", "Professional", "Nemesis", "Factions", "Home", "Profession", "Skill", "Race_Bonus", "Story", "Roleplaying_Special_Moves")

Guard = Creature("Guard", 1, "1x1", 4, "Human", "Flesh", "Dumb Idiot", "Attacks", "Spear", "Chain Mail", "Combat_Special_Moves", 2, 2, 2, "Immunities", "Weaknesses", "Vitals_1", "Vitals_2", "Vitals_3", "Reactions", "Combat_Role", "Tactics_1", "Tactics_2", "Tactics_3", "Value", "Needs", "Mission", "Role_Playing_Special_Moves", 30, 15, 20, 2, 5, 10, 1, 2, 1, 1, 0, 1, 2, 1, 4, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, "Equipment", "Backpack", "Adventuring_Special_Moves", "Adventuring_Difficulty", "Role_Playing_Difficulty", "Combat_Difficulty")

Maincharacter = Dougey.Name
Guard_name = Guard.Name

def mods(attribute):
    mod = (attribute // 5) - 2
    return mod

str_mod = mods(Dougey.STR)
dex_mod = mods(Dougey.DEX)
con_mod = mods(Dougey.CON)
int_mod = mods(Dougey.INT)
wis_mod = mods(Dougey.WIS)
cha_mod = mods(Dougey.CHA)

character_str_mod = str_mod


print(character_str_mod)

print(Maincharacter, Guard_name)

print(Dougey.blinded_status_stage)
print(Dougey.Max_AP)
print(Dougey.HP["Prime"])

 

 #Dice Roller

def roll_dice(low,high,fail,crit):
  total = random.randint(low,high)
  if total <= fail:
    print("You rolled a " + str(total) + " which is a Critical Fail")
    return "Critical Fail"
  elif total >= crit:
    print("You rolled a " + str(total) + " which is a Critical!")
    return "Critical"
  else:
    print("Roll = " + str(total))
    return total



# Contest function

#Player starts turn, 
# prompt player with action
# player selects action 
# prompt player with description and get confirmation
# if the player doesn't confirm, prompt again
# player selects target, rolls and adds modifiers, the target then selects a reaction (unless predefined in action) and rolls + modifiers. (prompt GM for approval) If Player > target, apply payload, else no effect. Deduct AP
# else if the action is a scale - roll and add modifiers, then prompt GM for approval, then apply the effect based on the range. Deduct AP
# else if the action is a DC, roll and add modifiers, then prompt GM for approval, if yes, apply effect. Deduct AP

def contest(source,action,target):

  source_stat = mods(int(eval(str(source.Name) + "." + str(actions_dict[action]["Stat"]))))
  source_skill = eval(str(source.Name) + "." + str(actions_dict[action]["Skill"]))
  source_mod = eval(str(source.Name) + ".misc_bonus")
  source_crit = eval(str(source.Name) + ".crit_threshold")
  source_crit_fail = eval(str(source.Name) + ".crit_fail_threshold")

  target_name = eval(target + ".Name")
  target_crit = eval(target + ".crit_threshold")
  target_crit_fail = eval(target + ".crit_fail_threshold")

  #set up crit success and crit fail
  source_dice = roll_dice(1,20,source_crit_fail,source_crit)


    #roll source actions
  if type(source_dice) == "str":
    source_roll = source_dice
  else:
    source_roll = source_dice + source_stat + source_skill + source_mod
  print("After all bonuses, your total is " + str(source_roll))

  source_mod = 0

  reaction = actions_dict[action]["Reaction"]
  print(target + ", Roll a " + reaction + " check as a reaction.")

  if reaction == "Muscle" or "Wrestle" or "Brawl" or "Jump":
    reaction_stat = "STR"
  elif reaction == "Coordination" or "Finesse" or "Sleight" or "Stealth":
    reaction_stat = "DEX"
  elif reaction == "Endurance" or "Concentration" or "Vitality":
    reaction_stat == "CON"
  elif reaction == "Academic" or "Arcana" or "Culture" or "Investigation" or "Nature":
    reaction_stat = "INT"
  elif reaction == "Insight" or "Interaction" or "Medicine" or "Perception" or "Survival":
    reaction_stat = "WIS"
  elif reaction == "Aggressive" or "Suave" or "Diplomatic" or "Sincere":
    reaction_stat = "CHA"
  else:
    reaction_stat = input("What is the stat for your reaction: STR; DEX; CON; INT; WIS; CHA")
  
  target_stat = mods(eval(str(target) + "." + reaction_stat))
  target_skill = eval(str(target) + "." + reaction)
  target_armor = eval(target + ".Armor")


  target_roll = roll_dice(1,20,target_crit_fail,target_crit) + target_stat + target_skill + eval(target + ".misc_bonus")
  print(target + "'s " + reaction + " is total is " + str(target_roll))
  
  if source_roll == target_roll:
    print("You both tied and cancel each other out")
  elif source_roll == "Critical":
    print("You rolled a critical success!")
    result = "Critical"
  elif source_roll == "Critical Fail":
    print("You rolled a critical fail")
    result = "Critical Fail"
  elif target_roll == "Critical":
    print("Your target rolled a critical success, you fail")
    result = "Critical Fail"
  elif target_roll == "Critical Fail":
    print("Your target rolled a critical fail, you succeed")
    result = "Critical"
  elif source_roll > target_roll:
    print("You succeed!")
    result = "Success"
  else:
    result = "Fail"
    print("Sorry, you failed")
  return result


  # Special action function for actions that trigger a target's choice of standard reactions

#Player starts turn, 
# prompt player with action
# player selects action 
# prompt player with description and get confirmation
# if the player doesn't confirm, prompt again
# if the action is a contest, player selects target, rolls and adds modifiers, the target then selects a reaction (unless predefined in action) and rolls + modifiers. (prompt GM for approval) If Player > target, apply payload, else no effect. Deduct AP
# else if the action is a scale - roll and add modifiers, then prompt GM for approval, then apply the effect based on the range. Deduct AP
# else if the action is a DC, roll and add modifiers, then prompt GM for approval, if yes, apply effect. Deduct AP

def special_action(source,action,target,reaction):
  #set up sourse variables
  source_weapon = eval(str(source.Name) + ".Main_Hand")
  source_stat = mods(int(eval(str(source.Name) + "." + str(actions_dict[action]["Stat"]))))
  source_skill = eval(str(source.Name) + "." + str(actions_dict[action]["Skill"]))
  source_mod = eval(str(source.Name) + ".misc_bonus")
  source_crit = eval(str(source.Name) + ".crit_threshold")
  source_crit_fail = eval(str(source.Name) + ".crit_fail_threshold")



  #set up target Variables
  
  target_name = eval(target + ".Name")
  target_armor = eval(target + ".Armor")
  target_crit = eval(target + ".crit_threshold")
  target_crit_fail = eval(target + ".crit_fail_threshold")

  #set up crit success and crit fail
  source_dice = roll_dice(1,20,source_crit_fail,source_crit)


    #roll source actions
  if type(source_dice) == "str":
    source_roll = source_dice
  else:
    source_roll = source_dice + source_stat + source_skill + source_mod
  print("After all bonuses, your total is " + str(source_roll))

  source_mod = 0

  #get target reaction
  print(target + " chose to react with " + reaction)


  print(target + ", Roll a " + reaction + " check as a reaction.")

  # Roll reaction for target 
  target_stat = mods(eval(str(target) + "." + actions_dict[reaction]["Stat"]))
  target_skill = eval(str(target) + "." + actions_dict[reaction]["Skill"])
  target_armor = eval(target + ".Armor")

  if actions_dict[reaction]["Dice_Roll"] == "d6":
    target_dice = roll_dice(1,6,0,target_crit)
    if reaction == "Block":
      target_roll = target_dice + armors_dict[target_armor]["Defend"] + math.floor(armors_dict[target_armor]["Block_Bonus"] * (target_stat + target_skill))
      print("The targets' " + reaction + " roll is " + str(target_dice) + " dice roll + " + str(armors_dict[target_armor]["Defend"]) + " armor base + (" + str(math.floor(armors_dict[target_armor]["Block_Bonus"])) + " modifier of " + str(target_stat + target_skill) + " skill bonus) \nfor a total of \n" + str(target_roll))
    else:
      target_roll = target_dice + armors_dict[target_armor]["Agility"] + math.floor(armors_dict[target_armor]["Dodge_Bonus"] * (target_stat + target_skill))
      print("The targets' " + reaction + " roll is " + str(target_dice) + " dice roll + " + str(armors_dict[target_armor]["Agility"]) + " armor base + (" + str(armors_dict[target_armor]["Dodge_Bonus"]) + " modifier of " + str(target_stat + target_skill) + " skill bonus) \nfor a total of \n" + str(target_roll))
  else:
    target_dice = roll_dice(1,20,target_crit_fail,target_crit)
    if type(target_dice) == "str":
      target_roll = target_dice
    else:
      target_roll = target_dice + target_stat + target_skill
    print("The targets' " + reaction + " is total is " + str(target_roll))



  if source_roll == target_roll:
    print("You both tied and cancel each other out")
  elif source_roll == "Critical":
    print("You rolled a critical success!")
    result = "Critical"
  elif source_roll == "Critical Fail":
    print("You rolled a critical fail")
    result = "Critical Fail"
  elif target_roll == "Critical":
    print("Your target rolled a critical success, you fail")
    result = "Critical Fail"
  elif target_roll == "Critical Fail":
    print("Your target rolled a critical fail, you succeed")
    result = "Critical"
  elif source_roll > target_roll:
    print("You succeed!")
    result = "Success"
  else:
    result = "Fail"
    print("Sorry, you failed")
  return result


def range_action(source,action):
  source_stat = mods(int(eval(str(source.Name) + "." + str(actions_dict[action]["Stat"]))))
  source_skill = eval(str(source.Name) + "." + str(actions_dict[action]["Skill"]))
  source_mod = eval(str(source.Name) + ".misc_bonus")
  source_crit = eval(str(source.Name) + ".crit_threshold")
  source_crit_fail = eval(str(source.Name) + ".crit_fail_threshold")

  #set up crit success and crit fail
  source_dice = roll_dice(1,20,source_crit_fail,source_crit)


    #roll source actions
  if type(source_dice) == "str":
    source_roll = source_dice
  else:
    source_roll = source_dice + source_stat + source_skill + source_mod
  print("After all bonuses, your total is " + str(source_roll))

  source_mod = 0

  return source_roll



def dc_action(source,action):
  source_stat = mods(int(eval(str(source.Name) + "." + str(actions_dict[action]["Stat"]))))
  source_skill = eval(str(source.Name) + "." + str(actions_dict[action]["Skill"]))
  source_mod = eval(str(source.Name) + ".misc_bonus")
  source_crit = eval(str(source.Name) + ".crit_threshold")
  source_crit_fail = eval(str(source.Name) + ".crit_fail_threshold")

  #set up crit success and crit fail
  source_dice = roll_dice(1,20,source_crit_fail,source_crit)


    #roll source actions
  if type(source_dice) == "str":
    source_roll = source_dice
  else:
    source_roll = source_dice + source_stat + source_skill + source_mod
  print("After all bonuses, your total is " + str(source_roll))

  source_mod = 0


  if source_roll == "Critical":
    print("You rolled a critical success!")
    result = "Critical"
  elif source_roll == "Critical Fail":
    print("You rolled a critical fail")
    result = "Critical Fail"
  else:
    result = input("GM, the player rolled a " + str(source_roll) + "\nIs that a Success or a Fail?")

  return result
  

def action_cost(source,action):
  if actions_dict[action]["Speed"] == "~":
    weapon = eval(str(source.Name) + ".Main_Hand")
    action_cost = weapons_dict[weapon]["AP"]
  else:
    action_cost = actions_dict[action]["Speed"]
  return action_cost


def stamina(source):
    source_stamina = source.Stamina
    source.HP[source_stamina] = eval(str(source.Name) + "." + str(source_stamina))
    source_AP = source.Max_AP
    source_RP = source.Max_RP
    source_MP = source.Max_MP
    print(str(source.Name) + ":\nCurrent HP = " + str(source.HP["Prime"] + source.HP["Wounded"] + source.HP["Bloodied"]) + "\nCurrent Stamina = " + source_stamina + "\nAP = " + str(source_AP) + "\nRP = " + str(source_RP) + "\nMP = " + str(source_MP))

  


'''
effect function
this is going to be a crazy one with a lot of twists and turns but here goes nothing

declare the class to take in a source, action, result, and kwargs

start with the simple actions, all they do is change something on a source

evaluate the source '.' attribute and apply the payload
'''

def effect(source,action,result,**kwargs):
  try:
    if result == "Critical":
      exec(source.Name + "." + str(actions_dict[action]["Payload"]))
      exec(source.Name + "." + str(actions_dict[action]["Payload"]))
    elif result == "Fail":
      print("Sorry you Suck")
    elif result == 'Critical Fail':
      print("You really suck bad")
    else:
      exec(source.Name + "." + str(actions_dict[action]["Payload"]))
  except:
    print("Sorry this isn't built out yet here is the error")


def open_phase(source):
  print("Statuses aren't done yet")


def turn(player):
  source = eval(str(player))
  print(str(source.Name) + ", Its your turn!\n\nYour stamina kicks in and regenerates your HP, AP, RP, and MP")
  stamina(source)
  open_phase(source)
  
  source_AP = source.AP
  source_MP = source.MP

  while source_AP > 0:
    action = input("What would you like to do?")
    if action == "Weapon Attack":
      action_AP = weapons_dict[eval(str(source.Name) + ".Main_Hand")]["AP"]
    else:
      action_AP = actions_dict[action]["Speed"]
    print(actions_dict[action]["Description"])
    if int(action_AP) > source_AP:
      action = input("Sorry, you don't have enough AP for that action\nWhat else would you like to do")
    print("You have " + str(source_AP) + " left and the " + action + " action costs " + str(action_AP) + " AP")
    confirmation = input("Do you wish to proceed?")

    if confirmation == "yes":
      if actions_dict[action]["Action_Type"] == "Range":
        result = range_action(source, action)
      elif actions_dict[action]["Action_Type"] == "Contest":
        target = input("Who would you like to target?")
        result = contest(source, action, target)
      if actions_dict[action]["Action_Type"] == "Special":
        target = input("Who would you like to target?")
        reaction = input(target + ", " + source.Name + " is targeting you with a " + action + " action. How do you react?")
        result = special_action(source, action, target, reaction)
      else:
        target = input("Who would you like to target?")
        result = dc_action(source,action)

      source_AP -= int(action_cost(source, action))
    else:
      print("I'll cancel that for you!")

    print("The result of you " + action + " action is " + str(result))
    effect(target,action,result)

    print("You still have " + str(source_AP) + " AP left.")


  print("You are out of AP and your turn is done")
  

def round_mechanics(*initiative_list):
  print("Round Mechanics aren't done yet")


def combat_round(initiative):
  round_mechanics()
  hostile = True
  while hostile == True:
    for combatant in initiative:
      print("Its your turn " + combatant)
      turn(combatant)


def combat_encounter(*combatants):
  initiative = []
  initiative_order = []
  for i in combatants:
    combat_order = {
        "name": i.Name,
        "initiative":roll_dice(1,20,0,21)
        }
    initiative.append(combat_order)

  print(initiative)

  initiative_list = sorted(initiative, key=lambda x: x['initiative'], reverse=True)

  for i in initiative_list:
    print(i["name"], i["initiative"])
    initiative_order.append(i["name"])
    
  for i in initiative_order:
    print(i)

  hostile = True
  while hostile == True:
    combat_round(initiative_order)


combat_encounter(Dougey,Guard)
