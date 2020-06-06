var actions_dict = {
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
            "Speed": "0",
            "Range": "~",
            "Description": "LOWER YOUR AP MANUALLY \n\u2022Weapon attacks vary by weapon. See your weapon for information.\n\u2022You can choose to replace your Muscle mod with a -2 Finesse mod\n\u2022If the weapon has a Balance tag, you can ignore the -2 penalty to your Finesse mod",
            "Dice_Roll": "d20",
            "Action_Type": "Special",
            "Reaction": "Standard_Reactions",
            "Payload": "Store in weapon"
        },
    "Disarm":{
            "Type": "Action",
            "Stat": "STR",
            "Skill": "Muscle",
            "Speed": "2",
            "Range": "1",
            "Description": "\u2022Grab an object held by a target and attempt to pull it away. Make a Disarm contest against the target\u2019s +8 Muscle Check.  On a success, the target is disarmed of the item. \n\u2022Attempting to Disarm a weapon gives the target an opportunity attack against you on a fail.\n\u2022Each Debuff status affecting the target\u2019s arm gives them an additional -3 toward the check. ",
            "Dice_Roll": "d20",
            "Action_Type": "Special",
            "Reaction": "Muscle",
            "Payload": "target_selected_equipment = None"
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
            "Reaction": "Muscle || Finesse",
            "Payload": ""
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
            "Reaction": "Muscle",
            "Payload": "target_suffocating_status_stage += 1"
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
            "Reaction": "Muscle",
            "Payload": "target_restrained_status_stage +=1"
        },
    "Strike":{
            "Type": "Action",
            "Stat": "STR",
            "Skill": "Brawl",
            "Speed": "1",
            "Range": "1",
            "Description": "\u2022Make a Strike check against a target\u2019s choice of reaction. On a hit, the target takes a stage of Stunned for every 2 hits they have taken during your turn (Attack, special move, or another Strike).",
            "Dice_Roll": "d20",
            "Action_Type": "Contest",
            "Reaction": "Standard_Reactions",
            "Payload": "target_stunned_status_stage +=1"
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
            "Payload": "target_prone_status_stage +=1"
        },
    "Tackle":{
            "Type": "Movement",
            "Stat": "STR",
            "Skill": "Brawl",
            "Speed": "3",
            "Range": "1",
            "Description": "\u2022Make a Tackle check contested against the target\u2019s Muscle check. On a success the target takes a stage of Prone and Grappled. You also take a stage of Prone\n\u2022 You can use MP instead of AP if you desire",
            "Dice_Roll": "d20",
            "Action_Type": "Contest",
            "Reaction": "Muscle",
            "Payload": "target_prone_status_stage +=1\ntarget_restrained_status_stage +=1\nsource_prone_status_stage +=1\nsource_restrained_status_stage +=1"
        },
    "Leap":{
            "Type": "Movement",
            "Stat": "STR",
            "Skill": "Jump",
            "Speed": "1",
            "Range": "Jump",
            "Description": "\u2022Declare a distance you want to Leap. Make a Leap check and add your Momentum stages if applicable. \n\u2022Your horizontal range = (Leap check/5) + Momentum Stage \n\u2022Your vertical range =  (Leap check/10) + Momentum Stage\n\u2022If the declared distance is less than the range, you must succeed in a Coordination Check or take a stage of Prone \n\u2022DC = Range * 5\n\u2022You can choose to replace your Jump mod with a -2 Coordination mod\n\u2022 You can use MP instead of AP if you desire",
            "Dice_Roll": "d20",
            "Action_Type": "Roll",
            "Reaction": "",
            "Payload": "horizontal_movement_range = source_total//5\nvertical_movement_range = source_total//10"
        },
    "Lunge":{
            "Type": "Movement",
            "Stat": "STR",
            "Skill": "Jump",
            "Speed": "1",
            "Range": "1",
            "Description": "\u2022Make a Lunge check to gain stages of Momentum.\n\u2022Momentum stage = Lunge check / 10 \n\u2022 You can use MP instead of AP if you desire",
            "Dice_Roll": "d20",
            "Action_Type": "Roll",
            "Reaction": "",
            "Payload": "source_momentum_stage += (source_total//10)"
        },
    "Climb":{
            "Type": "Movement",
            "Stat": "STR",
            "Skill": "Jump",
            "Speed": "1",
            "Range": "1",
            "Description": "\u2022Make a Climb check to scale up a surface or creature. \n\u2022DC = 5 + (2 * Total climbing range)\n\u2022On a fail, you fall from your height and suffer any applicable effects. \n\u2022 You can use MP instead of AP if you desire",
            "Dice_Roll": "d20",
            "Action_Type": "Roll",
            "Reaction": "",
            "Payload": ""
        },
    "Dive":{
            "Type": "Reaction",
            "Stat": "DEX",
            "Skill": "Coordination",
            "Speed": "2",
            "Range": "Jump",
            "Description": "\u2022Trigger - An Attack is declared against you or you are in the Area of Effect of an Attack or Special Move.\n*Dive automatically fails if Attacks or Special Moves targeting you fill the Area of Effect you are in and you are not within Jumping range of the border of that Attack\u2019s Area of Effect IE: Earthquake\nEffect:\n\u2022Move up to the Range away to gain a +10 on a Dodge Check but land Prone \n\u2022Prone stage = 0 to 8 Stage 3; 9 to 14 stage 2; 15+ Stage 1\n\u2022 EQUATION: Armors Agility Bonus + Dive Bonus (full, 1/2, or 0 SEE ARMOR) + 1d6 + 10.",
            "Dice_Roll": "d6",
            "Action_Type": "Reaction",
            "Reaction": "",
            "Payload": "action_result = \"Failure\"\nsource_prone_stage +=1"
        },
    "Dodge":{
            "Type": "Reaction",
            "Stat": "DEX",
            "Skill": "Coordination",
            "Speed": "1",
            "Range": "0",
            "Description": "\u2022Trigger - An Attack is declared against you or you are in the Area of Effect of an Attack or Special Move.\n*Dodge automatically fails if Attacks or Special Moves targeting you fill the Area of Effect you are in and you are not on the border of that Attack\u2019s Area of Effect IE: Earthquake\nEffect:\n\u2022Roll 1d6 and add your Armor's Dodge Bonus to contest the Attack or evade the effect. On success, you take no damage.\n\u2022 EQUATION: Armors Agility Bonus + Dodge Bonus (full, 1/2, or 0 SEE ARMOR) + 1d6.",
            "Dice_Roll": "d6",
            "Action_Type": "Reaction",
            "Reaction": "",
            "Payload": "action_result = \"Failure\""
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
            "Payload": "action_result = \"Failure\""
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
            "Payload": "source_vitality -= 1"
        },
    "Steal":{
            "Type": "Action",
            "Stat": "DEX",
            "Skill": "Sleight of Hand",
            "Speed": "2",
            "Range": "1",
            "Description": "\u2022An attempt to take an equipped weapon or item from an equipment slot of the Target (not from a hand). Make a Steal contest against the target\u2019s +8 Perception check. On a success, you take the item, on a fail the target is given a free opportunity attack against you\n\u2022Each stage of the Hidden status you have against the target gives you an additional +3 toward the Steal check",
            "Dice_Roll": "d20",
            "Action_Type": "Contest",
            "Reaction": "Perception",
            "Payload": ""
        },
      "Feint":{
            "Type": "Action",
            "Stat": "DEX",
            "Skill": "Sleight",
            "Speed": "2",
            "Range": "~",
            "Description": "\u2022Roll a Feint contest against a target\u2019s Evaluate Enemy check. On a success you deceive a target of your intended attack, and they must roll their intended reaction to the attack. The target cannot use the same reaction against your next attack ",
            "Dice_Roll": "d20",
            "Action_Type": "Contest",
            "Reaction": "Evaluate Enemy",
            "Payload": ""
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
            "Payload": ""
        },
    "Hide":{
            "Type": "Movement",
            "Stat": "DEX",
            "Skill": "Stealth",
            "Speed": "2",
            "Range": "0",
            "Description": "\u2022Attempt to hide away from view. Make a Hide check. DC determined by the GM. On a success, you gain 1 stage of Hidden\n\u2022 You can use MP instead of AP if you desire",
            "Dice_Roll": "d20",
            "Action_Type": "DC",
            "Reaction": "",
            "Payload": ""
        },
    "Block":{
            "Type": "Reaction",
            "Stat": "CON",
            "Skill": "Endurance",
            "Speed": "1",
            "Range": "0",
      "Description": "\u2022Trigger - An Attack or special move is declared against you or you are in the Area of Effect of an Attack or special move.\nEffect:\n\u2022Roll 1d6 and add your armors Defense bonus to contest the Attack or evade the effect. On success, you take no damage\n\u2022 EQUATION: Armors Defense Bonus + Block Bonus (full, 1/2, or 0 SEE ARMOR) + 1d6.",
            "Dice_Roll": "d6",
            "Action_Type": "Reaction",
            "Reaction": "",
            "Payload": "action_result = \"Failure\""
        },
    "Brace":{
            "Type": "Action",
            "Stat": "CON",
            "Skill": "Endurance",
            "Speed": "2",
            "Range": "0",
            "Description": "\u2022Roll a Brace check to give yourself an additional RP until the start of your next turn. \n\u2022Extra RP = the Brace check /5 (rounded down)",
            "Dice_Roll": "d20",
            "Action_Type": "Special",
            "Reaction": "",
            "Payload": ""
        },
    "Charge Power":{
            "Type": "Action",
            "Stat": "CON",
            "Skill": "Concentration",
            "Speed": "2",
            "Range": "0",
            "Description": "\u2022Roll a Charge Power check to gain momentum towards your next Power Rank \n\u2022DC = 10 + Power Rank",
            "Dice_Roll": "d20",
            "Action_Type": "Roll",
            "Reaction": "",
            "Payload": ""
        },
    "Concentrate":{
            "Type": "Action",
            "Stat": "CON",
            "Skill": "Concentration",
            "Speed": "2",
            "Range": "0",
      "Description": "\u2022Roll a concentrate check to remove mental statuses or maintain Concentration on the spell or effect. \n\u2022 SPELL CONCENTRATE: DC = 8 + power rank of spell + number of turns concentrated.\n\2022 MENTAL STATUS: DC = 8 + 1 per debuff. On a success, remove all stages of 1 mental status.",
            "Dice_Roll": "d20",
            "Action_Type": "Roll",
            "Reaction": "",
            "Payload": ""
        },
    "Focus":{
            "Type": "Action",
            "Stat": "CON`",
            "Skill": "Concentration",
            "Speed": "2",
            "Range": "0",
            "Description": "\u2022Focus can be applied before any action to raise the minimum roll value. \n\u2022Roll a Focus check and divide it in half to make a focus value. On your following action, any dice roll below this focus value will be treated as the focus value instead of the dice value (except for Crit fails).",
            "Dice_Roll": "d20",
            "Action_Type": "Roll",
            "Reaction": "",
            "Payload": ""
        },
    "Recover":{
            "Type": "Action",
            "Stat": "CON",
            "Skill": "Vitality",
            "Speed": "2",
            "Range": "2",
            "Description": "\u2022Roll a Recover Check to regain a damaged health block or applicable status. DC = 8 + 1 per Debuff status currently affecting you AND Missing Health Block",
            "Dice_Roll": "d20",
            "Action_Type": "Roll",
            "Reaction": "",
            "Payload": ""
        },
    "Enemy History":{
            "Type": "Action",
            "Stat": "INT",
            "Skill": "Academic",
            "Speed": "1",
            "Range": "24",
            "Description": "\u2022Roll an Enemy History check to tap your knowledge of any historical record or mentions of this specific group. DC is determined by the GM",
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
            "Description": "\u2022Roll an Arcana check to tap your knowledge of what magic is being used and what effects it has. DC is determined by the GM",
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
            "Description": "\u2022Roll a Tactics check contested against the targets insight check to tap knowledge of any specific tactics used by the enemy's Stat Block.",
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
            "Description": "Search a corpse or through your bag for a spesific item. DC is determined by GM",
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
            "Description": "\u2022Roll a Battlefield check to find any advantages or weaknesses presented on the battlefield. You can learn a number of positions = Battlefield check / 5",
            "Dice_Roll": "d20",
            "Action_Type": "DC",
            "Reaction": "",
            "Payload": ""
        },
    "Evaluate Enemy":{
            "Type": "Action",
            "Stat": "WIS",
            "Skill": "Insight",
            "Speed": "1",
            "Range": "24",
            "Description": "\u2022Try to read an enemies motives strengths and difficulty. DC is determined by the GM",
            "Dice_Roll": "d20",
            "Action_Type": "Contest",
            "Reaction": "",
            "Payload": ""
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
            "Payload": ""
        },
    "Improvise":{
            "Type": "Action",
            "Stat": "WIS",
            "Skill": "Interaction",
            "Speed": "1",
            "Range": "~",
            "Description": "\u2022Find a branch for a quick weapon, kick dirt to put out a fire, or use your ingenuity to solve a quick problem. DC is determined by GM.",
            "Dice_Roll": "d20",
            "Action_Type": "DC",
            "Reaction": "",
            "Payload": ""
        },
    "Bandage":{
            "Type": "Action",
            "Stat": "WIS",
            "Skill": "Medicine",
            "Speed": "2",
            "Range": "1",
            "Description": "\u2022Aid an ally by Healing a Health Block or 1 status (if applicable). DC determined by Status or GM",
            "Dice_Roll": "d20",
            "Action_Type": "Roll",
            "Reaction": "",
            "Payload": ""
        },
    "Aim":{
            "Type": "Action",
            "Stat": "WIS",
            "Skill": "Perception",
            "Speed": "2",
            "Range": "Attack Range",
            "Description": "\u2022Roll an Aim check to improve the accuracy of your next attack (action or special move) against a single target you can see. Add your Aim Check total / 4 to your following attack roll. ",
            "Dice_Roll": "d20",
            "Action_Type": "Roll",
            "Reaction": "",
            "Payload": ""
        },
    "Find Vitals":{
            "Type": "Action",
            "Stat": "WIS",
            "Skill": "Survival",
            "Speed": "2",
            "Range": "24",
            "Description": "\u2022Roll a Find Vitals to determine an enemies Vital points. The vital stage you learn is equal to your Find Vitals check divided by 10",
            "Dice_Roll": "d20",
            "Action_Type": "Contest",
            "Reaction": "",
            "Payload": ""
        },
    "Taunt":{
            "Type": "Action",
            "Stat": "CHA",
            "Skill": "Aggressive",
            "Speed": "2",
            "Range": "24",
            "Description": "\u2022Roll a Taunt check against a target to inflict the Captivated Frightened, or Frenzied status to a target. DC determined by GM",
            "Dice_Roll": "d20",
            "Action_Type": "DC",
            "Reaction": "",
            "Payload": ""
        },
    "Distract":{
            "Type": "Action",
            "Stat": "CHA",
            "Skill": "Suave",
            "Speed": "2",
            "Range": "24",
            "Description": "\u2022Roll a Distract check against a target to give a target a level of Flanked. DC determined by GM",
            "Dice_Roll": "d20",
            "Action_Type": "DC",
            "Reaction": "",
            "Payload": ""
        },
    "Pacify":{
            "Type": "Action",
            "Stat": "CHA",
            "Skill": "Diplomatic",
            "Speed": "2",
            "Range": "24",
            "Description": "\u2022Roll a Pacify check against a target's Diplomatic check to try and convince a them to withdraw from combat. On a success, initiative is paused.\n\n\u2022You can replace the roll with a Sincere check -2/Health Tier missing or an Aggressive check -2/ unbroken health tier. ",
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
            "Description": "\u2022Roll an Encourage check against a target to remove a Mental status from a target. DC determined by GM",
            "Dice_Roll": "d20",
            "Action_Type": "DC",
            "Reaction": "",
            "Payload": ""
        }
  }




