# Undiscovered RPG 

### Application Design

## Installation
Use the package manager [pip]() to install Undiscovered RPG
```bash
pip install UndiscoveredRPG
```

## Usage
```python
import UndiscoveredRPG as undiscovered
```

### Vision and Direction

Create a web app and eventually a mobile app to house and facilitate playing Undiscovered RPG

##### THE PROBLEM - ANTIQUATED SYSTEMS AND LIMITATIONS OF PEN AND PAPER GAMES
* I hope it is clear that I love pen and paper games. but there are some real difficulties. 
* How many potential players have been interested in playing but have been stuck with the question: "How do I find a group?"
* How many potential GMs have asked: "How do I find players?"
* How many players have downloaded illegal copies of materials because they didn't want to fork out the high price for starting materials and subsequent additional materials that cost upwards of $50 at times but only have 10-15 pages that are relevant to them.
*How many players don't improve because they only one or two players in the group have the handbooks and materials for the whole. 
* How many GMs have had to walk beginner players through the over wealth of introduction materials because they have analysis paralysis. 
* How many have noticed the great divide between beginner players and Advanced players in the community or their groups without a clear direction of how to fix it. 
* I could go on but I think it is starting to form a clear picture. 
* We want to create a revolutionary way of approaching table top roleplaying games that addresses and solves a vast majority of these concerns, and creates a truly immersive and interconnected community that draws all of its players together

##### OUR SOLUTION  
**MOBILE APP/COMMUNITY ENGAGEMENT DESIGN**
We are building an app with the vision and direction to guide the user experience. Each of these points is a simplified version of our vision so please ask questions of anything you want to know more about!
**App Features**
**Character Creation**
* The goal is to lower the ramp-up time from 90 min to 15 min. 
* The app will ask questions and guide players through character creation offering quick builds but also offering detailed specifics for those who prefer to look into more.
**Game Play**
* Simplified Player Character sheet and UI with options to automate the experience that can be added or taken away as players gain mastery of the game mechanics
* The goal being that a player with no previous experience could pick up and play the game
* Integrated GM UI that reacts to players and controls the player experience

* This will also have optional automation that will simplify the GM experience and lower the threshold for starting GMs
* Training modules and tips for players and GMs alike to bridge the great divide between beginner players and the experienced who have read all the rules
* Our goal is to create a path for new players to become intermediate as soon as possible

**Community**
* A shared MMO style world - Our version of the Adventures League will be playing in a shared world. There are rules in place for GMs to still have creative freedom, but the players can share a world and join factions with other players, trade, take part in world-changing events, and take part in competing quest lines. They can explore the world and add to the compendium shared by all. 
* The world is largely unexplored and its discovery will be based on the group's decisions 
* Open Community - Because of this, every group is listed in the community and they can gain fame and notoriety as well as have open invitations for new players
* Players interested in finding groups can reach out to groups with open invitations, ask for help to the community, and share their experiences
* Open Content addition - The world is unexplored and undefined. There is fame and rewards waiting for those who want to create and share new quests, art, factions, classes, special moves, creatures, locations, equipment, and much more. 
* Those who create content that becomes popular will have an opportunity to have it go from legend and myth to actual canonized rules and lore. 
* Single player Role playing - Those who don't want to or can't access the group play but would like to be a part of the world, can take up a role in the society. 
* Become a blacksmith, farmer, guard, judge, or one of many others,  and send real groups on quests to earn currency materials, tools and much more. 
* A GM will potentially have the ability to tell the players who walk into a tavern, which RPCs (Role Playing Characters) are gambling around the table and which shifty person is in the back live on the app, as well as facilitate conversations and quests for them. 

### Tasks and Resources

