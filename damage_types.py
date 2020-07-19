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