//Player one rolls

function master_reset(){
  function reset(skill,action,reaction,prime,wounded,bloodied,prime_total,wounded_total,bloodied_total,aP,rP,mP,status1,stage1,status2,stage2,status3,stage3,status4,stage4,status5,stage5,status6,stage6){
    //get the rows and columns of each parameter so that we can add 6 to them later and reset them row by row)
    var skill_row = parseInt( skill.slice(1));
    var action_row = parseInt( action.slice(1));
    var reaction_row = parseInt( reaction.slice(1));
    var prime_row = parseInt( prime.slice(1));
    var wounded_row = parseInt( wounded.slice(1));
    var bloodied_row = parseInt( bloodied.slice(1));
    var prime_total_row = parseInt( prime_total.slice(1));
    var wounded_total_row = parseInt( wounded_total.slice(1));
    var bloodied_total_row = parseInt( bloodied_total.slice(1));
    var aP_row = parseInt( aP.slice(1));
    var rP_row = parseInt( rP.slice(1));
    var mP_row = parseInt( mP.slice(1));
    var status1_row = parseInt( status1.slice(1));
    var stage1_row = parseInt( stage1.slice(1));
    var status2_row = parseInt( status2.slice(1));
    var stage2_row = parseInt( stage2.slice(1));
    var status3_row = parseInt( status3.slice(1));
    var stage3_row = parseInt( stage3.slice(1));
    var status4_row = parseInt( status4.slice(1));
    var stage4_row = parseInt( stage4.slice(1));
    var status5_row = parseInt( status5.slice(1));
    var stage5_row = parseInt( stage5.slice(1));
    var status6_row = parseInt( status6.slice(1));
    var stage6_row = parseInt( stage6.slice(1));

    var skill_col = skill.slice(0,1);
    var action_col = action.slice(0,1);
    var reaction_col = reaction.slice(0,1);
    var prime_col = prime.slice(0,1);
    var wounded_col = wounded.slice(0,1);
    var bloodied_col = bloodied.slice(0,1);
    var prime_total_col = prime_total.slice(0,1);
    var wounded_total_col = wounded_total.slice(0,1);
    var bloodied_total_col = bloodied_total.slice(0,1);
    var aP_col = aP.slice(0,1);
    var rP_col = rP.slice(0,1);
    var mP_col = mP.slice(0,1);
    var status1_col = status1.slice(0,1);
    var stage1_col = stage1.slice(0,1);
    var status2_col = status2.slice(0,1);
    var stage2_col = stage2.slice(0,1);
    var status3_col = status3.slice(0,1);
    var stage3_col = stage3.slice(0,1);
    var status4_col = status4.slice(0,1);
    var stage4_col = stage4.slice(0,1);
    var status5_col = status5.slice(0,1);
    var stage5_col = stage5.slice(0,1);
    var status6_col = status6.slice(0,1);
    var stage6_col = stage6.slice(0,1);

    
    //get the current values of each 
    var skill_val = SpreadsheetApp.getActiveSheet().getRange(skill).getValue();
    var action_val = SpreadsheetApp.getActiveSheet().getRange(action).getValue();
    var reaction_val = SpreadsheetApp.getActiveSheet().getRange(reaction).getValue();
    var prime_val = SpreadsheetApp.getActiveSheet().getRange(prime).getValue();
    var wounded_val = SpreadsheetApp.getActiveSheet().getRange(wounded).getValue();
    var bloodied_val = SpreadsheetApp.getActiveSheet().getRange(bloodied).getValue();
    var prime_total_val = SpreadsheetApp.getActiveSheet().getRange(prime_total).getValue();
    var wounded_total_val = SpreadsheetApp.getActiveSheet().getRange(wounded_total).getValue();
    var bloodied_total_val = SpreadsheetApp.getActiveSheet().getRange(bloodied_total).getValue();
    var aP_val = SpreadsheetApp.getActiveSheet().getRange(aP).getValue();
    var rP_val = SpreadsheetApp.getActiveSheet().getRange(rP).getValue();
    var mP_val = SpreadsheetApp.getActiveSheet().getRange(mP).getValue();
    var status1_val = SpreadsheetApp.getActiveSheet().getRange(status1).getValue();
    var stage1_val = SpreadsheetApp.getActiveSheet().getRange(stage1).getValue();
    var status2_val = SpreadsheetApp.getActiveSheet().getRange(status2).getValue();
    var stage2_val = SpreadsheetApp.getActiveSheet().getRange(stage2).getValue();
    var status3_val = SpreadsheetApp.getActiveSheet().getRange(status3).getValue();
    var stage3_val = SpreadsheetApp.getActiveSheet().getRange(stage3).getValue();
    var status4_val = SpreadsheetApp.getActiveSheet().getRange(status4).getValue();
    var stage4_val = SpreadsheetApp.getActiveSheet().getRange(stage4).getValue();
    var status5_val = SpreadsheetApp.getActiveSheet().getRange(status5).getValue();
    var stage5_val = SpreadsheetApp.getActiveSheet().getRange(stage5).getValue();
    var status6_val = SpreadsheetApp.getActiveSheet().getRange(status6).getValue();
    var stage6_val = SpreadsheetApp.getActiveSheet().getRange(stage6).getValue();
        
    
    //while loop to reset all the values and iterate through all of characters
    var initiative = 1;
    
    var skill_pos = skill_col + skill_row;
    var action_pos = action_col + action_row;
    var reaction_pos = reaction_col + reaction_row;
    var prime_pos = prime_col + prime_row;
    var wounded_pos = wounded_col + wounded_row;
    var bloodied_pos = bloodied_col + bloodied_row;
    var prime_total_pos = prime_total_col + prime_total_row;
    var wounded_total_pos = wounded_total_col + wounded_total_row;
    var bloodied_total_pos = bloodied_total_col + bloodied_total_row;
    var aP_pos = aP_col + aP_row;
    var rP_pos = rP_col + rP_row;
    var mP_pos = mP_col + mP_row;
    var status1_pos = status1_col + status1_row;
    var stage1_pos = stage1_col + stage1_row;
    var status2_pos = status2_col + status2_row;
    var stage2_pos = stage2_col + stage2_row;
    var status3_pos = status3_col + status3_row;
    var stage3_pos = stage3_col + stage3_row;
    var status4_pos = status4_col + status4_row;
    var stage4_pos = stage4_col + stage4_row;
    var status5_pos = status5_col + status5_row;
    var stage5_pos = stage5_col + stage5_row;
    var status6_pos = status6_col + status6_row;
    var stage6_pos = stage6_col + stage6_row;
    
    while (initiative < 12){
      skill_val = "Academic";
      action_val = "Aim";
      reaction_val = "Block";

      prime_val = prime_total_val;
      wounded_val = wounded_total_val;
      bloodied_val = bloodied_total_val;
      aP_val = 6;
      rP_val = 6;
      mP_val = 6;
      status1_val = "";
      stage1_val = "";
      status2_val = "";
      stage2_val = "";
      status3_val = "";
      stage3_val = "";
      status4_val = "";
      stage4_val = "";
      status5_val = "";
      stage5_val = "";
      status6_val = "";
      stage6_val = "";
      
      
      skill_pos = skill_col + skill_row;
      action_pos = action_col + action_row;
      reaction_pos = reaction_col + reaction_row;
      prime_pos = prime_col + prime_row;
      wounded_pos = wounded_col + wounded_row;
      bloodied_pos = bloodied_col + bloodied_row;
      prime_total_pos = prime_total_col + prime_total_row;
      wounded_total_pos = wounded_total_col + wounded_total_row;
      bloodied_total_pos = bloodied_total_col + bloodied_total_row;
      aP_pos = aP_col + aP_row;
      rP_pos = rP_col + rP_row;
      mP_pos = mP_col + mP_row;
      status1_pos = status1_col + status1_row;
      stage1_pos = stage1_col + stage1_row;
      status2_pos = status2_col + status2_row;
      stage2_pos = stage2_col + stage2_row;
      status3_pos = status3_col + status3_row;
      stage3_pos = stage3_col + stage3_row;
      status4_pos = status4_col + status4_row;
      stage4_pos = stage4_col + stage4_row;
      status5_pos = status5_col + status5_row;
      stage5_pos = stage5_col + stage5_row;
      status6_pos = status6_col + status6_row;
      stage6_pos = stage6_col + stage6_row;
      
      prime_total_val = SpreadsheetApp.getActiveSheet().getRange(prime_total_pos).getValue();
      wounded_total_val = SpreadsheetApp.getActiveSheet().getRange(wounded_total_pos).getValue();
      bloodied_total_val = SpreadsheetApp.getActiveSheet().getRange(bloodied_total_pos).getValue();
      
      
      
      SpreadsheetApp.getActiveSheet().getRange(skill_pos).setValue(skill_val);
      SpreadsheetApp.getActiveSheet().getRange(action_pos).setValue(action_val);
      SpreadsheetApp.getActiveSheet().getRange(reaction_pos).setValue(reaction_val);
      SpreadsheetApp.getActiveSheet().getRange(prime_pos).setValue(prime_val);
      SpreadsheetApp.getActiveSheet().getRange(wounded_pos).setValue(wounded_val);
      SpreadsheetApp.getActiveSheet().getRange(bloodied_pos).setValue(bloodied_val);
      SpreadsheetApp.getActiveSheet().getRange(aP_pos).setValue(aP_val);
      SpreadsheetApp.getActiveSheet().getRange(rP_pos).setValue(rP_val);
      SpreadsheetApp.getActiveSheet().getRange(mP_pos).setValue(mP_val);
      SpreadsheetApp.getActiveSheet().getRange(status1_pos).setValue(status1_val);
      SpreadsheetApp.getActiveSheet().getRange(stage1_pos).setValue(stage1_val);
      SpreadsheetApp.getActiveSheet().getRange(status2_pos).setValue(status2_val);
      SpreadsheetApp.getActiveSheet().getRange(stage2_pos).setValue(stage2_val);
      SpreadsheetApp.getActiveSheet().getRange(status3_pos).setValue(status3_val);
      SpreadsheetApp.getActiveSheet().getRange(stage3_pos).setValue(stage3_val);
      SpreadsheetApp.getActiveSheet().getRange(stage4_pos).setValue(stage4_val);
      SpreadsheetApp.getActiveSheet().getRange(status5_pos).setValue(status5_val);
      SpreadsheetApp.getActiveSheet().getRange(stage5_pos).setValue(stage5_val);
      SpreadsheetApp.getActiveSheet().getRange(status6_pos).setValue(status6_val);
      SpreadsheetApp.getActiveSheet().getRange(stage6_pos).setValue(stage6_val);
      
      skill_row = skill_row + 6;
      action_row = action_row + 6;
      reaction_row = reaction_row + 6;
      prime_row = prime_row + 6;
      wounded_row = wounded_row + 6;
      bloodied_row = bloodied_row + 6;
      aP_row = aP_row + 6;
      rP_row = rP_row + 6;
      mP_row = mP_row + 6;
      status1_row = status1_row + 6;
      stage1_row = stage1_row + 6;
      status2_row = status2_row + 6;
      stage2_row = stage2_row + 6;
      status3_row = status3_row + 6;
      stage3_row = stage3_row + 6;
      status4_row = status4_row + 6;
      stage4_row = stage4_row + 6;
      status5_row = status5_row + 6;
      stage5_row = stage5_row + 6;
      status6_row = status6_row + 6;
      stage6_row = stage6_row + 6;
      prime_total_row = prime_total_row + 6;
      wounded_total_row = wounded_total_row + 6;
      bloodied_total_row = bloodied_total_row + 6;
      
      initiative ++;
    }
  }
    
  reset("C3","C5","C7","M4","K4","I4","M3","K3","I3","O2","O4","O6","P2","Q2","P3","Q3","P4","Q4","P5","Q5","P6","Q6","P7","Q7")
}

