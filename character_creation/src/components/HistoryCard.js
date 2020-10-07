import React, {useState,useEffect} from 'react'
import Input from './Input'
import Select from './Select'
import {backgrounds} from '../data/backgrounds'

const backgroundWealth = []
const backgroundBonuses = {
    skill:[],
    renown:[],
    equipment:[],
    unfinishedBusiness:[]
}

for(let background in backgrounds){
    if(backgrounds[background].Type === "General"){
        backgroundWealth.push(background)
    }
}

function HistoryCard(props){
    const [backgroundList,setBackgroundList] = useState([])
    const [society,setSociety] = useState([])
    const [backgroundOptions, setBackgroundOptions] = useState(backgroundBonuses)
    const {questions,subquestions,updateCharacter,character} = props

    useEffect(() => {
        let societyArr = []
        for(let bkgrnd in backgrounds){
            if(backgrounds[bkgrnd].Type === "General"){
                societyArr.push(bkgrnd)
            }
        }
        setSociety(societyArr)
    },[])

    useEffect(() => {
        const backgroundArr = []
        for(let bkgrnd in backgrounds){
            if(backgrounds[bkgrnd].Type === character.society){
                backgroundArr.push(bkgrnd)
            }
        }

        setBackgroundList(backgroundArr)

    },[character.society])

    useEffect(() => {
        let newOptions = {skill:[],
            renown:[],
            equipment:[],
            unfinishedBusiness:[]
        }
        console.log("This is the blank initial state bonuses ===>",backgroundBonuses)
        console.log("These are the new options ===>",newOptions)
        console.log("These are the state background bonuses ===>",backgroundOptions)

        console.log(character.society)

        if(character.society !== ''){
            newOptions.skill.push(backgrounds[character.society]['Skill'])
            backgrounds[character.society].Renown.map(bonus => newOptions.renown.push(bonus))
            backgrounds[character.society]["Unfinished Business"].map(bonus => newOptions.unfinishedBusiness.push(bonus))
            backgrounds[character.society].Equipment.map(bonus => newOptions.equipment.push(bonus))
        }
        if(character.background !== ''){
            newOptions.skill.push(backgrounds[character.background]['Skill'])
            backgrounds[character.background].Renown.map(bonus => newOptions.renown.push(bonus))
            backgrounds[character.background]["Unfinished Business"].map(bonus => newOptions.unfinishedBusiness.push(bonus))
            backgrounds[character.background].Equipment.map(bonus => newOptions.equipment.push(bonus))
        }

        console.log("This is what the state will be set as ===>",newOptions)

        
        
        

        return () => {
            setBackgroundOptions(newOptions)
            newOptions = {
                skill:[],
                renown:[],
                equipment:[],
                unfinishedBusiness:[]
            }
        }

    },[character.society,character.background])
    


    return(
        <form>
            <h2>Your History</h2>
            <Select
                label={questions.society.label}
                name={questions.society.name}
                options={society}
                value={character.society}
                onChange={updateCharacter}
            
            />

            {
                character.society !== '' &&
                <div>
                    <Select
                        label={questions.background.label}
                        name={questions.background.name}
                        options={backgroundList}
                        value={character.background}
                        onChange={updateCharacter}
                    />
                </div>
            }

            {
                character.society !== '' &&
                <div>
                    <Input 
                        label={subquestions.skill_background.label}
                        type={subquestions.skill_background.type}
                        name={subquestions.skill_background.name}
                        options={backgroundOptions.skill}
                        onChange={updateCharacter}
                    />
                    <Input 
                        label={subquestions.renown_background.label}
                        type={subquestions.renown_background.type}
                        name={subquestions.renown_background.name}
                        options={backgroundOptions.renown}
                        onChange={updateCharacter}
                    />
                    <Input 
                        label={subquestions['unfinished_business'].label}
                        type={subquestions['unfinished_business'].type}
                        name={subquestions['unfinished_business'].name}
                        options={backgroundOptions.unfinishedBusiness}
                        onChange={updateCharacter}
                    />
                    <Input 
                        label={subquestions.equipment.label}
                        type={subquestions.equipment.type}
                        name={subquestions.equipment.name}
                        options={backgroundOptions.equipment}
                        onChange={updateCharacter}
                    />
                </div>
            }

            <Input
                label={questions.call_to_action.label}
                type={questions.call_to_action.type}
                name={questions.call_to_action.name}
                placeholder={questions.call_to_action.placeholder}
            />

            <Input
                label={questions.mission.label}
                type={questions.mission.type}
                name={questions.mission.name}
                placeholder={questions.mission.placeholder}
            />

        </form>
    )
}

export default HistoryCard