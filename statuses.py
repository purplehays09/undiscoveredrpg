




"""1.   Blinded - can't take into account whether the target is attacking from ranged during the attack action. Pre reaction
2.   Burning - doesn't add in any burning effect to adjacent targets
3.   Crippled - doesn't take into account which arm and it doesn't store them aside from the number action
4.   Deafened - doesn't take into account any flanked direction and therefore doesn't add secondary effect pre roll
5.   fatigued works
6.   Impaled - I need to make a section in the effect action that adds secondary effects. I then need to make a character attribute that stores effect secondary attributes post action/reaction
7.  Captivated - I need to add a function to the action cost function and the turn fuction that changes the AP cost and then store these attributes on the character level pre selection/pre action cost
8.   Confused - I need to add functionality to reset the crit fail threshold after a crit fail. Post roll
9.   Frightened - Same as captivated
10.  Stunned - I need to store the initiative order change
11.   Momentum - I need to create an instance of the armor on the character to keep track of durability, I also need to keep track of consecutive movement and such. Post movement
12.    Prone - I need to program out a way to have the removing functions and things so that movement can get rid of this. I might even have to make payloads for removal and put them on the character class pre movement
13.   Restrained - I need to create the way to remove this, also, maybe change the effect again
14.   Suffocating - add removal and death mechanic when mod reaches -3 add function to class, post open phase
15.   Surprised - add removal on attack, and interrupt for roll equation pre roll
16.   Cover - add an attack direction mechanic pre roll
17.   Flanked - Same as Cover pre roll
18.   Hidden - I don't know, add a hidden from dictionary? hidden dictionary
19.   High Ground - add elevation
20.   Unbalanced - Wait till map post move

character - grid position, character body, armor

function - secondary effect: deafened and impaled and , removal, 

update - attack: ranged, turn: flanked, action_cost and turn : ap change
"""



# statuses

