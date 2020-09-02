import React, {useState, useEffect}from 'react'
import {questions} from './data/question'
import {races} from './data/races'
import {backgrounds} from './data/backgrounds'
import Intro_Card from './Intro_Card'
import Input from './Input'
import Select from './Select'

const emptyForm = {
    name:'',
    race:'',
    subrace:'',
    trademark:'',
    quirk:'',
    adventuring_race:'',
    roleplaying_race:'',
    combat_race:'',
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

        setCharacter({
            ...character,
            [name]:value
        })
    }

    

    return(
        <div>
            <Intro_Card
                questions={questions.intro}
                subquestions={questions.race}
                updateCharacter={updateCharacter}
                character={character}
            />
        </div>
    )
}