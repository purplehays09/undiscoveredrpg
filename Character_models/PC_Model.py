

class PC:
    def __init__(self, Name, Combat_Class, Race, Eye_Color, Skin_Tone, Hair_Color, Size, Weight, Trademarks, STR, DEX, CON, INT, WIS, CHA, Muscle, Wrestle, Brawl, Coordination, Finesse, Sleight_of_Hand, Stealth, Endurance, Concentration, Vitality, Academic, Arcana, Culture, Analyze, Nature, Aggressive, Suave, Diplomatic, Sincere, Tier_1, Tier_2, Tier_3, Offensive_Ability, Defensive_Ability, Movement_Ability, Special_Ability, Main_Hand, Off_Hand, Utility, Armor, Combat_Special_Move, Backpack, Gold, Rations, Kits, Adventuring_Special_Moves, Value_Self, Value_Others, Value_Society, Mission, Interests, Talents, Quirks, Fears, Family, Friends, Professional, Nemesis, Factions, Home, Profession, Skill, Race_Bonus, Story, Roleplaying_Special_Moves): 
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
        STR_Mod = (STR // 5) - 2
        self.DEX = DEX
        DEX_Mod = (DEX // 5) - 2
        self.CON = CON
        CON_Mod = (CON // 5) - 2
        self.INT = INT
        INT_Mod = (INT // 5) - 2
        self.WIS = WIS
        WIS_MOD = (WIS // 5) - 2
        self.CHA = CHA
        CHA_Mod = (CHA // 5) - 2
        self.Muscle = Muscle
        self.Wrestle = Wrestle
        self.Brawl = Brawl
        self.Coordination = Coordination
        self.Finesse = Finesse
        self.Sleight_of_Hand = Sleight_of_Hand
        self.Stealth = Stealth
        self.Endurance = Endurance
        self.Concentration = Concentration
        self.Vitality = Vitality
        self.Academic = Academic
        self.Arcana = Arcana
        self.Culture = Culture
        self.Analyze = Analyze
        self.Nature = Nature
        self.Aggressive = Aggressive
        self.Suave = Suave
        self.Diplomatic = Diplomatic
        self.Sincere = Sincere
        
        #Health information
        self.Tier_1 = Tier_1
        self.Tier_2 = Tier_2
        self.Tier_3 = Tier_3
        self.Max_Vitality = Tier_3
        self.Current_Vitality = Tier_3

        
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

        # Combat stats 
        self.Attack_Bonus = Muscle + STR_Mod
        self.Dodge_Bonus = Coordination + DEX_Mod
        self.Defend_Bonus = Endurance + CON_Mod
        self.Offensive_Ability = Offensive_Ability
        self.Defensive_Ability = Defensive_Ability
        self.Movement_Ability = Movement_Ability
        self.Special_Ability = Special_Ability
        self.Free_Movement = 4
        self.AP = 12
        self.RP = 4
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
        self.Carry_Weight = 5 + STR_Mod
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


Dougey = PC("Dougey", "Brute", "Human", "Blue", "Skin_Tone", "Hair_Color", 1, 4, "Trademarks", 26, 21, 18, 6, 10, 13, 4, 0, 2, 1, 0, 0, 2, 3, 0, 0, 0, 0, 1, 2, 1, 3, 0, 0, 0, 3, 5, 7, "Offensive_Ability", "Defensive_Ability", "Movement_Ability", "Special_Ability", "Maul", "Off_Hand", "Utility", "ChainMail", "Combat_Special_Move", "Backpack", 100, 5, "Kits", "Adventuring_Special_Moves", "Loyalty", "Compassion", "Cooperation", "Mission", "Interests", "Talents", "Quirks", "Fears", "Family", "Friends", "Professional", "Nemesis", "Factions", "Home", "Profession", "Skill", "Race_Bonus", "Story", "Roleplaying_Special_Moves")

Maincharacter = Dougey.Name

print(Maincharacter)