function p1_skill(){
  function roll(mod_pos, roll_pos, final_pos) {
    var ui = SpreadsheetApp.getUi();
    var min = 1;
    var max = 21;
    var mod = SpreadsheetApp.getActiveSheet().getRange(mod_pos).getValue();
    var roll = Math.floor(Math.random() * (max - min)) + min; //The maximum is exclusive and the minimum is inclusive
    SpreadsheetApp.getActiveSheet().getRange(roll_pos).setValue(roll);
    var final = parseInt(mod) + roll
  
    SpreadsheetApp.getActiveSheet().getRange(final_pos).setValue(final);
  }
  roll("D3", "F2", "G2")
}

function p1_action(){
  function roll(mod_pos, roll_pos, final_pos, ap_pos, action_pos) {
    var ui = SpreadsheetApp.getUi();
    var min = 1;
    var max = 21;
    var action = SpreadsheetApp.getActiveSheet().getRange(action_pos).getValue();
    var mod = SpreadsheetApp.getActiveSheet().getRange(mod_pos).getValue();
    ui.alert(actions_dict[action]["Description"])
    
    //lower the ap
    var ap = SpreadsheetApp.getActiveSheet().getRange(ap_pos).getValue();

    ap = ap - actions_dict[action]["Speed"];
    
    SpreadsheetApp.getActiveSheet().getRange(ap_pos).setValue(ap);
    
    var roll = Math.floor(Math.random() * (max - min)) + min; //The maximum is exclusive and the minimum is inclusive
    SpreadsheetApp.getActiveSheet().getRange(roll_pos).setValue(roll);
    var final = parseInt(mod) + roll;
  
    SpreadsheetApp.getActiveSheet().getRange(final_pos).setValue(final);
  }
  roll("D5", "F4", "G4", "O2","C5")
}

function p1_reaction(){
  function reaction_roll(react_name, mod_pos, roll_pos, final_pos, rp_pos) {
    var ui = SpreadsheetApp.getUi();
    var min = 1;
    var max = 21;
    var name = SpreadsheetApp.getActiveSheet().getRange(react_name).getValue();
    ui.alert(actions_dict[name]["Description"])
    if (name == "Block"|| name == "Dodge" || name == "Dive"){
      max = 7;
    }else{
      max = 21;
    }
    
    var ap = SpreadsheetApp.getActiveSheet().getRange(rp_pos).getValue();
    ap = ap - actions_dict[name]["Speed"];
    SpreadsheetApp.getActiveSheet().getRange(rp_pos).setValue(ap);
    
    var mod = SpreadsheetApp.getActiveSheet().getRange(mod_pos).getValue();
    var roll = Math.floor(Math.random() * (max - min)) + min; //The maximum is exclusive and the minimum is inclusive
    SpreadsheetApp.getActiveSheet().getRange(roll_pos).setValue(roll);
    var final = parseInt(mod) + roll
  
    SpreadsheetApp.getActiveSheet().getRange(final_pos).setValue(final);
  }
  reaction_roll("C7", "D7", "F6", "G6", "O4")
}

// player 1 damage
function p1_damage(){
  function damage(prime,wounded,bloodied){
    var ui = SpreadsheetApp.getUi();
    var hp_prime = SpreadsheetApp.getActiveSheet().getRange(prime).getValue();
    var hp_wounded = SpreadsheetApp.getActiveSheet().getRange(wounded).getValue();
    var hp_bloodied = SpreadsheetApp.getActiveSheet().getRange(bloodied).getValue();
    var broken = "X";
    
    if (hp_prime != broken && hp_prime > 0){
      hp_prime -= 1;
    }else if (hp_prime == 0){
      
      hp_prime = broken;
      hp_wounded -= 1;
      ui.alert("You broke your prime Stamina. Roll a d20 for your injury.");
    }else if (hp_wounded != broken && hp_wounded > 0){
      hp_wounded -= 1;
    }else if (hp_wounded == 0){
      
      hp_wounded = broken;
      hp_bloodied -= 1;
      ui.alert("You broke your core Stamina. Roll a d20 for your injury.");
    }else if (hp_bloodied != broken && hp_bloodied > 0){
      hp_bloodied -= 1;
    }else if (hp_bloodied == 0){
      
      hp_bloodied = broken;
      ui.alert("You are dying! Roll a Death Saving throw");      
    }else{
      ui.alert("Something is wrong with your HP, please reset and try again");
    }
    
    SpreadsheetApp.getActiveSheet().getRange(prime).setValue(String(hp_prime));
    SpreadsheetApp.getActiveSheet().getRange(wounded).setValue(String(hp_wounded));
    SpreadsheetApp.getActiveSheet().getRange(bloodied).setValue(String(hp_bloodied));
  }
  
  damage("M4", "K4", "I4")
}

//p1 heal button

function p1_stamina(){
  function stamina(prime_max, prime_hp, wounded_max, wounded_hp, bloodied_max, bloodied_hp, ap, rp, mp){
    var full = 6
    
    SpreadsheetApp.getActiveSheet().getRange(ap).setValue(String(full));
    SpreadsheetApp.getActiveSheet().getRange(rp).setValue(String(full));
    SpreadsheetApp.getActiveSheet().getRange(mp).setValue(String(full));
    var ui = SpreadsheetApp.getUi();
    var max_prime = SpreadsheetApp.getActiveSheet().getRange(prime_max).getValue();
    var hp_prime = SpreadsheetApp.getActiveSheet().getRange(prime_hp).getValue();
    var max_wounded = SpreadsheetApp.getActiveSheet().getRange(wounded_max).getValue();
    var hp_wounded = SpreadsheetApp.getActiveSheet().getRange(wounded_hp).getValue();
    var max_bloodied = SpreadsheetApp.getActiveSheet().getRange(bloodied_max).getValue();
    var hp_bloodied = SpreadsheetApp.getActiveSheet().getRange(bloodied_hp).getValue();
    var broken = "X";

    
    if (hp_prime != broken){
      hp_prime = max_prime;
      SpreadsheetApp.getActiveSheet().getRange(prime_hp).setValue(String(hp_prime));
    }else if (hp_wounded != broken){
      hp_wounded = max_wounded;
      SpreadsheetApp.getActiveSheet().getRange(wounded_hp).setValue(String(hp_wounded));
    }else if (hp_bloodied != broken){
      hp_bloodied = max_bloodied;
      SpreadsheetApp.getActiveSheet().getRange(bloodied_hp).setValue(String(hp_bloodied));
    }else if (hp_bloodied == broken){
      ui.alert("You can not recover when you are dying.")
    }else{
      ui.alert("Something is wrong with your HP, please reset and try again");
    }    
    
  }
  stamina("M3","M4","K3","K4","I3","I4","O2","O4","O6")
}

//player 2 rolls


function p2_skill(){
  function roll(mod_pos, roll_pos, final_pos) {
    var ui = SpreadsheetApp.getUi();
    var min = 1;
    var max = 21;
    var mod = SpreadsheetApp.getActiveSheet().getRange(mod_pos).getValue();
    var roll = Math.floor(Math.random() * (max - min)) + min; //The maximum is exclusive and the minimum is inclusive
    SpreadsheetApp.getActiveSheet().getRange(roll_pos).setValue(roll);
    var final = parseInt(mod) + roll
  
    SpreadsheetApp.getActiveSheet().getRange(final_pos).setValue(final);
  }
  roll("D9", "F8", "G8")
}

function p2_action(){
    function roll(mod_pos, roll_pos, final_pos, ap_pos, action_pos) {
    var ui = SpreadsheetApp.getUi();
    var min = 1;
    var max = 21;
    var action = SpreadsheetApp.getActiveSheet().getRange(action_pos).getValue();
    var mod = SpreadsheetApp.getActiveSheet().getRange(mod_pos).getValue();
    ui.alert(actions_dict[action]["Description"])
    
    //lower the ap
    var ap = SpreadsheetApp.getActiveSheet().getRange(ap_pos).getValue();

      ap = ap - actions_dict[action]["Speed"];
    
    SpreadsheetApp.getActiveSheet().getRange(ap_pos).setValue(ap);
    
    var roll = Math.floor(Math.random() * (max - min)) + min; //The maximum is exclusive and the minimum is inclusive
    SpreadsheetApp.getActiveSheet().getRange(roll_pos).setValue(roll);
    var final = parseInt(mod) + roll;
  
    SpreadsheetApp.getActiveSheet().getRange(final_pos).setValue(final);
  }
  roll("D11", "F10", "G10", "O8", "C11")
}

function p2_reaction(){
  function reaction_roll(react_name, mod_pos, roll_pos, final_pos, rp_pos) {
    var ui = SpreadsheetApp.getUi();
    var min = 1;
    var max = 21;
    var name = SpreadsheetApp.getActiveSheet().getRange(react_name).getValue();
    ui.alert(actions_dict[name]["Description"])
    if (name == "Block"|| name == "Dodge" || name == "Dive"){
      max = 7;
    }else{
      max = 21;
    }
    
    var ap = SpreadsheetApp.getActiveSheet().getRange(rp_pos).getValue();
    ap = ap - actions_dict[name]["Speed"];
    SpreadsheetApp.getActiveSheet().getRange(rp_pos).setValue(ap);
    
    var mod = SpreadsheetApp.getActiveSheet().getRange(mod_pos).getValue();
    var roll = Math.floor(Math.random() * (max - min)) + min; //The maximum is exclusive and the minimum is inclusive
    SpreadsheetApp.getActiveSheet().getRange(roll_pos).setValue(roll);
    var final = parseInt(mod) + roll
  
    SpreadsheetApp.getActiveSheet().getRange(final_pos).setValue(final);
  }
  reaction_roll("C13", "D13", "F12", "G12", "O10")
}

