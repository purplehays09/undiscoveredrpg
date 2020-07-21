
features_dict = {
    "Name":{
        "Description":"String",
        "Pre_Action":'''

          ''',
        "Post_Action":'''

          ''',
        "Equip":'''

        ''',
        "Unequip":'''

        '''
    },
    "Dual Wielding":{
        "Description":"You can use this weapon in your Off Hand (if available) and attack for -1 AP but with no Techinques. ",
        "Pre_Action":'''
weapon = input("Do you want to use your\n" +  source.Equipment["Main Hand"] + "\n or your\n" + source.Equipment["Off Hand"])
          ''',
        "Equip":'''
if slot == "Off Hand":
  source.Equipment[slot][item]["AP"] -= 1
  source.Equipment[slot][item]["Techniques] = {}

  source.Pre_Action.update("Dual Wielding" = features_dict["Dual Wielding"]["Pre_Action"])
        ''',
        "Unequip":'''
source.Pre_Action.pop("Dual Wielding")
        '''
    },
    "Dueling":{
        "Description":"You can perform Feint, Parry, Riposte, and Disarm for -1 AP/RP respectively. ",
        "Pre_Action":'''
if action == "Feint" or "Disarm":
  source.AP += 1
          ''',
        "Pre_Reaction":'''
if reaction == "Parry" or "Riposte":
  source.RP += 1
          ''',
        "Equip":'''
source.Pre_Action.update(Dueling = features_dict["Dueling"]["Pre_Action"])
source.Pre_Reaction.update(Dueling = features_dict["Dueling"]["Pre_Reaction"])
        ''',
        "Unequip":'''
source.Pre_Action.pop("Dueling")
source.Pre_Reaction.pop("Dueling")
        '''
    },
    "Finesse":{
        "Description":"You can Replace your Muscle skill with your Finesse Skill",
        "Pre_Action":'''
if action == "Weapon Attack":
  source.misc_bonus -= mods(source.Attributes["STR"])
  source.misc_bonus -= source.Skills["Muscle"]

  source.misc_bonus += mods(source.Attributes["DEX"])
  source.misc_bonus += source.Skills["Finesse"]
          ''',
        "Post_Action":'''
if action == "Weapon Attack":
  source.misc_bonus -= mods(source.Attributes["DEX"])
  source.misc_bonus -= source.Skills["Finesse"]

  source.misc_bonus += mods(source.Attributes["STR"])
  source.misc_bonus += source.Skills["Muscle"]
          ''',
        "Equip":'''
source.Pre_Action.update(Finesse = features_dict["Finesse"]["Pre_Action"])
source.Post_Action.update(Finesse = features_dict["Finesse"]["Post_Action"])
        ''',
        "Unequip":'''
source.Pre_Action.pop("Finesse")
souce.Post_Action.pop("Finesse")
        '''
    },
    "Grappling":{
        "Description":"You can perform Wrestle checks with this weapon against a target",
        "Pre_Action":'''

          ''',
        "Post_Action":'''

          ''',
        "Equip":'''

        ''',
        "Unequip":'''

        '''
    },
    "Heavy":{
        "Description":"You can use 2 techniques per attack",
        "Pre_Action":'''

          ''',
        "Post_Action":'''

          ''',
        "Equip":'''

        ''',
        "Unequip":'''

        '''
    },
    "Light":{
        "Description":"Doesn't damage Heavy armors Durability",
        "Post_Roll":'''
if action == "Weapon Attack":
  target_armor = target.Equipment["Armor"]
  if target_armor["Type"] == "Heavy":
    target.Equipment["Armor"][target_armor]["Durability"] += 1
          ''',
        "Equip":'''
source.Post_Roll.update(Light = features_dict["Light"][Post_Roll])
        ''',
        "Unequip":'''
source.Post_Roll.pop("Light")
        '''
    },
    "Thrown":{
        "Description":"You can add 1 stage of momentum to your impact equation when you attack with this weapon at range.",
        "Pre_Action":'''
range = distance(source,target)
if action == "Weapon Attack" and range > 1:
  status(source,momentum,1)
          ''',
        "Post_Action":'''
if action == "Weapon Attack" and range > 1:
  status(source,momentum,-1)
          ''',
        "Equip":'''
source.Pre_Action.update(Thrown = features_dict["Thrown"]["Pre_Action"])
source.Post_Action.update(Thrown = features_dict["Thrown"]["Post_Action"])
        ''',
        "Unequip":'''
source.Pre_Action.pop("Thrown")
source.Post_Action.pop("Thrown")
        '''
    },
    "Versatile":{
        "Description":"You can use the weapon as a Piercing or Slashing weapon.",
        "Pre_Action":'''

if action == "Weapon Attack":
  choice = input("Do you want to use slashing or piercing?")

  if choice == "slashing":
    source.Equipment[weapon]["Type"] = "Slashing"
  else:
    source.Equipment[weapon]["Type"] = "Piercing"
          ''',
        "Equip":'''
source.Pre_Action.update(Versatile = features_dict["Thrown"]["Pre_Action"])

        ''',
        "Unequip":'''
source.Pre_Action.pop("Versatile)
        '''
    },

    #armor features 
    "Agility":{
        "Description":{
                "Stage 1": "+2 to your Coordination Skill",
                "Stage 2": "+5 to your Coordination Skill",
                "Stage 3": "+5 to your Coordination skill\nRolling a 6 on your Dodge Reaction is an automatic success."
        },
        "Pre_Action":'''

          ''',
        "Post_Action":'''

          ''',
        "Equip":'''

        ''',
        "Unequip":'''

        '''
    },
    "Braced":{
        "Description":{
                "Stage 1": "You have a +2 on reactions against Slashing damage",
                "Stage 1": "You have a +5 on reactions against Slashing damage",
                "Stage 3": "You have a +5 on reactions against Slashing damage and you can ignore Stage 1 physical statuses"
        },
        "Pre_Action":'''

          ''',
        "Post_Action":'''

          ''',
        "Equip":'''

        ''',
        "Unequip":'''

        '''
    },
    "Defense":{
        "Description":{
                "Stage 1": "+2 to your Endurance Skill",
                "Stage 2": "+5 to your Endurance Skill",
                "Stage 3": "+5 to your Endurance skill\nRolling a 6 on your Block Reaction is an automatic success."
        },
        "Pre_Action":'''

          ''',
        "Post_Action":'''

          ''',
        "Equip":'''

        ''',
        "Unequip":'''

        '''
    },
    "Fortified":{
        "Description":{
                "Stage 1": "You have a +2 on reactions against Piercing damage",
                "Stage 2": "You have a +5 on reactions against Piercing damage",
                "Stage 3": "You have a +5 on reactions against Piercing damage and you can ignore Stage 1 physical statuses"
        },
        "Pre_Action":'''

          ''',
        "Post_Action":'''

          ''',
        "Equip":'''

        ''',
        "Unequip":'''

        '''
    },
    "Nimble":{
        "Description":{
                "Stage 1": "You can move 1 yard each time you take Coordination Reactions",
                "Stage 2": "",
                "Stage 3": "You can move 1 yard each time you take Coordination Reactions"
        },
        "Pre_Action":'''

          ''',
        "Post_Action":'''

          ''',
        "Equip":'''

        ''',
        "Unequip":'''

        '''
    },
    "Pocketed":{
        "Description":{
                "Stage 1": "",
                "Stage 2": "",
                "Stage 3": ""
        },
        "Pre_Action":'''

          ''',
        "Post_Action":'''

          ''',
        "Equip":'''

        ''',
        "Unequip":'''

        '''
    },
    "Restricting":{
        "Description":{
                "Stage 1": "",
                "Stage 2": "",
                "Stage 3": ""
        },
        "Pre_Action":'''

          ''',
        "Post_Action":'''

          ''',
        "Equip":'''

        ''',
        "Unequip":'''

        '''
    },
    "Unburdened":{
        "Description":{
                "Stage 1": "",
                "Stage 2": "",
                "Stage 3": ""
        },
        "Pre_Action":'''

          ''',
        "Post_Action":'''

          ''',
        "Equip":'''

        ''',
        "Unequip":'''

        '''
    }    
}
