import React, {useState, useEffect}from 'react'
import {questions} from '../data/question'
// import {races} from '../data/races'
// import {backgrounds} from '../data/backgrounds'
import IntroCard from './IntroCard'
import HistoryCard from './HistoryCard'
// import Input from './Input'
// import Select from './Select'

const emptyForm = {
    name:'',
    race: {
        main:'',
        sub:'',
        bonuses:{
            adventuring:[],
            roleplaying:[],
            combat:[]
        }
    },
    trademark:'',
    quirk:'',
    background: {
        main:'',
        sub:'',
        bonuses:{
            skill:'',
            renown:'',
            unfinished_business:'',
            equipment:[]
        }
    },
    call_to_action:'',
    mission:'',
    class:{
        main:'',
        sub:'',
        bonuses:[]
    },
    weapon:'',
    armor:'',
    attributes:{
        highest:'',
        lowest:'',
        second_high:'',
        second_low:''
    },
    skills:[],
    values:[],
    // subrace:'',
    // adventuring_race:'',
    // roleplaying_race:'',
    // combat_race:'',
    // society:'',
    // background:'',
    // skill_background:'',
    // renown_background:'',
    // equipment:[],
    // unfinished_business:'',
    // options:[],
    // subclass:[],
    // highest:'',
    // lowest:'',
    // second_high:'',
    // second_low:'',
    // principles:[]
}

export default function Dashboard(){
    const [character, setCharacter] = useState(emptyForm)

    const updateCharacter = (evt) => {
        const {name,value} = evt.target
        if(name === 'race'){

            setCharacter({
                ...character,
                race:{
                    ...character.race,
                    main:value,
                    sub:''
                }
            })
        }else if(name === 'subrace'){


            setCharacter({
                ...character,
                race:{
                    ...character.race,
                    sub:value
                }
            })
        }else{
            console.log("you shouldn't be here")
            setCharacter({
                ...character,
                [name]:value
            })
        }
    }

    

    return(
        <div>
            <IntroCard
                questions={questions.intro}
                subquestions={questions.race}
                updateCharacter={updateCharacter}
                character={character}
            />
            
            {/* <HistoryCard
                questions={questions.history}
                subquestions={questions.background}
                updateCharacter={updateCharacter}
                character={character}
            /> */}
            
        </div>
    )
}