function p2_damage(){
  function damage(prime,wounded,bloodied){
    var ui = SpreadsheetApp.getUi();
    var hp_prime = SpreadsheetApp.getActiveSheet().getRange(prime).getValue();
    var hp_wounded = SpreadsheetApp.getActiveSheet().getRange(wounded).getValue();
    var hp_bloodied = SpreadsheetApp.getActiveSheet().getRange(bloodied).getValue();
    var broken = "X";
    
    if (hp_prime != broken && hp_prime > 0){
      hp_prime -= 1;
    }else if (hp_prime == 0){
      
      hp_prime = broken;
      hp_wounded -= 1;
      ui.alert("You broke your prime Stamina. Roll a d20 for your injury.");
    }else if (hp_wounded != broken && hp_wounded > 0){
      hp_wounded -= 1;
    }else if (hp_wounded == 0){
      
      hp_wounded = broken;
      hp_bloodied -= 1;
      ui.alert("You broke your core Stamina. Roll a d20 for your injury.");
    }else if (hp_bloodied != broken && hp_bloodied > 0){
      hp_bloodied -= 1;
    }else if (hp_bloodied == 0){
      
      hp_bloodied = broken;
      ui.alert("You are dying! Roll a Death Saving throw");      
    }else{
      ui.alert("Something is wrong with your HP, please reset and try again");
    }
    
    SpreadsheetApp.getActiveSheet().getRange(prime).setValue(String(hp_prime));
    SpreadsheetApp.getActiveSheet().getRange(wounded).setValue(String(hp_wounded));
    SpreadsheetApp.getActiveSheet().getRange(bloodied).setValue(String(hp_bloodied));
  }
  
  damage("M10", "K10", "I10")
}

//p1 heal button

function p2_stamina(){
  function stamina(prime_max, prime_hp, wounded_max, wounded_hp, bloodied_max, bloodied_hp, ap, rp, mp){
    var full = 6
    
    SpreadsheetApp.getActiveSheet().getRange(ap).setValue(String(full));
    SpreadsheetApp.getActiveSheet().getRange(rp).setValue(String(full));
    SpreadsheetApp.getActiveSheet().getRange(mp).setValue(String(full));
    var ui = SpreadsheetApp.getUi();
    var max_prime = SpreadsheetApp.getActiveSheet().getRange(prime_max).getValue();
    var hp_prime = SpreadsheetApp.getActiveSheet().getRange(prime_hp).getValue();
    var max_wounded = SpreadsheetApp.getActiveSheet().getRange(wounded_max).getValue();
    var hp_wounded = SpreadsheetApp.getActiveSheet().getRange(wounded_hp).getValue();
    var max_bloodied = SpreadsheetApp.getActiveSheet().getRange(bloodied_max).getValue();
    var hp_bloodied = SpreadsheetApp.getActiveSheet().getRange(bloodied_hp).getValue();
    var broken = "X";
    
    if (hp_prime != broken){
      hp_prime = max_prime;
      SpreadsheetApp.getActiveSheet().getRange(prime_hp).setValue(String(hp_prime));
    }else if (hp_wounded != broken){
      hp_wounded = max_wounded;
      SpreadsheetApp.getActiveSheet().getRange(wounded_hp).setValue(String(hp_wounded));
    }else if (hp_bloodied != broken){
      hp_bloodied = max_bloodied;
      SpreadsheetApp.getActiveSheet().getRange(bloodied_hp).setValue(String(hp_bloodied));
    }else if (hp_bloodied == broken){
      ui.alert("You can not recover when you are dying.")
    }else{
      ui.alert("Something is wrong with your HP, please reset and try again");
    }    
    
  }
  stamina("M9","M10","K9","K10","I9","I10","O8","O10","O12")
}



//Player 3 rolls
function p3_skill(){
  function roll(mod_pos, roll_pos, final_pos) {
    var ui = SpreadsheetApp.getUi();
    var min = 1;
    var max = 21;
    var mod = SpreadsheetApp.getActiveSheet().getRange(mod_pos).getValue();
    var roll = Math.floor(Math.random() * (max - min)) + min; //The maximum is exclusive and the minimum is inclusive
    SpreadsheetApp.getActiveSheet().getRange(roll_pos).setValue(roll);
    var final = parseInt(mod) + roll
  
    SpreadsheetApp.getActiveSheet().getRange(final_pos).setValue(final);
  }
  roll("D15", "F14", "G14")
}

function p3_action(){
  function roll(mod_pos, roll_pos, final_pos, ap_pos, action_pos) {
    var ui = SpreadsheetApp.getUi();
    var min = 1;
    var max = 21;
    var action = SpreadsheetApp.getActiveSheet().getRange(action_pos).getValue();
    var mod = SpreadsheetApp.getActiveSheet().getRange(mod_pos).getValue();
    ui.alert(actions_dict[action]["Description"])
    
    //lower the ap
    var ap = SpreadsheetApp.getActiveSheet().getRange(ap_pos).getValue();

      ap = ap - actions_dict[action]["Speed"];
    
    SpreadsheetApp.getActiveSheet().getRange(ap_pos).setValue(ap);
    
    var roll = Math.floor(Math.random() * (max - min)) + min; //The maximum is exclusive and the minimum is inclusive
    SpreadsheetApp.getActiveSheet().getRange(roll_pos).setValue(roll);
    var final = parseInt(mod) + roll;
  
    SpreadsheetApp.getActiveSheet().getRange(final_pos).setValue(final);
  }
  roll("D17", "F16", "G16", "O14", "C17")
}

function p3_reaction(){
  function reaction_roll(react_name, mod_pos, roll_pos, final_pos, rp_pos) {
    var ui = SpreadsheetApp.getUi();
    var min = 1;
    var max = 21;
    var name = SpreadsheetApp.getActiveSheet().getRange(react_name).getValue();
    ui.alert(actions_dict[name]["Description"])
    if (name == "Block"|| name == "Dodge" || name == "Dive"){
      max = 7;
    }else{
      max = 21;
    }
    
    var ap = SpreadsheetApp.getActiveSheet().getRange(rp_pos).getValue();
    ap = ap - actions_dict[name]["Speed"];
    SpreadsheetApp.getActiveSheet().getRange(rp_pos).setValue(ap);
    
    var mod = SpreadsheetApp.getActiveSheet().getRange(mod_pos).getValue();
    var roll = Math.floor(Math.random() * (max - min)) + min; //The maximum is exclusive and the minimum is inclusive
    SpreadsheetApp.getActiveSheet().getRange(roll_pos).setValue(roll);
    var final = parseInt(mod) + roll
  
    SpreadsheetApp.getActiveSheet().getRange(final_pos).setValue(final);
  }
  reaction_roll("C19", "D19", "F18", "G18", "O16")
}

function p3_damage(){
  function damage(prime,wounded,bloodied){
    var ui = SpreadsheetApp.getUi();
    var hp_prime = SpreadsheetApp.getActiveSheet().getRange(prime).getValue();
    var hp_wounded = SpreadsheetApp.getActiveSheet().getRange(wounded).getValue();
    var hp_bloodied = SpreadsheetApp.getActiveSheet().getRange(bloodied).getValue();
    var broken = "X";
    
    if (hp_prime != broken && hp_prime > 0){
      hp_prime -= 1;
    }else if (hp_prime == 0){
      
      hp_prime = broken;
      hp_wounded -= 1;
      ui.alert("You broke your prime Stamina. Roll a d20 for your injury.");
    }else if (hp_wounded != broken && hp_wounded > 0){
      hp_wounded -= 1;
    }else if (hp_wounded == 0){
      
      hp_wounded = broken;
      hp_bloodied -= 1;
      ui.alert("You broke your core Stamina. Roll a d20 for your injury.");
    }else if (hp_bloodied != broken && hp_bloodied > 0){
      hp_bloodied -= 1;
    }else if (hp_bloodied == 0){
      
      hp_bloodied = broken;
      ui.alert("You are dying! Roll a Death Saving throw");      
    }else{
      ui.alert("Something is wrong with your HP, please reset and try again");
    }
    
    SpreadsheetApp.getActiveSheet().getRange(prime).setValue(String(hp_prime));
    SpreadsheetApp.getActiveSheet().getRange(wounded).setValue(String(hp_wounded));
    SpreadsheetApp.getActiveSheet().getRange(bloodied).setValue(String(hp_bloodied));
  }
  
  damage("M16", "K16", "I16")
}

//p3 heal button

function p3_stamina(){
  function stamina(prime_max, prime_hp, wounded_max, wounded_hp, bloodied_max, bloodied_hp, ap, rp, mp){
    var full = 6
    
    SpreadsheetApp.getActiveSheet().getRange(ap).setValue(String(full));
    SpreadsheetApp.getActiveSheet().getRange(rp).setValue(String(full));
    SpreadsheetApp.getActiveSheet().getRange(mp).setValue(String(full));
    var ui = SpreadsheetApp.getUi();
    var max_prime = SpreadsheetApp.getActiveSheet().getRange(prime_max).getValue();
    var hp_prime = SpreadsheetApp.getActiveSheet().getRange(prime_hp).getValue();
    var max_wounded = SpreadsheetApp.getActiveSheet().getRange(wounded_max).getValue();
    var hp_wounded = SpreadsheetApp.getActiveSheet().getRange(wounded_hp).getValue();
    var max_bloodied = SpreadsheetApp.getActiveSheet().getRange(bloodied_max).getValue();
    var hp_bloodied = SpreadsheetApp.getActiveSheet().getRange(bloodied_hp).getValue();
    var broken = "X";
    
    if (hp_prime != broken){
      hp_prime = max_prime;
      SpreadsheetApp.getActiveSheet().getRange(prime_hp).setValue(String(hp_prime));
    }else if (hp_wounded != broken){
      hp_wounded = max_wounded;
      SpreadsheetApp.getActiveSheet().getRange(wounded_hp).setValue(String(hp_wounded));
    }else if (hp_bloodied != broken){
      hp_bloodied = max_bloodied;
      SpreadsheetApp.getActiveSheet().getRange(bloodied_hp).setValue(String(hp_bloodied));
    }else if (hp_bloodied == broken){
      ui.alert("You can not recover when you are dying.")
    }else{
      ui.alert("Something is wrong with your HP, please reset and try again");
    }    
    
  }
  stamina("M15","M16","K15","K16","I15","I16","O14","O16","O18")
}


//player 4 rolls

function p4_skill(){
  function roll(mod_pos, roll_pos, final_pos) {
    var ui = SpreadsheetApp.getUi();
    var min = 1;
    var max = 21;
    var mod = SpreadsheetApp.getActiveSheet().getRange(mod_pos).getValue();
    var roll = Math.floor(Math.random() * (max - min)) + min; //The maximum is exclusive and the minimum is inclusive
    SpreadsheetApp.getActiveSheet().getRange(roll_pos).setValue(roll);
    var final = parseInt(mod) + roll
  
    SpreadsheetApp.getActiveSheet().getRange(final_pos).setValue(final);
  }
  roll("D21", "F20", "G20")
}

function p4_action(){
  function roll(mod_pos, roll_pos, final_pos, ap_pos, action_pos) {
    var ui = SpreadsheetApp.getUi();
    var min = 1;
    var max = 21;
    var action = SpreadsheetApp.getActiveSheet().getRange(action_pos).getValue();
    var mod = SpreadsheetApp.getActiveSheet().getRange(mod_pos).getValue();
    ui.alert(actions_dict[action]["Description"])
    
    //lower the ap
    var ap = SpreadsheetApp.getActiveSheet().getRange(ap_pos).getValue();

      ap = ap - actions_dict[action]["Speed"];
    
    SpreadsheetApp.getActiveSheet().getRange(ap_pos).setValue(ap);
    
    var roll = Math.floor(Math.random() * (max - min)) + min; //The maximum is exclusive and the minimum is inclusive
    SpreadsheetApp.getActiveSheet().getRange(roll_pos).setValue(roll);
    var final = parseInt(mod) + roll;
  
    SpreadsheetApp.getActiveSheet().getRange(final_pos).setValue(final);
  }
  roll("D23", "F22", "G22", "O20", "C23")
}

function p4_reaction(){
  function reaction_roll(react_name, mod_pos, roll_pos, final_pos, rp_pos) {
    var ui = SpreadsheetApp.getUi();
    var min = 1;
    var max = 21;
    var name = SpreadsheetApp.getActiveSheet().getRange(react_name).getValue();
    ui.alert(actions_dict[name]["Description"])
    if (name == "Block"|| name == "Dodge" || name == "Dive"){
      max = 7;
    }else{
      max = 21;
    }
    
    var ap = SpreadsheetApp.getActiveSheet().getRange(rp_pos).getValue();
    ap = ap - actions_dict[name]["Speed"];
    SpreadsheetApp.getActiveSheet().getRange(rp_pos).setValue(ap);
    
    var mod = SpreadsheetApp.getActiveSheet().getRange(mod_pos).getValue();
    var roll = Math.floor(Math.random() * (max - min)) + min; //The maximum is exclusive and the minimum is inclusive
    SpreadsheetApp.getActiveSheet().getRange(roll_pos).setValue(roll);
    var final = parseInt(mod) + roll
  
    SpreadsheetApp.getActiveSheet().getRange(final_pos).setValue(final);
  }
  reaction_roll("C25", "D25", "F24", "G24", "O22")
}

