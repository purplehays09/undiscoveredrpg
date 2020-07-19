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
            "Payload": "print('It is the name action')"
        },
    "Move": {
        "Type": "Movement",
        "Description": "You know... just like move to where you aren't. Pretty much 1 MP per yard.",
        "Payload": '''
move(source)
        '''
        },
    "Weapon Attack":{
            "Type": "Action",
            "Stat": "STR",
            "Skill": "Muscle",
            "Speed": "~",
            "Range": "~",
            "Description": "\u2022Standard attacks vary by weapon and spell. See your attacks for information.\n\u2022You can choose to replace your Muscle mod with a -2 Finesse mod\n\u2022If the weapon has a Balance tag, you can ignore the -2 penalty to your Finesse mod",
            "Dice_Roll": "d20",
            "Action_Type": "Attack",
            "Reaction": "Standard_Reactions",
            "Payload": '''
if source.Attack_Options["Base"] == "Damage":
      damage(target,amount)
    else:
      status(target,source.Attack_Options["Base"],amount)
    for k,v in source.Attack_Options["Technique"]:
      if k != "Distance" or "Pin Point":
        print("You used: " + k)
        exec(techniques_dict[k][v]["Payload"])
      else:
        print("You used: " + k)
            '''
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
            "Payload": '''
target_equipment = target.Equipment
print(target_name + " has the following equipped")
for item in target_equipment:
  print(item + " holds: " + str(target_equipment[item]))
weapon_select = input("What hand would you want to select?")
print("You forcibly remove " + target_name + "'s " + target_equipment[weapon_select] + " from their " + weapon_select + " and it falls to the ground")
target_equipment[weapon_select] = None
            
            '''
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
            "Payload": '''
# item = input("What are you throwing?")
# purpose = input("Are you trying to: Attack, Pass, or Hurl)
# if purpose == "Attack":
#   target = input("Who are you trying to attack?")
#   special_attack(source,target,)
print('Throw isnt done yet. GM, go ahead and fill in the blanks')
            '''
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
            "Payload": '''
status(target,'Suffocating',1)
print(target_name + "'s suffocating stage is now: " + str(target.Statuses["Suffocating"]))
            '''
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
            "Payload": '''
status(target,'Restrained',1)
print(target_name + "'s restrained stage is now: " + str(target.Statuses["Restrained"]))
            '''
        },
    "Strike":{
            "Type": "Action",
            "Stat": "STR",
            "Skill": "Brawl",
            "Speed": 1,
            "Range": "1",
            "Description": "\u2022Make a Strike check against a target\u2019s choice of reaction. On a hit, the target takes a stage of Stunned for every 2 hits they have taken during your turn (Attack, special move, or another Strike).",
            "Dice_Roll": "d20",
            "Action_Type": "Attack",
            "Reaction": "Standard_Reactions",
            "Payload": '''
status(target,'Stunned',1)
print(target_name + "'s stunned stage is now: " + str(target.Statuses["Stunned"]))
            '''
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
            "Payload": '''
status(target,'Prone',1)
print(target_name + "'s prone stage is now: " + str(target.Statuses["Prone"]))
            '''
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
            "Payload": "print('Tackle isnt done yet. GM, go ahead and fill in the blanks')"
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
            "Payload": '''


direction = input("Are you leaping horizontal or vertical?")
if direction == 'horizontal':
  amount = result // 5
  target.MP += result // 5
  print("Your horizontal range is : " + str(amount))

else:
  amount = result // 10
  target.MP += 10
  print("Your vertical range is : " + str(amount))

move(source)
            '''
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
            "Payload": '''
amount = result // 10
status(target,'Momentum',amount)
print(target_name + "'s momentum stage is now: " + str(target.Statuses["Momentum"]))
            
            '''
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
            "Payload": "print('Climb isnt done yet. GM, go ahead and fill in the blanks')"
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
            "Payload": "print('Dive isnt done yet. GM, go ahead and fill in the blanks')"
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
            "Payload": "print('Parry isnt done yet. GM, go ahead and fill in the blanks')"
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
            "Payload": "print('Riposte isnt done yet. GM, go ahead and fill in the blanks')"
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
            "Payload": "print('Feint isnt done yet. GM, go ahead and fill in the blanks')"
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
            "Payload": '''
source = str(source)
source_name = eval(source).Name
print(target_name + " has the following on them:")
for i in eval(target_name).Backpack:
  print(i)
purpose = input("Which would you like to take?")

eval(target_name + ".Backpack.remove(purpose)")
eval(source_name + ".Backpack.append(purpose)")
print(source_name + ", you now have the " + purpose + " in your backpack")
            '''
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
            "Payload": '''
status(source,'Prone',1)
print(source_name + "'s prone stage is now: " + str(source.Statuses["Prone"]))
            '''
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
            "Payload": '''
eval(target_name).Positions['Hidden'] += 1
print(target_name + "'s hidden stage is now: " + str(eval(target_name).Positions["Hidden"]))
            '''
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
            "Payload": '''
target.RP += result // 5
print(target_name + "'s RP is now: " + str(target.RP))
            '''
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
        "Payload": '''
eval(target_name).Power_Rank += 1
print(target_name + "'s power tier stage is now: " + str(target.Power_Rank))
            '''
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
            "Payload": '''

purpose = input("What mental status do you want to heal?")
current_stage = target.Statuses[purpose]
status(target,purpose,-current_stage)
print(target_name + ", your " + purpose + " is now: " + str(target).Statuses[purpose]))
            '''
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
            "Payload": '''
print('GM, go ahead and tell raise the lowest dice roll value to: ' + str(result // 2))
'''
        },
    "Recover":{
            "Type": "Action",
            "Stat": "CON",
            "Skill": "Vitality",
            "Speed": "0",
            "Range": "2",
            "Description": "\u2022Roll a Recover Check to regain a damaged health block. DC = 8 + 1 per Debuff status currently affecting you AND Missing Health Block",
            "Dice_Roll": "d20",
            "Action_Type": "Range",
            "Reaction": "",
            "Payload": '''
target_stamina = eval(target_name).Stamina
target_health = eval(target_name + "." + target_stamina)
print("You currenlty have : " + str(target_health) + " HP")
target_health += result // 10

print("Your " + target_stamina + " stamina now has: " + str(target_health) + " HP")
            '''
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
            "Payload": "print('GM, go ahead and tell them what know about the NPC')"
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
            "Payload": "print('GM, go ahead and tell them what they know about the magic')"
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
            "Payload": '''
if target.visibility["Tactics_1"] and target.visibility["Tactics_2"] and target.visibility["Tactics_3"] == False :
  target.visibility["Tactics_1"] = True
  print(target_name + "'s Tactics 1 is: " + target.Tactics[1])
elif target.visibility["Tactics_3"] and target.visibility["Tactics_2"] == False:
  target.visibility["Tactics_2"] = True
  print(target_name + "'s Tactics 1 is: " + target.Tactics[1])
  print(target_name + "'s Tactics 2 is: " + target.Tactics[2])
elif target.visibility["Tactics_3"] == False:
  target.visibility["Tactics_3"] = True
  print(target_name + "'s Tactics 1 is: " + target.Tactics[1])
  print(target_name + "'s Tactics 2 is: " + target.Tactics[2])
  print(target_name + "'s Tactics 3 is: " + target.Tactics[3])
  '''
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
            "Payload": "print('GM, go ahead and tell them what they found')"
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
            "Payload": "print('GM, go ahead and tell the player the positions on the field')"
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
            "Payload": '''
target.visibility["Max_HP"] = True
print(target_name + "'s max HP is: " + str(target.Max_HP))
            '''
        },
    "Coordinated Attack":{
            "Type": "Action",
            "Stat": "WIS",
            "Skill": "Interaction",
            "Speed": "6",
            "Range": "12",
            "Description": "\u2022Roll a Coordinated Attack check to invite an ally within range to perform actions (with you) in succession. \n\u2022You and your ally spend their 12 AP for the round to share a single turn and with a total combined AP for both of you equal to your Coordinated Attack check\n\u2022You are limited to movement and one action each.",
            "Dice_Roll": "d20",
            "Action_Type": "Attack",
            "Reaction": "",
            "Payload": "print('Coordinated Attack isnt done yet. GM, go ahead and fill in the blanks')"
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
            "Payload": "print('Improvise isnt done yet. GM, go ahead and fill in the blanks')"
        },
        #this one needs to fix the last else now that there is a set function for reducing and increasing statuses
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
            "Payload": '''
target_name = input("Who would you like to bandage?")
target_stamina = eval(target_name).Stamina
target_health = eval(target_name + "." + target_stamina)

print(target_name + " is currently in their " + target_stamina + " stamina which currenlty has : " + str(target_health) + " HP")

purpose = input("Would you like to give them health or type the status you'd like to Bandage.")
if purpose == "health":
  target_health += 1
  print(target_name + "'s " + target_stamina + " stamina now has: " + str(target_health) + " HP")
else:
  status = eval(purpose)
  eval(target_name).status = 1
  print(target_name + "'s " + purpose + " is now at stage: " + str(eval(target_name).status))
            '''
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
            "Payload": '''
target.temp_bonus += result // 4
print("Your following attack with have a bonus of: " + str(target.temp_bonus))
            '''
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
            "Payload": '''
if target.visibility["Vitals_1"] and target.visibility["Vitals_2"] and target.visibility["Vitals_3"] == False :
  target.visibility["Vitals_1"] = True
  print(target_name + "'s vital 1 is: " + target.Vitals_1)
elif target.visibility["Vitals_3"] and target.visibility["Vitals_2"] == False:
  target.visibility["Vitals_2"] = True
  print(target_name + "'s vital 1 is: " + target.Vitals_1)
  print(target_name + "'s vital 2 is: " + target.Vitals_2)
elif target.visibility["Vitals_3"] == False:
  target.visibility["Vitals_3"] = True
  print(target_name + "'s vital 1 is: " + target.Vitals_1)
  print(target_name + "'s vital 2 is: " + target.Vitals_2)
  print(target_name + "'s vital 3 is: " + target.Vitals_3)
            '''
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
            "Payload": '''
preference = input("Are you trying to frighten or captivate the target?")
if preference == "frighten":
  status(target,'Frightened',1)
  print(target_name + "'s Frightened status is now: " + str(target.Statuses["Frightened"]))
else:
  status(target,'Captivated',1)
  print(target_name + "'s Captivated status is now: " + str(target.Statuses["Captivated"]))
            '''
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
            "Payload": '''
target.Positions['Flanked'] += 1
print(target_name + "'s flanked stage is now: " + str(target.Positions["Flanked"]))
            '''
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
            "Payload": '''
target.Hostility = False
print(target_name + "'s is no longer hostile.")
            '''
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
            "Payload": '''
target_name = input("Who do you wish to encourage?")
eval(target_name).Statuses[Captivated] = 0
eval(target_name).Statuses[Confused] = 0
eval(target_name).Statuses[Frightened] = 0
eval(target_name).Statuses[Stunned] = 0
print(target_name + "'s mental statuses are cleared")
            '''
        }
  }