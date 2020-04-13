
# Define the Class for NPC
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




class Creature:
    def __init__(self, Name, Size, Shape, Weight, Anatomy, Material, Description, Attacks, Weapons, Abilities, Vitality, Immunities, Weaknesses, Vitals, Reactions, Combat_Role, Solo_Tactics, Group_Tactics, Value, Needs, Mission, Stats, Skills, Speed, Adventuring_Difficulty, Role_Playing_Difficulty, Combat_Difficulty):
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
        self.Abilities = Abilities
        self.Vitality = Vitality
        self.Immunities = Immunities
        self.Weaknesses = Weaknesses
        self.Vitals = Vitals
        self.Reactions = Reactions
        self.Abilities = Abilities
        self.Combat_Role = Combat_Role
        self.Solo_Tactics = Solo_Tactics
        self.Group_Tactics = Group_Tactics


        #Charisma = #Charisma
        self.Value = Value
        self.Needs = Needs
        self.Mission = Mission
        self.Abilities = Abilities


        self.Stats = Stats
        self.Skills = Skills
        self.Speed = Speed
        self.Abilities = Abilities