function p4_damage(){
  function damage(prime,wounded,bloodied){
    var ui = SpreadsheetApp.getUi();
    var hp_prime = SpreadsheetApp.getActiveSheet().getRange(prime).getValue();
    var hp_wounded = SpreadsheetApp.getActiveSheet().getRange(wounded).getValue();
    var hp_bloodied = SpreadsheetApp.getActiveSheet().getRange(bloodied).getValue();
    var broken = "X";
    
    if (hp_prime != broken && hp_prime > 0){
      hp_prime -= 1;
    }else if (hp_prime == 0){
      
      hp_prime = broken;
      hp_wounded -= 1;
      ui.alert("You broke your prime Stamina. Roll a d20 for your injury.");
    }else if (hp_wounded != broken && hp_wounded > 0){
      hp_wounded -= 1;
    }else if (hp_wounded == 0){
      
      hp_wounded = broken;
      hp_bloodied -= 1;
      ui.alert("You broke your core Stamina. Roll a d20 for your injury.");
    }else if (hp_bloodied != broken && hp_bloodied > 0){
      hp_bloodied -= 1;
    }else if (hp_bloodied == 0){
      
      hp_bloodied = broken;
      ui.alert("You are dying! Roll a Death Saving throw");      
    }else{
      ui.alert("Something is wrong with your HP, please reset and try again");
    }
    
    SpreadsheetApp.getActiveSheet().getRange(prime).setValue(String(hp_prime));
    SpreadsheetApp.getActiveSheet().getRange(wounded).setValue(String(hp_wounded));
    SpreadsheetApp.getActiveSheet().getRange(bloodied).setValue(String(hp_bloodied));
  }
  
  damage("M22", "K22", "I22")
}

//p4 heal button

function p4_stamina(){
  function stamina(prime_max, prime_hp, wounded_max, wounded_hp, bloodied_max, bloodied_hp, ap, rp, mp){
    var full = 6
    
    SpreadsheetApp.getActiveSheet().getRange(ap).setValue(String(full));
    SpreadsheetApp.getActiveSheet().getRange(rp).setValue(String(full));
    SpreadsheetApp.getActiveSheet().getRange(mp).setValue(String(full));
    var ui = SpreadsheetApp.getUi();
    var max_prime = SpreadsheetApp.getActiveSheet().getRange(prime_max).getValue();
    var hp_prime = SpreadsheetApp.getActiveSheet().getRange(prime_hp).getValue();
    var max_wounded = SpreadsheetApp.getActiveSheet().getRange(wounded_max).getValue();
    var hp_wounded = SpreadsheetApp.getActiveSheet().getRange(wounded_hp).getValue();
    var max_bloodied = SpreadsheetApp.getActiveSheet().getRange(bloodied_max).getValue();
    var hp_bloodied = SpreadsheetApp.getActiveSheet().getRange(bloodied_hp).getValue();
    var broken = "X";
    
    if (hp_prime != broken){
      hp_prime = max_prime;
      SpreadsheetApp.getActiveSheet().getRange(prime_hp).setValue(String(hp_prime));
    }else if (hp_wounded != broken){
      hp_wounded = max_wounded;
      SpreadsheetApp.getActiveSheet().getRange(wounded_hp).setValue(String(hp_wounded));
    }else if (hp_bloodied != broken){
      hp_bloodied = max_bloodied;
      SpreadsheetApp.getActiveSheet().getRange(bloodied_hp).setValue(String(hp_bloodied));
    }else if (hp_bloodied == broken){
      ui.alert("You can not recover when you are dying.")
    }else{
      ui.alert("Something is wrong with your HP, please reset and try again");
    }    
    
  }
  stamina("M21","M22","K21","K22","I21","I22","O20","O22","O24")
}


//player 5 rolls
function p5_skill(){
  function roll(mod_pos, roll_pos, final_pos) {
    var ui = SpreadsheetApp.getUi();
    var min = 1;
    var max = 21;
    var mod = SpreadsheetApp.getActiveSheet().getRange(mod_pos).getValue();
    var roll = Math.floor(Math.random() * (max - min)) + min; //The maximum is exclusive and the minimum is inclusive
    SpreadsheetApp.getActiveSheet().getRange(roll_pos).setValue(roll);
    var final = parseInt(mod) + roll
  
    SpreadsheetApp.getActiveSheet().getRange(final_pos).setValue(final);
  }
  roll("D27", "F26", "G26")
}

function p5_action(){
  function roll(mod_pos, roll_pos, final_pos, ap_pos, action_pos) {
    var ui = SpreadsheetApp.getUi();
    var min = 1;
    var max = 21;
    var action = SpreadsheetApp.getActiveSheet().getRange(action_pos).getValue();
    var mod = SpreadsheetApp.getActiveSheet().getRange(mod_pos).getValue();
    ui.alert(actions_dict[action]["Description"])
    
    //lower the ap
    var ap = SpreadsheetApp.getActiveSheet().getRange(ap_pos).getValue();

      ap = ap - actions_dict[action]["Speed"];
    
    SpreadsheetApp.getActiveSheet().getRange(ap_pos).setValue(ap);
    
    var roll = Math.floor(Math.random() * (max - min)) + min; //The maximum is exclusive and the minimum is inclusive
    SpreadsheetApp.getActiveSheet().getRange(roll_pos).setValue(roll);
    var final = parseInt(mod) + roll;
  
    SpreadsheetApp.getActiveSheet().getRange(final_pos).setValue(final);
  }
  roll("D29", "F28", "G28", "O26", "C29")
}

function p5_reaction(){
  function reaction_roll(react_name, mod_pos, roll_pos, final_pos, rp_pos) {
    var ui = SpreadsheetApp.getUi();
    var min = 1;
    var max = 21;
    var name = SpreadsheetApp.getActiveSheet().getRange(react_name).getValue();
    ui.alert(actions_dict[name]["Description"])
    if (name == "Block"|| name == "Dodge" || name == "Dive"){
      max = 7;
    }else{
      max = 21;
    }
    
    var ap = SpreadsheetApp.getActiveSheet().getRange(rp_pos).getValue();
    ap = ap - actions_dict[name]["Speed"];
    SpreadsheetApp.getActiveSheet().getRange(rp_pos).setValue(ap);
    
    var mod = SpreadsheetApp.getActiveSheet().getRange(mod_pos).getValue();
    var roll = Math.floor(Math.random() * (max - min)) + min; //The maximum is exclusive and the minimum is inclusive
    SpreadsheetApp.getActiveSheet().getRange(roll_pos).setValue(roll);
    var final = parseInt(mod) + roll
  
    SpreadsheetApp.getActiveSheet().getRange(final_pos).setValue(final);
  }
  reaction_roll("C31", "D31", "F30", "G30","028")
}

function p5_damage(){
  function damage(prime,wounded,bloodied){
    var ui = SpreadsheetApp.getUi();
    var hp_prime = SpreadsheetApp.getActiveSheet().getRange(prime).getValue();
    var hp_wounded = SpreadsheetApp.getActiveSheet().getRange(wounded).getValue();
    var hp_bloodied = SpreadsheetApp.getActiveSheet().getRange(bloodied).getValue();
    var broken = "X";
    
    if (hp_prime != broken && hp_prime > 0){
      hp_prime -= 1;
    }else if (hp_prime == 0){
      
      hp_prime = broken;
      hp_wounded -= 1;
      ui.alert("You broke your prime Stamina. Roll a d20 for your injury.");
    }else if (hp_wounded != broken && hp_wounded > 0){
      hp_wounded -= 1;
    }else if (hp_wounded == 0){
      
      hp_wounded = broken;
      hp_bloodied -= 1;
      ui.alert("You broke your core Stamina. Roll a d20 for your injury.");
    }else if (hp_bloodied != broken && hp_bloodied > 0){
      hp_bloodied -= 1;
    }else if (hp_bloodied == 0){
      
      hp_bloodied = broken;
      ui.alert("You are dying! Roll a Death Saving throw");      
    }else{
      ui.alert("Something is wrong with your HP, please reset and try again");
    }
    
    SpreadsheetApp.getActiveSheet().getRange(prime).setValue(String(hp_prime));
    SpreadsheetApp.getActiveSheet().getRange(wounded).setValue(String(hp_wounded));
    SpreadsheetApp.getActiveSheet().getRange(bloodied).setValue(String(hp_bloodied));
  }
  
  damage("M28", "K28", "I28")
}

//p5 heal button

function p5_stamina(){
  function stamina(prime_max, prime_hp, wounded_max, wounded_hp, bloodied_max, bloodied_hp, ap, rp, mp){
    var full = 6
    
    SpreadsheetApp.getActiveSheet().getRange(ap).setValue(String(full));
    SpreadsheetApp.getActiveSheet().getRange(rp).setValue(String(full));
    SpreadsheetApp.getActiveSheet().getRange(mp).setValue(String(full));
    var ui = SpreadsheetApp.getUi();
    var max_prime = SpreadsheetApp.getActiveSheet().getRange(prime_max).getValue();
    var hp_prime = SpreadsheetApp.getActiveSheet().getRange(prime_hp).getValue();
    var max_wounded = SpreadsheetApp.getActiveSheet().getRange(wounded_max).getValue();
    var hp_wounded = SpreadsheetApp.getActiveSheet().getRange(wounded_hp).getValue();
    var max_bloodied = SpreadsheetApp.getActiveSheet().getRange(bloodied_max).getValue();
    var hp_bloodied = SpreadsheetApp.getActiveSheet().getRange(bloodied_hp).getValue();
    var broken = "X";
    
    if (hp_prime != broken){
      hp_prime = max_prime;
      SpreadsheetApp.getActiveSheet().getRange(prime_hp).setValue(String(hp_prime));
    }else if (hp_wounded != broken){
      hp_wounded = max_wounded;
      SpreadsheetApp.getActiveSheet().getRange(wounded_hp).setValue(String(hp_wounded));
    }else if (hp_bloodied != broken){
      hp_bloodied = max_bloodied;
      SpreadsheetApp.getActiveSheet().getRange(bloodied_hp).setValue(String(hp_bloodied));
    }else if (hp_bloodied == broken){
      ui.alert("You can not recover when you are dying.")
    }else{
      ui.alert("Something is wrong with your HP, please reset and try again");
    }    
    
  }
  stamina("M27","M28","K27","K28","I27","I28","O26","O28","O30")
}


//player 6 rolls
function p6_skill(){
  function roll(mod_pos, roll_pos, final_pos) {
    var ui = SpreadsheetApp.getUi();
    var min = 1;
    var max = 21;
    var mod = SpreadsheetApp.getActiveSheet().getRange(mod_pos).getValue();
    var roll = Math.floor(Math.random() * (max - min)) + min; //The maximum is exclusive and the minimum is inclusive
    SpreadsheetApp.getActiveSheet().getRange(roll_pos).setValue(roll);
    var final = parseInt(mod) + roll
  
    SpreadsheetApp.getActiveSheet().getRange(final_pos).setValue(final);
  }
  roll("D33", "F32", "G32")
}

function p6_action(){
  function roll(mod_pos, roll_pos, final_pos, ap_pos, action_pos) {
    var ui = SpreadsheetApp.getUi();
    var min = 1;
    var max = 21;
    var action = SpreadsheetApp.getActiveSheet().getRange(action_pos).getValue();
    var mod = SpreadsheetApp.getActiveSheet().getRange(mod_pos).getValue();
    ui.alert(actions_dict[action]["Description"])
    
    //lower the ap
    var ap = SpreadsheetApp.getActiveSheet().getRange(ap_pos).getValue();

      ap = ap - actions_dict[action]["Speed"];
    
    SpreadsheetApp.getActiveSheet().getRange(ap_pos).setValue(ap);
    
    var roll = Math.floor(Math.random() * (max - min)) + min; //The maximum is exclusive and the minimum is inclusive
    SpreadsheetApp.getActiveSheet().getRange(roll_pos).setValue(roll);
    var final = parseInt(mod) + roll;
  
    SpreadsheetApp.getActiveSheet().getRange(final_pos).setValue(final);
  }
  roll("D35", "F34", "G34", "O32", "C35")
}

