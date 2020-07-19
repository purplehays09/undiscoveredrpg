

# positions
positions_dict = {
    "Name":{
    "Description":"string",
    "Stage1": "string",
    "Stage2": "string",
    "Stage3": "string"
    },

    # add an attack direction mechanic 
    "Cover":{
        "Description":"Partly obscured from attacks",
        "Stage1": "\u2022 +5 reactions behind cover",
        "Stage2": "\u2022 +10 reactions behind cover",
        "Stage3": "\u2022 Cannot be targeted by attacks that require sight",
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

    #add attack direction
    "Flanked":{
        "Description":"Attacks from the target's peripherals or behind their view",
        "Stage1": "\u2022 Attacks against the target have a -1 Crit threshold",
        "Stage2": "\u2022 Attacks against the target have a -2 Crit threshold",
        "Stage3": "\u2022 Attacks against the target have a -5 Crit threshold",
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

        #I don't know, add a hidden from dictionary?
    "Hidden":{
        "Description":"Unable to be seen or unable to be targeted for attacks",
        "Stage1": "\u2022 First attack from hidden gives the target Surprised 1",
        "Stage2": "\u2022 First attack from hidden gives the target Surprised 2",
        "Stage3": "\u2022 First attack from hidden gives the target Surprised 3",
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

    #add elevation
    "High Ground":{
        "Description":"Being above the targets and gaining power behind attacks",
        "Stage1": "\u2022 Being above a target giving 1 stage of Momentum",
        "Stage2": "\u2022 Being above a target giving 2 stage of Momentum",
        "Stage3": "\u2022 Being above a target giving 3 stage of Momentum",
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

        #I don't fricken know until I add a map
    "Unbalanced":{
        "Description":"Being above the targets and gaining power behind attacks",
        "Stage1": "\u2022 Failed reactions give you a stage of Prone",
        "Stage2": "\u2022 Failed reactions give you a stage of Prone\n\u2022Every Physical Action against you can add a Shove Check for 0 AP",
        "Stage3": "\u2022 Failed reactions give you a stage of Prone\n\u2022Every Physical Action against you can add a Shove Check for 0 AP\n\u2022 Movement provokes a Trip action against you DC 15",
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