statuses_dict = {
    "Name":{
        "Type": "string(status types)",
        "Description":"string",
        "Stage1": "string",
        "Stage2": "string",
        "Stage3": "string",
        "Interrupt":{
            'Pre_Action':{
              1:'''
              
              ''',
              2:'''
              
              ''',
              3:'''
              
              '''
            }
        },
        "Payload":{
            0:"print('0')",
            1:"print('1')",
            2:"print('2')",
            3:"print('3')"
        }
    },
    "Bleeding":{
        "Type": "Physical",
        "Description":"Losing Blood\n  \u2022 Removal - Bandage(self/ally) check to douse. RDC",
        "Stage1": "\u2022 Take 1 damage at the beginning of the next turn (after regen)",
        "Stage2": "\u2022 Take 2 damage at the beginning of the next turn. (after regen)",
        "Stage3": "\u2022 Take 3 damage at the beginning of the next turn. (after regen)",
        "Interrupt":{
            'Pre_Action':{
              1:'''
              
              ''',
              2:'''
              
              ''',
              3:'''
              
              '''
            }
        },
        "Payload":{
            0:'''
target.Open_Phase.pop("Bleeding")
            ''',
            1:'''
if "Bleeding" in target.Open_Phase:
  target.Open_Phase.pop("Bleeding")
target.Open_Phase.update(Bleeding = "damage(target,1)")
            ''',
            2:'''
if "Bleeding" in target.Open_Phase:
  target.Open_Phase.pop("Bleeding)")

target.Open_Phase.update(Bleeding = "damage(target,2)")
            ''',
            3:'''
target.Open_Phase.pop("Bleeding")
target.Open_Phase.update(Bleeding = "damage(target,3)")
            ''',
            4:"print('permanantly bleeding')"
        }
        #blinded can't take into account whether the target is attacking from ranged during the attack action. 
    },
    "Blinded":{
        "Type": "Physical",
        "Description":"Impaired vision\n  \u2022 Removal - Bandage(ally)/Recover(self) check RDC.",
        "Stage1": "\u2022 -2 Attack",
        "Stage2": "\u2022 -5 Attack\n  \u2022 -5 Reactions vs Ranged attacks",
        "Stage3": "\u2022 -10 Attack\n  \u2022 -10 Reactions vs Ranged attacks",
        "Interrupt":{
            "Pre_Action":{
              1:'''
if actions_dict[action]["Action_Type"] == "Attack":
  target.misc_bonus -= 2
              ''',
              2:'''
if actions_dict[action]["Action_Type"] == "Attack":
  target.misc_bonus -= 5
              ''',
              3:'''
if actions_dict[action]["Action_Type"] == "Attack":
  target.misc_bonus -= 10
              '''             
            },
            "Pre_Reaction":{
              1:None,
              2:'''
if distance(source,target) > 1:
  target.misc_bonus -= 5
              ''',
              3:'''
if distance(source,target) > 1:
  target.misc_bonus -= 10
              '''
            },
            "Post_Action":{
              1:'''
if actions_dict[action]["Action_Type"] == "Attack":
  target.misc_bonus += 2
              ''',
              2:'''
if actions_dict[action]["Action_Type"] == "Attack":
  target.misc_bonus += 5
              ''',
              3:'''
if actions_dict[action]["Action_Type"] == "Attack":
  target.misc_bonus += 10
              '''              
            },
            "Post_Reaction":{
              1:None,
              2:'''
if distance(source,target) > 1:
  target.misc_bonus -= 5
              ''',
              3:'''
if distance(source,target) > 1:
  target.misc_bonus -= 10
              '''
            }
        },
        "Payload":{
            0:'''
target.Pre_Action.pop("Blinded")
target.Post_Action.pop("Blinded")
target.Pre_Reaction.pop("Blinded")
target.Post_Reaction.pop("Blinded")
            ''',
            1:'''
if 'Blinded' in target.Pre_Action:
  target.Pre_Action.pop("Blinded")
  target.Post_Action.pop("Blinded")
  target.Pre_Reaction.pop("Blinded")
  target.Post_Reaction.pop("Blinded")

target.Pre_Action.update(Blinded = statuses_dict['Blinded']['Interrupt']['Pre_Action][1])
target.Post_Action.update(Blinded = statuses_dict['Blinded']['Interrupt']['Post_Action][1])
            ''',
            2:'''
target.Pre_Action.pop("Blinded")
target.Post_Action.pop("Blinded")
target.Pre_Reaction.pop("Blinded")
target.Post_Reaction.pop("Blinded")

target.Pre_Action.update(Blinded = statuses_dict['Blinded']['Interrupt']['Pre_Action][2])
target.Pre_Reaction.update(Blinded = statuses_dict['Blinded']['Interrupt']['Pre_Reaction][2])
target.Post_Action.update(Blinded = statuses_dict['Blinded']['Interrupt']['Post_Action][2])
target.Post_Reaction.update(Blinded = statuses_dict['Blinded']['Interrupt']['Post_Reaction][2])
            ''',
            3:'''
target.Pre_Action.pop("Blinded")
target.Post_Action.pop("Blinded")
target.Pre_Reaction.pop("Blinded")
target.Post_Reaction.pop("Blinded")

target.Pre_Action.update(Blinded = statuses_dict['Blinded']['Interrupt']['Pre_Action][3])
target.Pre_Reaction.update(Blinded = statuses_dict['Blinded']['Interrupt']['Pre_Reaction][3])
target.Post_Action.update(Blinded = statuses_dict['Blinded']['Interrupt']['Post_Action][3])
target.Post_Reaction.update(Blinded = statuses_dict['Blinded']['Interrupt']['Post_Reaction][3])
            ''',
            4:"print('Permanantly Blinded')"
        }
    },

    #burning doesn't add in any burning effect to adjacent targets
    "Burning":{
        "Type": "Situational",
        "Description":"On Fire\n  \u2022  *Flammable objects adjacent to anything Burning must roll a reaction, if applicable (RDC), or take stages of burning equal to the origin of the status - 1. \nRemoval - Auto decrease\n Improvise (self/ally) check to douse. DC determined by GM",
        "Stage1": "\u2022 Take 1 damage at the beginning of the next turn (after regen)",
        "Stage2": "\u2022 Take 2 damage at the beginning of the next turn. (after regen)",
        "Stage3": "\u2022 Take 3 damage at the beginning of the next turn. (after regen)",
         "Interrupt":{
            'Pre_Action':{
              1:'''
              
              ''',
              2:'''
              
              ''',
              3:'''
              
              '''
            }
        },
        "Payload":{
            0:'''
target.Open_Phase.pop("Burning")
            ''',
            1:'''
if "Burning" in target.Open_Phase:
  target.Open_Phase.pop("Burning")
target.Open_Phase.update(Burning = "damage(target,1)")
            ''',
            2:'''
if "Burning" in target.Open_Phase:
  target.Open_Phase.pop("Burning")

target.Open_Phase.update(Burning = "damage(target,2)")
            ''',
            3:'''
target.Open_Phase.pop("Burning")
target.Open_Phase.update(Burning = "damage(target,3)")
            ''',
            4:"print('permanantly burning')"
        }
    },

    #crippled doesn't take into account which arm and it doesn't store them aside from the number
    "Crippled":{
        "Type": "Physical",
        "Description":"Damaged Limbs\n  \u2022 Removal - Bandage(self/ally) check RDC",
        "Stage1": "ARM \u2022 -2 on all actions/reactions with arm\nLEG \u2022 -2 MP and Dodge",
        "Stage2": "ARM \u2022 -5 on all actions/reactions with arm\n\u2022 Ever attack against arm adds a Disarm action\nLEG \n\u2022Double movement Cost and -5 Dodge\n\u2022 Every attack against leg adds a Trip action",
        "Stage3": "ARM \u2022 -10 on all actions/reactions with arm\n\u2022 Ever attack against arm adds a +5 Disarm action\nLEG \n\u2022 Triple movement Cost and -10 Dodge \n\u2022 Every attack against leg adds a +5 Trip action",
         "Interrupt":{
            'Pre_Action':{
              1:'''
              
              ''',
              2:'''
              
              ''',
              3:'''
              
              '''
            }
        },
        "Payload":{
            0:'''
selection = input("Are you targeting an Arm or a Leg?")
            ''',
            1:'''
selection = input("Are you targeting an Arm or a Leg?")
if selection == "Arm":
  target.Attributes["STR"] -= 2
  target.Skills["Finesse"] -= 2
  target.Skills["Sleight"] -= 2
else:
  target.Max_MP -= 2
  target.MP -= 2
  target.Skills["Coordination"] -= 2
            ''',
            2:'''
selection = input("Are you targeting an Arm or a Leg?")
if selection == "Arm":
  target.Attributes["STR"] -= 5
  target.Skills["Finesse"] -= 5
  target.Skills["Sleight"] -= 5
else:
  target.Max_MP -= 5
  target.MP -= 5
  target.Skills["Coordination"] -= 5
            ''',
            3:'''
selection = input("Are you targeting an Arm or a Leg?")
if selection == "Arm":
  target.Attributes["STR"] -= 10
  target.Skills["Finesse"] -= 10
  target.Skills["Sleight"] -= 10
else:
  target.Max_MP = 0
  target.MP = 0
  target.Skills["Coordination"] -= 10
            ''',
            4: "print('permanantly crippled')"
        }
    },

    #deafened doesn't scale if there is any other effect that limits RP
    "Deafened":{
        "Type": "Physical",
        "Description":"Impaired hearing\n  \u2022Removal - Bandage(ally)/Recover(self) check RDC.",
        "Stage1": "\u2022 -1 RP",
        "Stage2": "\u2022 -2 RP\n  \u2022 Attacks from out of sight add a stage of Surprised.",
        "Stage3": "\u2022 -4 RPs. Cannot hear allies or enemies.\n\u2022 Attacks from out of sight add two stages of Surprised",
        "Interrupt":{
          'Pre_Reaction':{
            1:None,
            2:'''
if target.Positions['Flanked'] > 0:
  target.Statuses['Surprised'] += 1
            ''',
            3:'''
if target.Positions['Flanked'] > 0:
  target.Statuses['Surprised'] += 2
            '''
          },
          'Post_Reaction':{
            1:None,
            2:'''
if target.Positions['Flanked'] > 0:
  target.Statuses['Surprised'] -= 1            
            ''',
            3:'''
if target.Positions['Flanked'] > 0:
  target.Statuses['Surprised'] -= 2            
            '''
          }
        },
        "Payload":{
            0:'''

difference = target.Max_RP - target.RP
target.Max_RP = target.Base_RP
target.RP = target.Max_RP - difference
            ''',
            1:'''
if 'Deafened' in target.Pre_Reaction:
  target.Pre_Reaction.pop('Deafened')
  target.Post_Reaction.pop('Deafened')

difference = target.Max_RP - target.RP
target.Max_RP = target.Base_RP
target.RP = target.Max_RP - difference
target.Max_RP -= 1
target.RP -= 1

            ''',
            2:'''
if 'Deafened' in target.Pre_Reaction:            
  target.Pre_Reaction.pop('Deafened')
  target.Post_Reaction.pop('Deafened')

target.Pre_Reaction.update(Deafened = statuses_dict['Deafened']['Interrupt'][Pre_Reaction][2])
target.Post_Reaction.update(Deafened = statuses_dict['Deafened']['Interrupt'][Post_Reaction][2])


difference = target.Max_RP - target.RP
target.Max_RP = target.Base_RP
target.RP = target.Max_RP - difference
target.Max_RP -= 2
target.RP -= 2
            ''',
            3:'''
target.Pre_Reaction.pop('Deafened')
target.Post_Reaction.pop('Deafened')

target.Pre_Reaction.update(Deafened = statuses_dict['Deafened']['Interrupt'][Pre_Reaction][3])
target.Post_Reaction.update(Deafened = statuses_dict['Deafened']['Interrupt'][Post_Reaction][3])

difference = target.Max_RP - target.RP
target.Max_RP = target.Base_RP
target.RP = target.Max_RP - difference
target.Max_RP -= 3
target.RP -= 3
            ''',
            4:"print('permanently deafened')"
        }
    },

    #fatigued doesn't scale if there is anything else that is limiting AP
    "Fatigued":{
        "Type": "Physical",
        "Description":"Soreness and lack of stamina\n  \u2022 Removal - Recover (self) check RDC",
        "Stage1": "\u2022 +1 AP cost on all actions",
        "Stage2": "\u2022 +2 AP cost on all actions",
        "Stage3": "\u2022 +3 AP cost on all actions",
         "Interrupt":{
            'Pre_Action':{
              1:'''
              
              ''',
              2:'''
              
              ''',
              3:'''
              
              '''
            }
        },
        "Payload":{
            0:'''
difference = target.Max_AP - target.AP
target.Max_AP = target.Base_AP
target.AP = target.Max_AP - difference
            ''',
            1:'''

difference = target.Max_AP - target.AP
target.Max_AP = target.Base_AP
target.AP = target.Max_AP - difference
target.Max_AP -= 1
target.AP -= 1

            ''',
            2:'''
difference = target.Max_AP - target.AP
target.Max_AP = target.Base_AP
target.AP = target.Max_AP - difference
target.Max_AP -= 2
target.AP -= 2

            ''',
            3:'''
difference = target.Max_AP - target.AP
target.Max_AP = target.Base_AP
target.AP = target.Max_AP - difference
target.Max_AP -= 3
target.AP -= 3

            ''',
            4:"print('permanently fatigued')"
        }
    },

    # I need to make a way to separate arms and legs
    "Impaled":{
        "Type": "Situational",
        "Description":"Lodged fragments or shrapnel in body\n  \u2022 Removal - Bandage(self/ally) check RDC\n    \u2022 Failed Bandage Check Adds a stage of Bleeding or Crippled",
        "Stage1": "\u2022 Take 1 damage for every 2 actions of the impaled limb",
        "Stage2": "\u2022 Take 1 damage for every action of the impaled limb",
        "Stage3": "\u2022 Take 2 damage for every action of the impaled limb",
         "Interrupt":{
            'Post_Action':{
              1:'''
target_finesse = roll(target,target.crit_threshold,target.crit_fail_threshold) + target.Skills['Finesse'] + target.Attributes['DEX']

if target_finesse < 11:
  print('You suffer from your impaled limb and take 1 damage')
  damage(target)
else:
  print("You manage to move through your impaled limb with your finesse.\nYou don't take any damage... This time")
              ''',
              2:'''
if actions_dict[action]['Stat'] == 'STR' or 'DEX' or 'CON':
  damage(target)
              ''',
              3:'''
if actions_dict[action]['Stat'] == 'STR' or 'DEX' or 'CON':
  damage(target,2)              
              '''
            }
        },
        "Payload":{
            0:'''
target.Post_Action.pop('Impaled')
            ''',
            1:'''
if 'Impaled' in target.Post_Action:
  target.Post_Action.pop('Impaled')

target.Post_Action.update(Impaled = statuses_dict['Impaled']['Interrupt'][1])
            ''',
            2:'''
target.Post_Action.pop('Impaled')

target.Post_Action.update(Impaled = statuses_dict['Impaled']['Interrupt'][2])
            ''',
            3:'''
target.Post_Action.pop('Impaled')

target.Post_Action.update(Impaled = statuses_dict['Impaled']['Interrupt'][3])
            '''
        }
    },

    # Ready to test
    "Captivated":{
        "Type": "Mental",
        "Description":"Antagonized or focussed on a specific enemy\n  \u2022 Removal - Focus (self)/Encourage (ally) check RDC",
        "Stage1": "\u2022 +1 AP on all actions and movement not directed to the source of the status",
        "Stage2": "\u2022 +2 AP on all actions and movement not directed to the source of the status",
        "Stage3": "\u2022 +3 AP on all actions and movement not directed to the source of the status",
         "Interrupt":{
            'Post_Action':{
              1:'''
if not target_name in source.Captivated_Source:
  source.AP -= 1              
              ''',
              2:'''
if not target_name in source.Captivated_Source:
  source.AP -= 2              
              ''',
              3:'''
if not target_name in source.Captivated_Source:
  source.AP -= 3              
              '''
            }
        },
        "Payload":{
            0:'''
target.Captivated_Source.pop(source_name)
            ''',
            1:'''
if source_name in target.Captivated_Source:
  target.Captivated_Source.pop(source_name)

target.Captivated_Source.update(source_name = 1)

            ''',
            2:'''
target.Captivated_Source.pop(source_name)

target.Captivated_Source.update(source_name = 2)
            ''',
            3:'''
target.Captivated_Source.pop(source_name)

target.Captivated_Source.update(source_name = 3)
            '''
        }
    },

    # I need to add functionality to reset the crit fail threshold after a crit fail. 
    "Confused":{
        "Type": "Mental",
        "Description":"Lack of clear thinking or blurred understanding.\n  \u2022 Removal - Focus (self)/Encourage (ally) check RDC",
        "Stage1": "\u2022 Crit Fail threshold raises by 1 each turn\n\u2022 Resets on Crit Fail",
        "Stage2": "\u2022 Crit Fail threshold raises by 2 each turn\n\u2022 Resets on Crit Fail",
        "Stage3": "\u2022 Crit Fail threshold raises by 3 each turn\n\u2022 Resets on Crit Fail",
         "Interrupt":{
            'Post_Roll':{
              1:'''
if source_roll == 'Critical Fail':
  source.crit_fail_threshold = 1              
              ''',
              2:'''
if source_roll == 'Critical Fail':
  source.crit_fail_threshold = 1              
              ''',
              3:'''
if source_roll == 'Critical Fail':
  source.crit_fail_threshold = 1              
              '''
            }
        },
        "Payload":{
            0:'''
target.Open_Phase.pop("Confused")
            ''',
            1:'''
if "Confused" in target.Open_Phase:
  target.Open_Phase.pop("Confused")
target.Open_Phase.update(Confused = "target.crit_fail_threshold += 1")
            ''',
            2:'''
target.Open_Phase.pop("Confused")

target.Open_Phase.update(Confused = "target.crit_fail_threshold += 2")
            ''',
            3:'''
target.Open_Phase.pop("Confused")

target.Open_Phase.update(Confused = "target.crit_fail_threshold += 3")
            '''
        }
    },

    # Ready to test
    "Frightened":{
        "Type": "Mental",
        "Description":"Antagonized or focussed on a specific enemy\n  \u2022 Removal - Focus (self)/Encourage (ally) check RDC",
        "Stage1": "\u2022 +1 AP on all actions and movement directed to the source of the status",
        "Stage2": "\u2022 +2 AP on all actions and movement directed to the source of the status",
        "Stage3": "\u2022 +3 AP on all actions and movement directed to the source of the status",
         "Interrupt":{
            'Post_Action':{
              1:'''
if target_name in source.Frightened_Source:
  source.AP -= 1              
              ''',
              2:'''
if target_name in source.Frightened_Source:
  source.AP -= 2              
              ''',
              3:'''
if target_name in source.Frightened_Source:
  source.AP -= 3              
              '''
            }
        },
        "Payload":{
            0:'''
target.Frightened_Source.pop(source_name)
            ''',
            1:'''
if source_name in target.Frightened_Source:
  target.Frightened_Source.pop(source_name)

target.Frightened_Source.update(source_name = 1)

            ''',
            2:'''
target.Frightened_Source.pop(source_name)

target.Frightened_Source.update(source_name = 2)
            ''',
            3:'''
target.Frightened_Source.pop(source_name)

target.Frightened_Source.update(source_name = 3)
            '''
        }
    },

    # I need to store the initiative order change
    "Stunned":{
        "Type": "Mental",
        "Description":"A state of inaction or delayed mental composure\n*If initiative position is knocked below the bottom of the round, you lose a turn but gain the first initiative position the next round.*\n\u2022 Removal - Focus (self)/Encourage (ally) check RDC",
        "Stage1": "\u2022 Move back 1 position in the initiative order",
        "Stage2": "\u2022 Move back 3 position in the initiative order",
        "Stage3": "\u2022 Move back 5 position in the initiative order\n\u2022 Gain 1 stage of Prone.",
         "Interrupt":{
            'Pre_Action':{
              1:'''
              
              ''',
              2:'''
              
              ''',
              3:'''
              
              '''
            }
        },
        "Payload":{
            0:"",
            1:"print('1')",
            2:"print('2')",
            3:"print('3')"
        }
    },

    # I need to create an instance of the armor on the character to keep track of durability
    # I also need to keep track of consecutive movement and such
    "Momentum":{
        "Type": "Situational",
        "Description":"Additional force added to attacks\n  \u2022 adds Impact equation\n\u2022 * Gain stages through Positioning and/or charging at enemies in a straight line. \n\u2022 Stage 1= 5 consecutive yards \n\u2022 Stage 2 = 10 consecutive yards \n\u2022 Stage 3 = 20 consecutive yards",
        "Stage1": "\u2022 -1 Crit threshold in the momentum direction\n\u2022 On hit, target Armor -2 Durability",
        "Stage2": "\u2022 -2 Crit threshold in the momentum direction\n\u2022 On hit, target Armor -3 Durability",
        "Stage3": "\u2022 -3 Crit threshold in the momentum direction\n\u2022 On hit, target Armor -5 Durability",
         "Interrupt":{
            'Pre_Action':{
              1:'''
if target.Location == melee_coordinates(source):
  source.crit_threshold -= 1
              ''',
              2:'''
if target.Location == melee_coordinates(source):
  source.crit_threshold -= 2              
              ''',
              3:'''
if target.Location == melee_coordinates(source):
  source.crit_threshold -= 3              
              '''
            }
            },
            "Post_Action":{
                1:'''
if target.Location == melee_coordinates(source):
  if action == 'Weapon Attack':
    weapon = source.Equipment['Main Hand']
    impact(source,target,weapons_dict[weapon]['Type'],'Bludgeoning',False)
source.crit_threshold += 1
              ''',
              2:'''
if target.Location == melee_coordinates(source):
  if action == 'Weapon Attack':
    weapon = source.Equipment['Main Hand']
    impact(source,target,weapons_dict[weapon]['Type'],'Bludgeoning',False)
source.crit_threshold += 2    
              ''',
              3:'''
if target.Location == melee_coordinates(source):
  if action == 'Weapon Attack':
    weapon = source.Equipment['Main Hand']
    impact(source,target,weapons_dict[weapon]['Type'],'Bludgeoning',False)
source.crit_threshold += 3
              '''
        },
        "Payload":{
            0:'''
target.Pre_Action.pop('Momentum')
target.Post_Action.pop('Momentum')            
            ''',
            1:'''
if 'Momentum' in target.Pre_Action:
  target.Pre_Action.pop('Momentum')
  target.Post_Action.pop('Momentum')

target.Pre_Action.update(Momentum = statuses_dict['Momentum']['Interrupt']['Pre_Action'][1])
target.Post_Action.update(Momentum = statuses_dict['Momentum']['Interrupt']['Pre_Action'][1])

            ''',
            2:'''
target.Pre_Action.pop('Momentum')
target.Post_Action.pop('Momentum')

target.Pre_Action.update(Momentum = statuses_dict['Momentum']['Interrupt']['Pre_Action'][1])
target.Post_Action.update(Momentum = statuses_dict['Momentum']['Interrupt']['Pre_Action'][1])

            ''',
            3:'''
target.Pre_Action.pop('Momentum')
target.Post_Action.pop('Momentum')

target.Pre_Action.update(Momentum = statuses_dict['Momentum']['Interrupt']['Pre_Action'][1])
target.Post_Action.update(Momentum = statuses_dict['Momentum']['Interrupt']['Pre_Action'][1])

            '''
        }
    },

    # I need to program out a way to have the removing functions and things so that movement can get rid of this. I might even have to make payloads for removal and put them on the character class
    "Prone":{
        "Type": "Situational",
        "Description":"Degrees of being knocked down or not in a readied combat stance\n\u2022 Removal - using AP to stand. 2 AP per stage",
        "Stage1": "\u2022 -2 on reactions",
        "Stage2": "\u2022 -5 on reactions",
        "Stage3": "\u2022 -10 on reactions",
         "Interrupt":{
            'Pre_Action':{
              1:'''
              
              ''',
              2:'''
              
              ''',
              3:'''
              
              '''
            }
        },
        "Payload":{
            0:"",
            1:"print('1')",
            2:"print('2')",
            3:"print('3')"
        }
    },

    # I need to create the way to remove this, also, maybe change the 
    "Restrained":{
        "Type": "Situational",
        "Description":"Limbs or body that are unable to move freely or are bound by an external force\n\u2022 Removal - Contest your Muscle check against their Grapple check to break free.\n  \u2022 Muscle check is made with a -5 per stage",
        "Stage1": "\u2022 Any restrained limb is considered Crippled 1",
        "Stage2": "\u2022 Any restrained limb is considered Crippled 2",
        "Stage3": "\u2022 Any restrained limb is considered Crippled 3",
         "Interrupt":{
            'Pre_Action':{
              1:'''
              
              ''',
              2:'''
              
              ''',
              3:'''
              
              '''
            }
        },
        "Payload":{
            0:"",
            1:"print('1')",
            2:"print('2')",
            3:"print('3')"
        }
    },

    #add removal and death mechanic when mod reaches -3
    "Suffocating":{
        "Type": "Situational",
        "Description":"Restricted breathing\n *When CON Mod reaches -3 target is Unconscious\n\u2022 Removal - Contest your Muscle check against their Choke check to break free.\n  \u2022 Muscle check is made with a -5 per stage",
        "Stage1": "\u2022 -1 CON Mod per turn",
        "Stage2": "\u2022 -3 CON Mod per turn",
        "Stage3": "\u2022 -5 CON Mod per turn",
         "Interrupt":{
            'Open_Phase':{
              1:'''
drain(target,'CON',5)            
              ''',
              2:'''
drain(target,'CON',10)                 
              ''',
              3:'''
drain(target,'CON',15)                 
              '''
            }
        },
        "Payload":{
            0:'''
target.Open_Phase.pop('Suffocating')            
            ''',
            1:'''
if 'Suffocating' in target.Open_Phase:
  target.Open_Phase.pop('Suffocating')

target.Open_Phase.update(Suffocating = statuses_dict['Suffocating']['Interrupt']['Open_Phase'][1])
            ''',
            2:'''
target.Open_Phase.pop('Suffocating')

target.Open_Phase.update(Suffocating = statuses_dict['Suffocating']['Interrupt']['Open_Phase'][2])
            ''',
            3:'''
target.Open_Phase.pop('Suffocating')

target.Open_Phase.update(Suffocating = statuses_dict['Suffocating']['Interrupt']['Open_Phase'][3])
            '''
        }
    },

    #add removal on attack, and interrupt for roll equation
    "Surprised":{
        "Type": "Situational",
        "Description":"Unaware or unprepared for an attack \n\u2022 Removal - CAll stages lost after the the target is aware of the source of the status",
        "Stage1": "\u2022 Replace the reaction roll with a d20 + Dodge/Defend Respectively",
        "Stage2": "\u2022 Replace the reaction roll with a d20",
        "Stage3": "\u2022 Replace the reaction roll with a d20\n \u2022 Crit fails count as vital 2",
         "Interrupt":{
            'Pre_Action':{
              1:'''
              
              ''',
              2:'''
              
              ''',
              3:'''
              
              '''
            }
        },
        "Payload":{
            0:"",
            1:"print('1')",
            2:"print('2')",
            3:"print('3')"
        }
    }
  }