function p6_reaction(){
  function reaction_roll(react_name, mod_pos, roll_pos, final_pos, rp_pos) {
    var ui = SpreadsheetApp.getUi();
    var min = 1;
    var max = 21;
    var name = SpreadsheetApp.getActiveSheet().getRange(react_name).getValue();
    ui.alert(actions_dict[name]["Description"])
    if (name == "Block"|| name == "Dodge" || name == "Dive"){
      max = 7;
    }else{
      max = 21;
    }
    
    var ap = SpreadsheetApp.getActiveSheet().getRange(rp_pos).getValue();
    ap = ap - actions_dict[name]["Speed"];
    SpreadsheetApp.getActiveSheet().getRange(rp_pos).setValue(ap);
    
    var mod = SpreadsheetApp.getActiveSheet().getRange(mod_pos).getValue();
    var roll = Math.floor(Math.random() * (max - min)) + min; //The maximum is exclusive and the minimum is inclusive
    SpreadsheetApp.getActiveSheet().getRange(roll_pos).setValue(roll);
    var final = parseInt(mod) + roll
  
    SpreadsheetApp.getActiveSheet().getRange(final_pos).setValue(final);
  }
  reaction_roll("C37", "D37", "F36", "G36", "O34")
}

function p6_damage(){
  function damage(prime,wounded,bloodied){
    var ui = SpreadsheetApp.getUi();
    var hp_prime = SpreadsheetApp.getActiveSheet().getRange(prime).getValue();
    var hp_wounded = SpreadsheetApp.getActiveSheet().getRange(wounded).getValue();
    var hp_bloodied = SpreadsheetApp.getActiveSheet().getRange(bloodied).getValue();
    var broken = "X";
    
    if (hp_prime != broken && hp_prime > 0){
      hp_prime -= 1;
    }else if (hp_prime == 0){
      
      hp_prime = broken;
      hp_wounded -= 1;
      ui.alert("You broke your prime Stamina. Roll a d20 for your injury.");
    }else if (hp_wounded != broken && hp_wounded > 0){
      hp_wounded -= 1;
    }else if (hp_wounded == 0){
      
      hp_wounded = broken;
      hp_bloodied -= 1;
      ui.alert("You broke your core Stamina. Roll a d20 for your injury.");
    }else if (hp_bloodied != broken && hp_bloodied > 0){
      hp_bloodied -= 1;
    }else if (hp_bloodied == 0){
      
      hp_bloodied = broken;
      ui.alert("You are dying! Roll a Death Saving throw");      
    }else{
      ui.alert("Something is wrong with your HP, please reset and try again");
    }
    
    SpreadsheetApp.getActiveSheet().getRange(prime).setValue(String(hp_prime));
    SpreadsheetApp.getActiveSheet().getRange(wounded).setValue(String(hp_wounded));
    SpreadsheetApp.getActiveSheet().getRange(bloodied).setValue(String(hp_bloodied));
  }
  
  damage("M34", "K34", "I34")
}

//p6 heal button

function p6_stamina(){
  function stamina(prime_max, prime_hp, wounded_max, wounded_hp, bloodied_max, bloodied_hp, ap, rp, mp){
    var full = 6
    
    SpreadsheetApp.getActiveSheet().getRange(ap).setValue(String(full));
    SpreadsheetApp.getActiveSheet().getRange(rp).setValue(String(full));
    SpreadsheetApp.getActiveSheet().getRange(mp).setValue(String(full));
    var ui = SpreadsheetApp.getUi();
    var max_prime = SpreadsheetApp.getActiveSheet().getRange(prime_max).getValue();
    var hp_prime = SpreadsheetApp.getActiveSheet().getRange(prime_hp).getValue();
    var max_wounded = SpreadsheetApp.getActiveSheet().getRange(wounded_max).getValue();
    var hp_wounded = SpreadsheetApp.getActiveSheet().getRange(wounded_hp).getValue();
    var max_bloodied = SpreadsheetApp.getActiveSheet().getRange(bloodied_max).getValue();
    var hp_bloodied = SpreadsheetApp.getActiveSheet().getRange(bloodied_hp).getValue();
    var broken = "X";
    
    if (hp_prime != broken){
      hp_prime = max_prime;
      SpreadsheetApp.getActiveSheet().getRange(prime_hp).setValue(String(hp_prime));
    }else if (hp_wounded != broken){
      hp_wounded = max_wounded;
      SpreadsheetApp.getActiveSheet().getRange(wounded_hp).setValue(String(hp_wounded));
    }else if (hp_bloodied != broken){
      hp_bloodied = max_bloodied;
      SpreadsheetApp.getActiveSheet().getRange(bloodied_hp).setValue(String(hp_bloodied));
    }else if (hp_bloodied == broken){
      ui.alert("You can not recover when you are dying.")
    }else{
      ui.alert("Something is wrong with your HP, please reset and try again");
    }    
    
  }
  stamina("M33","M34","K33","K34","I33","I34","O32","O34","O36")
}


//player 7 rolls

function p7_skill(){
  function roll(mod_pos, roll_pos, final_pos) {
    var ui = SpreadsheetApp.getUi();
    var min = 1;
    var max = 21;
    var mod = SpreadsheetApp.getActiveSheet().getRange(mod_pos).getValue();
    var roll = Math.floor(Math.random() * (max - min)) + min; //The maximum is exclusive and the minimum is inclusive
    SpreadsheetApp.getActiveSheet().getRange(roll_pos).setValue(roll);
    var final = parseInt(mod) + roll
  
    SpreadsheetApp.getActiveSheet().getRange(final_pos).setValue(final);
  }
  roll("D39", "F38", "G38")
}

function p7_action(){
  function roll(mod_pos, roll_pos, final_pos, ap_pos, action_pos) {
    var ui = SpreadsheetApp.getUi();
    var min = 1;
    var max = 21;
    var action = SpreadsheetApp.getActiveSheet().getRange(action_pos).getValue();
    var mod = SpreadsheetApp.getActiveSheet().getRange(mod_pos).getValue();
    ui.alert(actions_dict[action]["Description"])
    
    //lower the ap
    var ap = SpreadsheetApp.getActiveSheet().getRange(ap_pos).getValue();

      ap = ap - actions_dict[action]["Speed"];
    
    SpreadsheetApp.getActiveSheet().getRange(ap_pos).setValue(ap);
    
    var roll = Math.floor(Math.random() * (max - min)) + min; //The maximum is exclusive and the minimum is inclusive
    SpreadsheetApp.getActiveSheet().getRange(roll_pos).setValue(roll);
    var final = parseInt(mod) + roll;
  
    SpreadsheetApp.getActiveSheet().getRange(final_pos).setValue(final);
  }
  roll("D41", "F40", "G40", "O38", "C41")
}

function p7_reaction(){
  function reaction_roll(react_name, mod_pos, roll_pos, final_pos, rp_pos) {
    var ui = SpreadsheetApp.getUi();
    var min = 1;
    var max = 21;
    var name = SpreadsheetApp.getActiveSheet().getRange(react_name).getValue();
    ui.alert(actions_dict[name]["Description"])
    if (name == "Block"|| name == "Dodge" || name == "Dive"){
      max = 7;
    }else{
      max = 21;
    }
    
    var ap = SpreadsheetApp.getActiveSheet().getRange(rp_pos).getValue();
    ap = ap - actions_dict[name]["Speed"];
    SpreadsheetApp.getActiveSheet().getRange(rp_pos).setValue(ap);
    
    var mod = SpreadsheetApp.getActiveSheet().getRange(mod_pos).getValue();
    var roll = Math.floor(Math.random() * (max - min)) + min; //The maximum is exclusive and the minimum is inclusive
    SpreadsheetApp.getActiveSheet().getRange(roll_pos).setValue(roll);
    var final = parseInt(mod) + roll
  
    SpreadsheetApp.getActiveSheet().getRange(final_pos).setValue(final);
  }
  reaction_roll("C43", "D43", "F42", "G42", "O40")
}

function p7_damage(){
  function damage(prime,wounded,bloodied){
    var ui = SpreadsheetApp.getUi();
    var hp_prime = SpreadsheetApp.getActiveSheet().getRange(prime).getValue();
    var hp_wounded = SpreadsheetApp.getActiveSheet().getRange(wounded).getValue();
    var hp_bloodied = SpreadsheetApp.getActiveSheet().getRange(bloodied).getValue();
    var broken = "X";
    
    if (hp_prime != broken && hp_prime > 0){
      hp_prime -= 1;
    }else if (hp_prime == 0){
      
      hp_prime = broken;
      hp_wounded -= 1;
      ui.alert("You broke your prime Stamina. Roll a d20 for your injury.");
    }else if (hp_wounded != broken && hp_wounded > 0){
      hp_wounded -= 1;
    }else if (hp_wounded == 0){
      
      hp_wounded = broken;
      hp_bloodied -= 1;
      ui.alert("You broke your core Stamina. Roll a d20 for your injury.");
    }else if (hp_bloodied != broken && hp_bloodied > 0){
      hp_bloodied -= 1;
    }else if (hp_bloodied == 0){
      
      hp_bloodied = broken;
      ui.alert("You are dying! Roll a Death Saving throw");      
    }else{
      ui.alert("Something is wrong with your HP, please reset and try again");
    }
    
    SpreadsheetApp.getActiveSheet().getRange(prime).setValue(String(hp_prime));
    SpreadsheetApp.getActiveSheet().getRange(wounded).setValue(String(hp_wounded));
    SpreadsheetApp.getActiveSheet().getRange(bloodied).setValue(String(hp_bloodied));
  }
  
  damage("M40", "K40", "I40")
}

//p7 heal button

function p7_stamina(){
  function stamina(prime_max, prime_hp, wounded_max, wounded_hp, bloodied_max, bloodied_hp, ap, rp, mp){
    var full = 6
    
    SpreadsheetApp.getActiveSheet().getRange(ap).setValue(String(full));
    SpreadsheetApp.getActiveSheet().getRange(rp).setValue(String(full));
    SpreadsheetApp.getActiveSheet().getRange(mp).setValue(String(full));
    var ui = SpreadsheetApp.getUi();
    var max_prime = SpreadsheetApp.getActiveSheet().getRange(prime_max).getValue();
    var hp_prime = SpreadsheetApp.getActiveSheet().getRange(prime_hp).getValue();
    var max_wounded = SpreadsheetApp.getActiveSheet().getRange(wounded_max).getValue();
    var hp_wounded = SpreadsheetApp.getActiveSheet().getRange(wounded_hp).getValue();
    var max_bloodied = SpreadsheetApp.getActiveSheet().getRange(bloodied_max).getValue();
    var hp_bloodied = SpreadsheetApp.getActiveSheet().getRange(bloodied_hp).getValue();
    var broken = "X";
    
    if (hp_prime != broken){
      hp_prime = max_prime;
      SpreadsheetApp.getActiveSheet().getRange(prime_hp).setValue(String(hp_prime));
    }else if (hp_wounded != broken){
      hp_wounded = max_wounded;
      SpreadsheetApp.getActiveSheet().getRange(wounded_hp).setValue(String(hp_wounded));
    }else if (hp_bloodied != broken){
      hp_bloodied = max_bloodied;
      SpreadsheetApp.getActiveSheet().getRange(bloodied_hp).setValue(String(hp_bloodied));
    }else if (hp_bloodied == broken){
      ui.alert("You can not recover when you are dying.")
    }else{
      ui.alert("Something is wrong with your HP, please reset and try again");
    }    
    
  }
  stamina("M39","M40","K39","K40","I39","I40","O38","O40","O42")
}


//player 8 rolls

function p8_skill(){
  function roll(mod_pos, roll_pos, final_pos) {
    var ui = SpreadsheetApp.getUi();
    var min = 1;
    var max = 21;
    var mod = SpreadsheetApp.getActiveSheet().getRange(mod_pos).getValue();
    var roll = Math.floor(Math.random() * (max - min)) + min; //The maximum is exclusive and the minimum is inclusive
    SpreadsheetApp.getActiveSheet().getRange(roll_pos).setValue(roll);
    var final = parseInt(mod) + roll
  
    SpreadsheetApp.getActiveSheet().getRange(final_pos).setValue(final);
  }
  roll("D45", "F44", "G44")
}

function p8_action(){
  function roll(mod_pos, roll_pos, final_pos, ap_pos, action_pos) {
    var ui = SpreadsheetApp.getUi();
    var min = 1;
    var max = 21;
    var action = SpreadsheetApp.getActiveSheet().getRange(action_pos).getValue();
    var mod = SpreadsheetApp.getActiveSheet().getRange(mod_pos).getValue();
    ui.alert(actions_dict[action]["Description"])
    
    //lower the ap
    var ap = SpreadsheetApp.getActiveSheet().getRange(ap_pos).getValue();

      ap = ap - actions_dict[action]["Speed"];
    
    SpreadsheetApp.getActiveSheet().getRange(ap_pos).setValue(ap);
    
    var roll = Math.floor(Math.random() * (max - min)) + min; //The maximum is exclusive and the minimum is inclusive
    SpreadsheetApp.getActiveSheet().getRange(roll_pos).setValue(roll);
    var final = parseInt(mod) + roll;
  
    SpreadsheetApp.getActiveSheet().getRange(final_pos).setValue(final);
  }
  roll("D47", "F46", "G46", "O44", "C47")
}

