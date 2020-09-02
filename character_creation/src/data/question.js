
export const questions = {
    intro:{
        name:{
            label:"Hi, my name is:",
            type:"text",
            name:"name",
            placeholder:"Gidry Delthryn",
        },
        race:{
            label:"I belong to the race of:",
            type:"select",
            name:"race",
            placeholder:"",
        },
        subrace:{
            label:"My sub race is: ",
            type:"select",
            name:"subrace",
            placeholder:"",
        },
        trademark:{
            label:"The first thing others notice about my appearance is:",
            type:"text",
            name:"trademark",
            placeholder:"Pearly White Teeth",
        },
        quirk:{
            label:"I've heard that the oddest thing about my personality is:",
            type:"text",
            name:"quirk",
            placeholder:"I have to pee when I lie",
        }
    },
    race:{
        adventuring_race:{
            label:"While adventuring through the world, I lean on my racial skill of:",
            type:"radio",
            name:"adventuring",
            placeholder:"",
        },
        roleplaying_race:{
            label:"In conversations, I can rely on my racial skill of:",
            type:"radio",
            name:"roleplaying",
            placeholder:"",
        },
        combat_race:{
            label:"If a fight breaks out, I can always depend on my racial bonus:",
            type:"radio",
            name:"combat",
            placeholder:"",
        }
    },
    history:{
        background:{
            label:"Before I became an adventurer, I was a(n):",
            type:"select",
            name:"background",
            placeholder:"",
        },
        call_to_action:{
            label:"I left that life when _______ happened.",
            type:"text",
            name:"call_to_action",
            placeholder:"My home was burned by raiders.",
        },
        mission:{
            label:"My mission now is to:",
            type:"text",
            name:"mission",
            placeholder:"Avenge my family",
        }
    },
    background:{
        skill_background:{
            label:"I have picked up the ability to:",
            type:"radio",
            name:"background_skill",
            placeholder:"",
        },
        renown_background:{
            label:"I have a special renown with:",
            type:"radio",
            name:"renown",
            placeholder:"",
        },
        equipment:{
            label:"All I still have from that life are my:",
            type:"checkbox",
            name:"equipment",
            placeholder:"",
        },
        unfinished_business:{
            label:"I have unfinished business from my past:",
            type:"radio",
            name:"unfinished_business",
            placeholder:"",
        }
    },
    combat:{
        class:{
            label:"When a fight breaks out, I can rely on my skills as a:",
            type:"select",
            name:"class",
            placeholder:"",
        },
        weapon:{
            label:"My weapon I carry is:",
            type:"select",
            name:"weapon",
            placeholder:"",
        },
        armor:{
            label:"I usually wear armor in case of emergencies:",
            type:"select",
            name:"armor",
            placeholder:"",
        }
    },
    class:{
        options:{
            label:"My 3 class abilities are",
            type:"checkbox",
            name:"class_options",
            placeholder:"",
        },
        champion:{
            label:"As a defender, I carry a shield with me:",
            type:"select",
            name:"champion_shield",
            placeholder:"",
        },
        goliath:{
            label:"",
            type:"",
            name:"",
            placeholder:"",
        },
        ranger:{
            label:"Just in case, I always carry a:",
            type:"select",
            name:"ranger_utility",
            placeholder:"",
        },
        rogue:{
            label:"",
            type:"",
            name:"",
            placeholder:"",
        },
        druid:{
            hunter:{
                label:"My hunter form is:",
                type:"select",
                name:"hunter",
                placeholder:"",
                },
            sprinter:{
                label:"My sprinter form is:",
                type:"select",
                name:"sprinter",
                placeholder:"",
                },
            defender:{
                label:"My defender form is:",
                type:"select",
                name:"defender",
                placeholder:"",
                }
        },
        sorcerer:{
            label:"The element that I control is:",
            type:"select",
            name:"element",
            placeholder:"",
        },
        arcanist:{
            label:"The arcane art I specialize in is:",
            type:"select",
            name:"school",
            placeholder:"",
        }
    },
    attributes:{
        highest:{
            label:"My strongest attribute is:",
            type:"select",
            name:"highest",
            placeholder:"",
        },
        lowest:{
            label:"My weakest attribute is:",
            type:"select",
            name:"lowest",
            placeholder:"",
        },
        second_high:{
            label:"My back up attribute is:",
            type:"select",
            name:"second_high",
            placeholder:"",
        },
        second_low:{
            label:"My second weakest attribute is:",
            type:"select",
            name:"second_low",
            placeholder:"",
        },
        skills:{
            label:"I have some proficiency in these 6 skills:",
            type:"checkbox",
            name:"skills",
            placeholder:"",
        }
    },
    values:{
        values:{
            label:"The things I value in myself and the world are:",
            type:"checkbox",
            name:"values",
            placeholder:"",
        },
        principles:{
            label:"Because of this, my principle(s) are ",
            type:"text",
            name:"principles",
            placeholder:"I always fight to defend my honor",
        }
    }
    
}