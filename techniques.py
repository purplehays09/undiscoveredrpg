
techniques_dict = {
   "Name":{
      "Info":"String",
      1:{
          "Description":"String",
          "Payload":'''

         '''
      },
      2:{
          "Description":"String",
          "Payload":'''

         '''
      },
      3:{
          "Description":"String",
          "Payload":'''

         '''
      }
    },
    "Cleave":{
      "Info":"String",
      1:{
          "Description":"You can attempt to hit 2 targets. Both will roll reactions against the same attack roll",
          "Payload":'''

target2 = input("What second target do you want to attack")
target2 = make_class(target2)
if distance(source,target2) != 1:
  while distance(source,target2) != 1:
    target2 = input(This target is too far away, please select another target)

reaction2 = input(target2.Name + ", how do you react?")

result = attack(source,"Weapon Attack",target2,reaction)

if result == "Critical":
  damage(target2,weapons_dict[weapon]["Crit_Damage"])
elif result == "Fail":
  print("Sorry you Suck")
elif result == 'Critical Fail':
  print("You really suck bad")
else:
  exec(actions_dict[action]["Payload"])


         '''
      },
      2:{
          "Description":"You can attempt to hit up to 3 targets. All targets will roll reactions against the same attack roll.",
          "Payload":'''
targets = []

while len(targets) < 2:
  confirmation = input("Do you want to attack another target?")
  if confirmation == 'yes':
    new_target = input("Who would you like to target?)
    
    if distance(source,new_target) != 1:
      while distance(source,new_target) != 1:
        new_target = input(This target is too far away, please select another target)
    targets.append(new_target)

for i in targets:
  new_target = make_class(targets.pop(0))
  new_reaction = input(new_target + ", how do you react?")

  result = attack(source,"Weapon Attack",new_target,new_reaction)

  if result == "Critical":
    damage(target2,weapons_dict[weapon]["Crit_Damage"])
  elif result == "Fail":
    print("Sorry you Suck")
  elif result == 'Critical Fail':
    print("You really suck bad")
  else:
    exec(actions_dict[action]["Payload"])
         '''
      },
      3:{
          "Description":"You can attempt to hit 5 targets. All targets will roll reactions against the same attack roll. Crits will sever any limb hit on the first target",
          "Payload":'''
targets = []

while len(targets) < 4:
  confirmation = input("Do you want to attack another target?")
  if confirmation == 'yes':
    new_target = input("Who would you like to target?)
    
    if distance(source,new_target) != 1:
      while distance(source,new_target) != 1:
        new_target = input(This target is too far away, please select another target)
    targets.append(new_target)

for i in targets:
  new_target = make_class(targets.pop(0))
  new_reaction = input(new_target + ", how do you react?")

  result = attack(source,"Weapon Attack",new_target,new_reaction)

  if result == "Critical":
    damage(target2,weapons_dict[weapon]["Crit_Damage"])
  elif result == "Fail":
    print("Sorry you Suck")
  elif result == 'Critical Fail':
    print("You really suck bad")
  else:
    exec(actions_dict[action]["Payload"])
         '''
      }
    },
    "Concussion":{
      "Info":"String",
      1:{
          "Description":"String",
          "Payload":'''

         '''
      },
      2:{
          "Description":"String",
          "Payload":'''

         '''
      },
      3:{
          "Description":"String",
          "Payload":'''

         '''
      }
    },
    "Crush":{
      "Info":"String",
      1:{
          "Description":"Successful attacks will also add 1 stage of Crippled to the target",
          "Payload":'''
status(target,"Crippled",1)
         '''
      },
      2:{
          "Description":"Successful attacks will also add 2 stages of Crippled to the target",
          "Payload":'''
status(target,"Crippled",2)
         '''
      },
      3:{
          "Description":"Successful attacks will also add 3 stages of Crippled to the target",
          "Payload":'''
status(target,"Crippled",3)
         '''
      }
    },
    "Distance":{
      "Info":"String",
      1:{
          "Description":"You can choose take a -5 to hit to double your range",
          "Pre_Action":'''
source.misc_bonus -= 5
source.Equipment["Main Hand"]["Range"] *= 2
          ''',
          "Post_Action":'''
source.misc_bonus += 5
source.Equipment["Main Hand"]["Range"] /= 2
          ''',
          "Payload":'''
source.Pre_Action.update(Distance = techniques_dict["Distance"][1]["Pre_Action"])
source.Post_Action.update(Distance = techniques_dict["Distance"][1]["Post_Action"])
         '''
      },
      2:{
          "Description":"You can choose take a -2 to hit to double your range, or take a -5 to hit to triple your range",
          "Pre_Action":'''
source.misc_bonus -= 5
source.Equipment["Main Hand"]["Range"] *= 3
          ''',
          "Post_Action":'''
source.misc_bonus += 5
source.Equipment["Main Hand"]["Range"] /= 3
          ''',
          "Payload":'''
source.Pre_Action.update(Distance = techniques_dict["Distance"][2]["Pre_Action"])
source.Post_Action.update(Distance = techniques_dict["Distance"][2]["Post_Action"])
         '''
      },
      3:{
          "Description":"You can double your range or you can choose take a -2 to hit to triple your range",
          "Pre_Action":'''
source.misc_bonus -= 2
source.Equipment["Main Hand"]["Range"] *= 3
          ''',
          "Post_Action":'''
source.misc_bonus += 2
source.Equipment["Main Hand"]["Range"] /= 3
          ''',
          "Payload":'''
source.Pre_Action.update(Distance = techniques_dict["Distance"][3]["Pre_Action"])
source.Post_Action.update(Distance = techniques_dict["Distance"][3]["Post_Action"])
         '''
      }
    },
    "Flurry":{
      "Info":"String",
      1:{
          "Description":"Consecutive attacks in the same turn cost -1 AP after the first",
          "Payload":'''
weapon = source.Equipment["Main Hand"]
source.AP -= (weapons_dict[weapon]["AP"] - 1)

reaction2 = input(target.Name + ", how do you react?")

result = attack(source,"Weapon Attack",target,new_reaction)

if result == "Critical":
  damage(target2,weapons_dict[weapon]["Crit_Damage"])
elif result == "Fail":
  print("Sorry you Suck")
elif result == 'Critical Fail':
  print("You really suck bad")
else:
  exec(actions_dict[action]["Payload"])
         '''
      },
      2:{
          "Description":"Consecutive attacks in the same turn cost -2 AP after the first",
          "Payload":'''
weapon = source.Equipment["Main Hand"]
source.AP -= (weapons_dict[weapon]["AP"] - 2)

reaction2 = input(target.Name + ", how do you react?")

result = attack(source,"Weapon Attack",target,new_reaction)

if result == "Critical":
  damage(target2,weapons_dict[weapon]["Crit_Damage"])
elif result == "Fail":
  print("Sorry you Suck")
elif result == 'Critical Fail':
  print("You really suck bad")
else:
  exec(actions_dict[action]["Payload"])
         '''
      },
      3:{
          "Description":"Consecutive attacks in the same turn cost -3 AP after the first",
          "Payload":'''
weapon = source.Equipment["Main Hand"]
source.AP -= (weapons_dict[weapon]["AP"] - 3)

reaction2 = input(target.Name + ", how do you react?")

result = attack(source,"Weapon Attack",target,new_reaction)

if result == "Critical":
  damage(target2,weapons_dict[weapon]["Crit_Damage"])
elif result == "Fail":
  print("Sorry you Suck")
elif result == 'Critical Fail':
  print("You really suck bad")
else:
  exec(actions_dict[action]["Payload"])
         '''
      }
    },
    "Impact":{
      "Info":"String",
      1:{
          "Description":"Each attack adds a 1 stage of Momentum",
          "Payload":'''
status(source,"Momentum",1)
         '''
      },
      2:{
          "Description":"Each attack adds a 2 stages of Momentum",
          "Payload":'''
status(source,"Momentum",2)
         '''
      },
      3:{
          "Description":"Each attack adds a 3 stages of Momentum",
          "Payload":'''
status(source,"Momentum",3)
         '''
      }
    },
    "Pin Point":{
      "Info":"String",
      1:{
          "Description":"String",
          "Pre_Action":'''
bonus = roll_dice(1,6,0,21)
source.temp_bonus += bonus
          ''',
          "Post_Action":'''

          ''',
          "Payload":'''
source.Pre_Action.update("Pin Point" = techniques_dict["Pin Point"][1]["Pre_Action"])
         '''
      },
      2:{
          "Description":"String",
          "Pre_Action":'''
bonus = roll_dice(1,10,0,21)
source.temp_bonus += bonus
          ''',
          "Post_Action":'''

          ''',
          "Payload":'''
source.Pre_Action.update("Pin Point" = techniques_dict["Pin Point"][2]["Pre_Action"])
         '''
      },
      3:{
          "Description":"String",
          "Pre_Action":'''
bonus = roll_dice(1,20,0,21)
source.temp_bonus += bonus
          ''',
          "Post_Action":'''

          ''',
          "Payload":'''
source.Pre_Action.update("Pin Point" = techniques_dict["Pin Point"][3]["Pre_Action"])
         '''
      }
    },
    "Rend":{
      "Info":"String",
      1:{
          "Description":"Each attack adds 1 stage of Bleeding",
          "Payload":'''
status(target,"Bleeding",1)
         '''
      },
      2:{
          "Description":"Each attack adds 2 stages of Bleeding",
          "Payload":'''
status(target,"Bleeding",2)
         '''
      },
      3:{
          "Description":"Each attack adds 3 stages of Bleeding",
          "Payload":'''
status(target,"Bleeding",3)
         '''
      }
    },  
}