**Character Creation**
* Questionairre to guage player's level of understanding and separate them into a beginner's guide and an advanced guide
* Beginner's guide will give them a [class guide](https://docs.google.com/forms/d/1d5aDqzXIyccD5NrxcJnr2rpHsszFCkWUGOcTKCyDBfI/edit?usp=sharing) and the views and values [guide](https://docs.google.com/forms/d/1Jbe9KWW-3ZyiJHNYbLUOed8slKGYP7wHatHgfPOMk3w/edit?usp=sharing)
* Advanced guide will just jump to the character creation [guide](https://docs.google.com/forms/d/1gZW-EVN35fSsX2xEzSoiQyJUMBMVF6s1rf4Ajga7Yso/edit?usp=sharing)
* This should auto fill the character sheet out for you and give you a tutorial to walk you through finding what you need on the character sheet

**Character Sheet**
[Luciid chart diagram](https://www.lucidchart.com/invitations/accept/1285cef5-c4b1-4412-b5e5-64faa8fa15cd)

The character sheet is broken out into three different sections or pages, Role Playing, Combat, and Adventuring. Each section has the pertinant information for their 

#### Role Playing Page contains

* Basic information:
* Name - string from character input
* Combat_Class - string from class selection
* Race - string from race selection

Appearance:
* Eye_Color - string from character input
* Skin_Tone - string from character input
* Hair_Color - string from character input
* Size - int based on size options from race
* Weight int based on weight options from race
* Trademarks - string from character input

Views and values:
* Value_Self - string from character input
* View_Self - string from character input
* Value_Others - string from character input
* View_Others - string from character input
* Value_Society - string from character input
* View_Society - string from character input

Personality:
* Mission - string from character input
* Interests - string from character input
* Talents - string from character input
* Quirks - string from character input
* Fears - string from character input

Background:
* Family - string from character input
* Friends - string from character input
* Professional - string from character input
* Nemesis - string from character input
* Factions - string from character input
* Home - string from character input
* Profession - string from list of professions
* Skill - based on profession
* Race_Bonus - chosen based on race
* Story - string from character input



#### Combat Page Contains:

Combat variables:

Health:
* Max_Vitality - adjustable int start at 3 
* Current_Viitaliity - set at Max_Vitality until player selects to lower
* Tier_1 
* Tier_2 
* Tier_3 

Statuses: _if these are stage 0 they don't show on the page. When a player clicks the status, they will see a window to select a status and select stages_
* blinded_status_stage - adjustable int selected from status window
* burning_status_stage - adjustable int selected from status window
* crippled_arm_status_stage - adjustable int selected from status window
* crippled_leg_status_stage - adjustable int selected from status window
* deafened_status_stage - adjustable int selected from status window
* fatigued_status_stage - adjustable int selected from status window
* impaled_status_stage - adjustable int selected from status window
* captivated_status_stage - adjustable int selected from status window
* confused_status_stage - adjustable int selected from status window
* frightened_status_stage - adjustable int selected from status window
* stunned_status_stage - adjustable int selected from status window
* momentum_status_stage - adjustable int selected from status window
* prone_status_stage - adjustable int selected from status window
* restrained_status_stage - adjustable int selected from status window
* suffocating_status_stage - adjustable int selected from status window
* surprised_status_stage - iadjustable nt selected from status window
* charged_status_stage - adjustable int selected from status window
* enraged_status_stage - adjustable int selected from status window
* hastened_status_stage - adjustable int selected from status window
* petrified_status_stage - adjustable int selected from status window
* frozen_status_stage - adjustable int selected from status window

Combat Modifiers
* Attack_Bonus - int Skill Bonus + STR_MOD + Misc Bonuses
* Dodge_Bonus - int Skill Bonus + DEX_MOD + Armor Bonus
* Defend_Bonus - int Skill Bonus + CON_MOD + Armor Bonus
* Offensive_Ability - string Set from Class Selection
* Defensive_Ability - string Set from Class Selection
* Movement_Ability - string Set from Class Selection
* Specail_Ability - string Set from Class Selection
* Free_Movement - string Set from Armor
* AP - int Every turn starts at 12
* RP - int Every turn starts at 4
* Power_Rank - int start at 0
* Main_Hand - item object Weapon select during character creation
* Off_Hand - item object selected from list
* Utility - item object selected from list
* Armor - item object from armor select duuriing character creation

#### Adventuring Page Contains

Conditions: _if these are stage 0 they don't show on the page. When a player clicks the conditions, they will see a window to select a condition and select stages_
* bleeding_condition_stage - adjustable int selected from conditions window
* blinded_condition_stage - adjustable int selected from conditions window
* crippled_condition_stage - adjustable int selected from conditions window
* deafened_condition_stage - adjustable int selected from conditions window
* drowsy_condition_stage - adjustable int selected from conditions window
* fatigued_condition_stage - adjustable int selected from conditions window
* fractured_condition_stage - iadjustable nt selected from conditions window
* sickened_condition_stage - adjustable int selected from conditions window

* Short_Rest - int that increments with every short rest performed inbetween long rests

Equipment
* Carry_Weight - int based on STR mod + 5
* Backpack - dictionary that appends from character input
* Gold - adjustable int from character input
* Rations - adjustable int from character input
* Trusty Item - selection from dictionay of trusty items
* Kits - selection frrom dictionary of kits





#### Right Side Bar, Attributes and skills: _when minimized, it only shows attribuutes, clicking the attriibute will expand to see all skills and actions under the selected attribute_

* STR - adjustable int initiially set from attribute pool during character creation
* STR_Mod - int (attribute // 5) - 2
* DEX - adjustable int initiially set from attribute pool during character creation
* DEX_Mod - int (attribute // 5) - 2
* CON - adjustable int initiially set from attribute pool during character creation
* CON_Mod - int (attribute // 5) - 2
* INT - adjustable int initiially set from attribute pool during character creation
* INT_Mod - int (attribute // 5) - 2
* WIS - adjustable int initiially set from attribute pool during character creation
* WIS_MOD - int (attribute // 5) - 2
* CHA - adjustable int initiially set from attribute pool during character creation
* CHA_Mod - int (attribute // 5) - 2
* Muscle - adjustable int initiially set from skill pool during character creation
* Wrestle - adjustable int initiially set from skill pool during character creation
* Brawl - adjustable int initiially set from skill pool during character creation
* Leap - adjustable int initiially set from skill pool during character creation
* Lunge - adjustable int initiially set from skill pool during character creation
* Climb - adjustable int initiially set from skill pool during character creation
* Coordination - adjustable int initiially set from skill pool during character creation
* Finesse - adjustable int initiially set from skill pool during character creation
* Sleight_of_Hand - adjustable int initiially set from skill pool during character creation
* Stealth - adjustable int initiially set from skill pool during character creation
* Endurance - adjustable int initiially set from skill pool during character creation
* Concentration - adjustable int initiially set from skill pool during character creation
* Vitality - adjustable int initiially set from skill pool during character creation
* Academic - adjustable int initiially set from skill pool during character creation
* Arcana - adjustable int initiially set from skill pool during character creation
* Culture - adjustable int initiially set from skill pool during character creation
* Analyze - adjustable int initiially set from skill pool during character creation
* Nature - adjustable int initiially set from skill pool during character creation
* Aggressive - adjustable int initiially set from skill pool during character creation
* Suave - adjustable int initiially set from skill pool during character creation
* Diplomatic - adjustable int initiially set from skill pool during character creation
* Sincere - adjustable int initiially set from skill pool during character creation


#### Left Side Bar, special moves: _when minimized, it only shows titles (Roleplaying_Special_Moves...), clicking the title will expand to see all special abilities and actions under the selected title_ 


* Roleplaying_Special_Moves 
* Combat_Special_Move 
* Adventuring_Special_Moves 

## Combat Flow

[UML with Swimlanes](https://www.lucidchart.com/invitations/accept/118ed6d2-aac8-4f72-a2b3-e8b27545b983)

**Start the Combat**
* Start the combat Module
* Import the PC NPC and Creature for all of the characters. 
* Additionally, import the JSON reference objects for actions, materials, statuses, positions, weapons, armors, and classes
* Start the combat encounter by each player and each NPC rolling initiative and adding their MP to the equation. Then sort the list of all players from highest to lowest

**Start Round**
* start the round class
* Prompt the next player/GM in initiative order

**Start Turn**
* Start the Turn Class
* While the player has > 0 AP
    * if the player chooses to end their turn or runs out of AP end their turn
* Prompt the player to move or make actions
* if the player chooses to move, ask them where they want to move and prompt them with options and minus MP based on selection
* if the player chooses to make an action, trigger action class
 
    **Start Action**
* Start the action class
* Initialize the class from the action "Name" that was selected
* Assign all of the action.json elements of the selected action to the instance of the python class
* If the Action_Type is "DC", roll the d20 add the "Stat" and the "Skill" bonus from the character and push back to the GM to determine success
* Elif the Action_Type is "Roll" roll the d20 add the "Stat" and the "Skill" bonus from the character and determine effect from the Payload
* If the Action_Type is Contest, select the target for the action, roll the d20 add the "Stat" and the "Skill" bonus from the character, prompt the target to roll the d20 add the "Stat" and the "Skill" bonus from the their "Reaction section. Determine the victor and apply the effect
* If the Type is Special, create special actions for these 5 moves as python classes
* once the move is resolved, minus the AP from the targets and go back to the While loop
    **End Action Return to Turn**
        
* If the player is out of AP end their turn, if not, return to the loop

**End Turn Return to Round**

* When all combatants are finished with their turns, start the round loop over

* When all combatants on one side die or suspend combat, End Combat
   