function p8_reaction(){
  function reaction_roll(react_name, mod_pos, roll_pos, final_pos, rp_pos) {
    var ui = SpreadsheetApp.getUi();
    var min = 1;
    var max = 21;
    var name = SpreadsheetApp.getActiveSheet().getRange(react_name).getValue();
    ui.alert(actions_dict[name]["Description"])
    if (name == "Block"|| name == "Dodge" || name == "Dive"){
      max = 7;
    }else{
      max = 21;
    }
    
    var ap = SpreadsheetApp.getActiveSheet().getRange(rp_pos).getValue();
    ap = ap - actions_dict[name]["Speed"];
    SpreadsheetApp.getActiveSheet().getRange(rp_pos).setValue(ap);
    
    var mod = SpreadsheetApp.getActiveSheet().getRange(mod_pos).getValue();
    var roll = Math.floor(Math.random() * (max - min)) + min; //The maximum is exclusive and the minimum is inclusive
    SpreadsheetApp.getActiveSheet().getRange(roll_pos).setValue(roll);
    var final = parseInt(mod) + roll
  
    SpreadsheetApp.getActiveSheet().getRange(final_pos).setValue(final);
  }
  reaction_roll("C49", "D49", "F48", "G48", "O46")
}

function p8_damage(){
  function damage(prime,wounded,bloodied){
    var ui = SpreadsheetApp.getUi();
    var hp_prime = SpreadsheetApp.getActiveSheet().getRange(prime).getValue();
    var hp_wounded = SpreadsheetApp.getActiveSheet().getRange(wounded).getValue();
    var hp_bloodied = SpreadsheetApp.getActiveSheet().getRange(bloodied).getValue();
    var broken = "X";
    
    if (hp_prime != broken && hp_prime > 0){
      hp_prime -= 1;
    }else if (hp_prime == 0){
      
      hp_prime = broken;
      hp_wounded -= 1;
      ui.alert("You broke your prime Stamina. Roll a d20 for your injury.");
    }else if (hp_wounded != broken && hp_wounded > 0){
      hp_wounded -= 1;
    }else if (hp_wounded == 0){
      
      hp_wounded = broken;
      hp_bloodied -= 1;
      ui.alert("You broke your core Stamina. Roll a d20 for your injury.");
    }else if (hp_bloodied != broken && hp_bloodied > 0){
      hp_bloodied -= 1;
    }else if (hp_bloodied == 0){
      
      hp_bloodied = broken;
      ui.alert("You are dying! Roll a Death Saving throw");      
    }else{
      ui.alert("Something is wrong with your HP, please reset and try again");
    }
    
    SpreadsheetApp.getActiveSheet().getRange(prime).setValue(String(hp_prime));
    SpreadsheetApp.getActiveSheet().getRange(wounded).setValue(String(hp_wounded));
    SpreadsheetApp.getActiveSheet().getRange(bloodied).setValue(String(hp_bloodied));
  }
  
  damage("M46", "K46", "I46")
}

//p8 heal button

function p8_stamina(){
  function stamina(prime_max, prime_hp, wounded_max, wounded_hp, bloodied_max, bloodied_hp, ap, rp, mp){
    var full = 6
    
    SpreadsheetApp.getActiveSheet().getRange(ap).setValue(String(full));
    SpreadsheetApp.getActiveSheet().getRange(rp).setValue(String(full));
    SpreadsheetApp.getActiveSheet().getRange(mp).setValue(String(full));
    var ui = SpreadsheetApp.getUi();
    var max_prime = SpreadsheetApp.getActiveSheet().getRange(prime_max).getValue();
    var hp_prime = SpreadsheetApp.getActiveSheet().getRange(prime_hp).getValue();
    var max_wounded = SpreadsheetApp.getActiveSheet().getRange(wounded_max).getValue();
    var hp_wounded = SpreadsheetApp.getActiveSheet().getRange(wounded_hp).getValue();
    var max_bloodied = SpreadsheetApp.getActiveSheet().getRange(bloodied_max).getValue();
    var hp_bloodied = SpreadsheetApp.getActiveSheet().getRange(bloodied_hp).getValue();
    var broken = "X";
    
    if (hp_prime != broken){
      hp_prime = max_prime;
      SpreadsheetApp.getActiveSheet().getRange(prime_hp).setValue(String(hp_prime));
    }else if (hp_wounded != broken){
      hp_wounded = max_wounded;
      SpreadsheetApp.getActiveSheet().getRange(wounded_hp).setValue(String(hp_wounded));
    }else if (hp_bloodied != broken){
      hp_bloodied = max_bloodied;
      SpreadsheetApp.getActiveSheet().getRange(bloodied_hp).setValue(String(hp_bloodied));
    }else if (hp_bloodied == broken){
      ui.alert("You can not recover when you are dying.")
    }else{
      ui.alert("Something is wrong with your HP, please reset and try again");
    }    
    
  }
  stamina("M45","M46","K45","K46","I45","I46","O44","O46","O48")
}


//player 9 rolls

function p9_skill(){
  function roll(mod_pos, roll_pos, final_pos) {
    var ui = SpreadsheetApp.getUi();
    var min = 1;
    var max = 21;
    var mod = SpreadsheetApp.getActiveSheet().getRange(mod_pos).getValue();
    var roll = Math.floor(Math.random() * (max - min)) + min; //The maximum is exclusive and the minimum is inclusive
    SpreadsheetApp.getActiveSheet().getRange(roll_pos).setValue(roll);
    var final = parseInt(mod) + roll
  
    SpreadsheetApp.getActiveSheet().getRange(final_pos).setValue(final);
  }
  roll("D51", "F50", "G50")
}

function p9_action(){
  function roll(mod_pos, roll_pos, final_pos, ap_pos, action_pos) {
    var ui = SpreadsheetApp.getUi();
    var min = 1;
    var max = 21;
    var action = SpreadsheetApp.getActiveSheet().getRange(action_pos).getValue();
    var mod = SpreadsheetApp.getActiveSheet().getRange(mod_pos).getValue();
    ui.alert(actions_dict[action]["Description"])
    
    //lower the ap
    var ap = SpreadsheetApp.getActiveSheet().getRange(ap_pos).getValue();

      ap = ap - actions_dict[action]["Speed"];
    
    SpreadsheetApp.getActiveSheet().getRange(ap_pos).setValue(ap);
    
    var roll = Math.floor(Math.random() * (max - min)) + min; //The maximum is exclusive and the minimum is inclusive
    SpreadsheetApp.getActiveSheet().getRange(roll_pos).setValue(roll);
    var final = parseInt(mod) + roll;
  
    SpreadsheetApp.getActiveSheet().getRange(final_pos).setValue(final);
  }
  roll("D53", "F52", "G52", "O50", "C53")
}

function p9_reaction(){
  function reaction_roll(react_name, mod_pos, roll_pos, final_pos, rp_pos) {
    var ui = SpreadsheetApp.getUi();
    var min = 1;
    var max = 21;
    var name = SpreadsheetApp.getActiveSheet().getRange(react_name).getValue();
    ui.alert(actions_dict[name]["Description"])
    if (name == "Block"|| name == "Dodge" || name == "Dive"){
      max = 7;
    }else{
      max = 21;
    }
    
    var ap = SpreadsheetApp.getActiveSheet().getRange(rp_pos).getValue();
    ap = ap - actions_dict[name]["Speed"];
    SpreadsheetApp.getActiveSheet().getRange(rp_pos).setValue(ap);
    
    var mod = SpreadsheetApp.getActiveSheet().getRange(mod_pos).getValue();
    var roll = Math.floor(Math.random() * (max - min)) + min; //The maximum is exclusive and the minimum is inclusive
    SpreadsheetApp.getActiveSheet().getRange(roll_pos).setValue(roll);
    var final = parseInt(mod) + roll
  
    SpreadsheetApp.getActiveSheet().getRange(final_pos).setValue(final);
  }
  reaction_roll("C55", "D55", "F54", "G54","O52")
}

function p9_damage(){
  function damage(prime,wounded,bloodied){
    var ui = SpreadsheetApp.getUi();
    var hp_prime = SpreadsheetApp.getActiveSheet().getRange(prime).getValue();
    var hp_wounded = SpreadsheetApp.getActiveSheet().getRange(wounded).getValue();
    var hp_bloodied = SpreadsheetApp.getActiveSheet().getRange(bloodied).getValue();
    var broken = "X";
    
    if (hp_prime != broken && hp_prime > 0){
      hp_prime -= 1;
    }else if (hp_prime == 0){
      
      hp_prime = broken;
      hp_wounded -= 1;
      ui.alert("You broke your prime Stamina. Roll a d20 for your injury.");
    }else if (hp_wounded != broken && hp_wounded > 0){
      hp_wounded -= 1;
    }else if (hp_wounded == 0){
      
      hp_wounded = broken;
      hp_bloodied -= 1;
      ui.alert("You broke your core Stamina. Roll a d20 for your injury.");
    }else if (hp_bloodied != broken && hp_bloodied > 0){
      hp_bloodied -= 1;
    }else if (hp_bloodied == 0){
      
      hp_bloodied = broken;
      ui.alert("You are dying! Roll a Death Saving throw");      
    }else{
      ui.alert("Something is wrong with your HP, please reset and try again");
    }
    
    SpreadsheetApp.getActiveSheet().getRange(prime).setValue(String(hp_prime));
    SpreadsheetApp.getActiveSheet().getRange(wounded).setValue(String(hp_wounded));
    SpreadsheetApp.getActiveSheet().getRange(bloodied).setValue(String(hp_bloodied));
  }
  
  damage("M52", "K52", "I52")
}

//p9 heal button

function p9_stamina(){
  function stamina(prime_max, prime_hp, wounded_max, wounded_hp, bloodied_max, bloodied_hp, ap, rp, mp){
    var full = 6
    
    SpreadsheetApp.getActiveSheet().getRange(ap).setValue(String(full));
    SpreadsheetApp.getActiveSheet().getRange(rp).setValue(String(full));
    SpreadsheetApp.getActiveSheet().getRange(mp).setValue(String(full));
    var ui = SpreadsheetApp.getUi();
    var max_prime = SpreadsheetApp.getActiveSheet().getRange(prime_max).getValue();
    var hp_prime = SpreadsheetApp.getActiveSheet().getRange(prime_hp).getValue();
    var max_wounded = SpreadsheetApp.getActiveSheet().getRange(wounded_max).getValue();
    var hp_wounded = SpreadsheetApp.getActiveSheet().getRange(wounded_hp).getValue();
    var max_bloodied = SpreadsheetApp.getActiveSheet().getRange(bloodied_max).getValue();
    var hp_bloodied = SpreadsheetApp.getActiveSheet().getRange(bloodied_hp).getValue();
    var broken = "X";
    
    if (hp_prime != broken){
      hp_prime = max_prime;
      SpreadsheetApp.getActiveSheet().getRange(prime_hp).setValue(String(hp_prime));
    }else if (hp_wounded != broken){
      hp_wounded = max_wounded;
      SpreadsheetApp.getActiveSheet().getRange(wounded_hp).setValue(String(hp_wounded));
    }else if (hp_bloodied != broken){
      hp_bloodied = max_bloodied;
      SpreadsheetApp.getActiveSheet().getRange(bloodied_hp).setValue(String(hp_bloodied));
    }else if (hp_bloodied == broken){
      ui.alert("You can not recover when you are dying.")
    }else{
      ui.alert("Something is wrong with your HP, please reset and try again");
    }    
    
  }
  stamina("M51","M52","K51","K52","I51","I52","O50","O52","O54")
}

// player 10 rolls

function p10_skill(){
  function roll(mod_pos, roll_pos, final_pos) {
    var ui = SpreadsheetApp.getUi();
    var min = 1;
    var max = 21;
    var mod = SpreadsheetApp.getActiveSheet().getRange(mod_pos).getValue();
    var roll = Math.floor(Math.random() * (max - min)) + min; //The maximum is exclusive and the minimum is inclusive
    SpreadsheetApp.getActiveSheet().getRange(roll_pos).setValue(roll);
    var final = parseInt(mod) + roll
  
    SpreadsheetApp.getActiveSheet().getRange(final_pos).setValue(final);
  }
  roll("D57", "F56", "G56")
}

