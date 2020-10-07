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
    race:'',
    subrace:'',
    trademark:'',
    quirk:'',
    adventuring_race:'',
    roleplaying_race:'',
    combat_race:'',
    society:'',
    background:'',
    call_to_action:'',
    mission:'',
    skill_background:'',
    renown_background:'',
    equipment:[],
    unfinished_business:'',
    class:'',
    weapon:'',
    armor:'',
    options:[],
    subclass:[],
    highest:'',
    lowest:'',
    second_high:'',
    second_low:'',
    skills:[],
    values:[],
    principles:[]
}

export default function Dashboard(){
    const [character, setCharacter] = useState(emptyForm)

    const updateCharacter = (evt) => {
        const {name,value} = evt.target
        if(name === 'race'){
            console.log('pre change race: subrace ===>',character.subrace)
            setCharacter({
                ...character,
                subrace:'none'
            })
            console.log('post change race: subrace ===>',character.subrace)
        }
        setCharacter({
            ...character,
            [name]:value
        })
    }

    

    return(
        <div>
            <IntroCard
                questions={questions.intro}
                subquestions={questions.race}
                updateCharacter={updateCharacter}
                character={character}
            />
            
            <HistoryCard
                questions={questions.history}
                subquestions={questions.background}
                updateCharacter={updateCharacter}
                character={character}
            />
            
        </div>
    )
}