function p10_action(){
  function roll(mod_pos, roll_pos, final_pos, ap_pos, action_pos) {
    var ui = SpreadsheetApp.getUi();
    var min = 1;
    var max = 21;
    var action = SpreadsheetApp.getActiveSheet().getRange(action_pos).getValue();
    var mod = SpreadsheetApp.getActiveSheet().getRange(mod_pos).getValue();
    ui.alert(actions_dict[action]["Description"])
    
    //lower the ap
    var ap = SpreadsheetApp.getActiveSheet().getRange(ap_pos).getValue();

      ap = ap - actions_dict[action]["Speed"];
    
    SpreadsheetApp.getActiveSheet().getRange(ap_pos).setValue(ap);
    
    var roll = Math.floor(Math.random() * (max - min)) + min; //The maximum is exclusive and the minimum is inclusive
    SpreadsheetApp.getActiveSheet().getRange(roll_pos).setValue(roll);
    var final = parseInt(mod) + roll;
  
    SpreadsheetApp.getActiveSheet().getRange(final_pos).setValue(final);
  }
  roll("D59", "F58", "G58", "O56", "C59")
}

function p10_reaction(){
  function reaction_roll(react_name, mod_pos, roll_pos, final_pos, rp_pos) {
    var ui = SpreadsheetApp.getUi();
    var min = 1;
    var max = 21;
    var name = SpreadsheetApp.getActiveSheet().getRange(react_name).getValue();
    ui.alert(actions_dict[name]["Description"])
    if (name == "Block"|| name == "Dodge" || name == "Dive"){
      max = 7;
    }else{
      max = 21;
    }
    
    var ap = SpreadsheetApp.getActiveSheet().getRange(rp_pos).getValue();
    ap = ap - actions_dict[name]["Speed"];
    SpreadsheetApp.getActiveSheet().getRange(rp_pos).setValue(ap);
    
    var mod = SpreadsheetApp.getActiveSheet().getRange(mod_pos).getValue();
    var roll = Math.floor(Math.random() * (max - min)) + min; //The maximum is exclusive and the minimum is inclusive
    SpreadsheetApp.getActiveSheet().getRange(roll_pos).setValue(roll);
    var final = parseInt(mod) + roll
  
    SpreadsheetApp.getActiveSheet().getRange(final_pos).setValue(final);
  }
  reaction_roll("C61", "D61", "F60", "G60", "O58")
}

function p10_damage(){
  function damage(prime,wounded,bloodied){
    var ui = SpreadsheetApp.getUi();
    var hp_prime = SpreadsheetApp.getActiveSheet().getRange(prime).getValue();
    var hp_wounded = SpreadsheetApp.getActiveSheet().getRange(wounded).getValue();
    var hp_bloodied = SpreadsheetApp.getActiveSheet().getRange(bloodied).getValue();
    var broken = "X";
    
    if (hp_prime != broken && hp_prime > 0){
      hp_prime -= 1;
    }else if (hp_prime == 0){
      
      hp_prime = broken;
      hp_wounded -= 1;
      ui.alert("You broke your prime Stamina. Roll a d20 for your injury.");
    }else if (hp_wounded != broken && hp_wounded > 0){
      hp_wounded -= 1;
    }else if (hp_wounded == 0){
      
      hp_wounded = broken;
      hp_bloodied -= 1;
      ui.alert("You broke your core Stamina. Roll a d20 for your injury.");
    }else if (hp_bloodied != broken && hp_bloodied > 0){
      hp_bloodied -= 1;
    }else if (hp_bloodied == 0){
      
      hp_bloodied = broken;
      ui.alert("You are dying! Roll a Death Saving throw");      
    }else{
      ui.alert("Something is wrong with your HP, please reset and try again");
    }
    
    SpreadsheetApp.getActiveSheet().getRange(prime).setValue(String(hp_prime));
    SpreadsheetApp.getActiveSheet().getRange(wounded).setValue(String(hp_wounded));
    SpreadsheetApp.getActiveSheet().getRange(bloodied).setValue(String(hp_bloodied));
  }
  
  damage("M58", "K58", "I58")
}

//p10 heal button

function p10_stamina(){
  function stamina(prime_max, prime_hp, wounded_max, wounded_hp, bloodied_max, bloodied_hp, ap, rp, mp){
    var full = 6
    
    SpreadsheetApp.getActiveSheet().getRange(ap).setValue(String(full));
    SpreadsheetApp.getActiveSheet().getRange(rp).setValue(String(full));
    SpreadsheetApp.getActiveSheet().getRange(mp).setValue(String(full));
    var ui = SpreadsheetApp.getUi();
    var max_prime = SpreadsheetApp.getActiveSheet().getRange(prime_max).getValue();
    var hp_prime = SpreadsheetApp.getActiveSheet().getRange(prime_hp).getValue();
    var max_wounded = SpreadsheetApp.getActiveSheet().getRange(wounded_max).getValue();
    var hp_wounded = SpreadsheetApp.getActiveSheet().getRange(wounded_hp).getValue();
    var max_bloodied = SpreadsheetApp.getActiveSheet().getRange(bloodied_max).getValue();
    var hp_bloodied = SpreadsheetApp.getActiveSheet().getRange(bloodied_hp).getValue();
    var broken = "X";
    
    if (hp_prime != broken){
      hp_prime = max_prime;
      SpreadsheetApp.getActiveSheet().getRange(prime_hp).setValue(String(hp_prime));
    }else if (hp_wounded != broken){
      hp_wounded = max_wounded;
      SpreadsheetApp.getActiveSheet().getRange(wounded_hp).setValue(String(hp_wounded));
    }else if (hp_bloodied != broken){
      hp_bloodied = max_bloodied;
      SpreadsheetApp.getActiveSheet().getRange(bloodied_hp).setValue(String(hp_bloodied));
    }else if (hp_bloodied == broken){
      ui.alert("You can not recover when you are dying.")
    }else{
      ui.alert("Something is wrong with your HP, please reset and try again");
    }    
    
  }
  stamina("M57","M58","K57","K58","I57","I58","O56","O58","O60")
}


//player 11 rolls

function p11_skill(){
  function roll(mod_pos, roll_pos, final_pos) {
    var ui = SpreadsheetApp.getUi();
    var min = 1;
    var max = 21;
    var mod = SpreadsheetApp.getActiveSheet().getRange(mod_pos).getValue();
    var roll = Math.floor(Math.random() * (max - min)) + min; //The maximum is exclusive and the minimum is inclusive
    SpreadsheetApp.getActiveSheet().getRange(roll_pos).setValue(roll);
    var final = parseInt(mod) + roll
  
    SpreadsheetApp.getActiveSheet().getRange(final_pos).setValue(final);
  }
  roll("D63", "F62", "G62")
}

function p11_action(){
  function roll(mod_pos, roll_pos, final_pos, ap_pos, action_pos) {
    var ui = SpreadsheetApp.getUi();
    var min = 1;
    var max = 21;
    var action = SpreadsheetApp.getActiveSheet().getRange(action_pos).getValue();
    var mod = SpreadsheetApp.getActiveSheet().getRange(mod_pos).getValue();
    ui.alert(actions_dict[action]["Description"])
    
    //lower the ap
    var ap = SpreadsheetApp.getActiveSheet().getRange(ap_pos).getValue();

      ap = ap - actions_dict[action]["Speed"];
    
    SpreadsheetApp.getActiveSheet().getRange(ap_pos).setValue(ap);
    
    var roll = Math.floor(Math.random() * (max - min)) + min; //The maximum is exclusive and the minimum is inclusive
    SpreadsheetApp.getActiveSheet().getRange(roll_pos).setValue(roll);
    var final = parseInt(mod) + roll;
  
    SpreadsheetApp.getActiveSheet().getRange(final_pos).setValue(final);
  }
  roll("D65", "F64", "G64", "O62", "C65")
}

function p11_reaction(){
  function reaction_roll(react_name, mod_pos, roll_pos, final_pos, rp_pos) {
    var ui = SpreadsheetApp.getUi();
    var min = 1;
    var max = 21;
    var name = SpreadsheetApp.getActiveSheet().getRange(react_name).getValue();
    ui.alert(actions_dict[name]["Description"])
    if (name == "Block"|| name == "Dodge" || name == "Dive"){
      max = 7;
    }else{
      max = 21;
    }
    
    var ap = SpreadsheetApp.getActiveSheet().getRange(rp_pos).getValue();
    ap = ap - actions_dict[name]["Speed"];
    SpreadsheetApp.getActiveSheet().getRange(rp_pos).setValue(ap);
    
    var mod = SpreadsheetApp.getActiveSheet().getRange(mod_pos).getValue();
    var roll = Math.floor(Math.random() * (max - min)) + min; //The maximum is exclusive and the minimum is inclusive
    SpreadsheetApp.getActiveSheet().getRange(roll_pos).setValue(roll);
    var final = parseInt(mod) + roll
  
    SpreadsheetApp.getActiveSheet().getRange(final_pos).setValue(final);
  }
  reaction_roll("C67", "D67", "F66", "G66", "O62")
}

function p11_damage(){
  function damage(prime,wounded,bloodied){
    var ui = SpreadsheetApp.getUi();
    var hp_prime = SpreadsheetApp.getActiveSheet().getRange(prime).getValue();
    var hp_wounded = SpreadsheetApp.getActiveSheet().getRange(wounded).getValue();
    var hp_bloodied = SpreadsheetApp.getActiveSheet().getRange(bloodied).getValue();
    var broken = "X";
    
    if (hp_prime != broken && hp_prime > 0){
      hp_prime -= 1;
    }else if (hp_prime == 0){
      
      hp_prime = broken;
      hp_wounded -= 1;
      ui.alert("You broke your prime Stamina. Roll a d20 for your injury.");
    }else if (hp_wounded != broken && hp_wounded > 0){
      hp_wounded -= 1;
    }else if (hp_wounded == 0){
      
      hp_wounded = broken;
      hp_bloodied -= 1;
      ui.alert("You broke your core Stamina. Roll a d20 for your injury.");
    }else if (hp_bloodied != broken && hp_bloodied > 0){
      hp_bloodied -= 1;
    }else if (hp_bloodied == 0){
      
      hp_bloodied = broken;
      ui.alert("You are dying! Roll a Death Saving throw");      
    }else{
      ui.alert("Something is wrong with your HP, please reset and try again");
    }
    
    SpreadsheetApp.getActiveSheet().getRange(prime).setValue(String(hp_prime));
    SpreadsheetApp.getActiveSheet().getRange(wounded).setValue(String(hp_wounded));
    SpreadsheetApp.getActiveSheet().getRange(bloodied).setValue(String(hp_bloodied));
  }
  
  damage("M64", "K64", "I64")
}

//p11 heal button

function p11_stamina(){
  function stamina(prime_max, prime_hp, wounded_max, wounded_hp, bloodied_max, bloodied_hp, ap, rp, mp){
    var full = 6
    
    SpreadsheetApp.getActiveSheet().getRange(ap).setValue(String(full));
    SpreadsheetApp.getActiveSheet().getRange(rp).setValue(String(full));
    SpreadsheetApp.getActiveSheet().getRange(mp).setValue(String(full));
    var ui = SpreadsheetApp.getUi();
    var max_prime = SpreadsheetApp.getActiveSheet().getRange(prime_max).getValue();
    var hp_prime = SpreadsheetApp.getActiveSheet().getRange(prime_hp).getValue();
    var max_wounded = SpreadsheetApp.getActiveSheet().getRange(wounded_max).getValue();
    var hp_wounded = SpreadsheetApp.getActiveSheet().getRange(wounded_hp).getValue();
    var max_bloodied = SpreadsheetApp.getActiveSheet().getRange(bloodied_max).getValue();
    var hp_bloodied = SpreadsheetApp.getActiveSheet().getRange(bloodied_hp).getValue();
    var broken = "X";
    
    if (hp_prime != broken){
      hp_prime = max_prime;
      SpreadsheetApp.getActiveSheet().getRange(prime_hp).setValue(String(hp_prime));
    }else if (hp_wounded != broken){
      hp_wounded = max_wounded;
      SpreadsheetApp.getActiveSheet().getRange(wounded_hp).setValue(String(hp_wounded));
    }else if (hp_bloodied != broken){
      hp_bloodied = max_bloodied;
      SpreadsheetApp.getActiveSheet().getRange(bloodied_hp).setValue(String(hp_bloodied));
    }else if (hp_bloodied == broken){
      ui.alert("You can not recover when you are dying.")
    }else{
      ui.alert("Something is wrong with your HP, please reset and try again");
    }    
    
  }
  stamina("M63","M64","K63","K64","I63","I64","O62","O64","O66")
}
