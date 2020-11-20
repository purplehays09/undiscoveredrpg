import React, {useState,useEffect} from 'react'
import Input from './Input'
import Select from './Select'
import {races} from '../data/races'

const baseRaces = []
let subraceList = []
const raceBonuses = {
    adventuring:[],
    roleplaying:[],
    combat:[]
}

for(let race in races){
    if(races[race].type === "General" || races[race].type === "Standard"){
        baseRaces.push(race)
    }
}



export const getOptions = (bodyObj, list, setSubList, bonusesObj) => {
    const newOptions = {...bonusesObj}
    setSubList([])
    
    
    if(bodyObj.main !== ''){
        const subOptions = []

        for(let option in list){

            if(list[option].type === bodyObj.main){
                subOptions.push(option)
            }
        }    
        setSubList(subOptions)


        for (let bonus in newOptions){

            list[bodyObj.main][bonus].map(option => {
                newOptions[bonus].push(option)
            })
        }
    }

    if(bodyObj.sub !== ''){
        console.log("before 'forloop'")
        for(let bonus in newOptions){
            console.log("inside for loop")
            list[bodyObj.sub][bonus].map(option => {
                console.log('subrace options ===>',option)
                newOptions[bonus].push(option)
            })
        }

    }
    
    console.log('newOptions ===>', newOptions)

    return newOptions
}

export default function IntroCard(props){
    const [subraces,setSubraces] = useState(subraceList)
    const [raceOptions, setRaceOptions] = useState(raceBonuses)
    const {questions,subquestions,updateCharacter,character} = props


    useEffect(() => {
        setRaceOptions(getOptions(character.race,races,setSubraces,{adventuring:[],roleplaying:[],combat:[]}))
        console.log("character.race ===>",character.race)
    },[character.race.main,character.race.sub])

    
    
    
    return(
        <form>
            <h2>Who are you?</h2>
            <Input 
                label={questions.name.label}
                type={questions.name.type}
                placeholder={questions.name.placeholder}
                name={questions.name.name}
                value={character.name}
                onChange={updateCharacter}
            />

            <div className='race form'>
                <h3>Fantasy Race</h3>
                <Select 
                    label={questions.race.label}
                    name={questions.race.name}
                    options={baseRaces}
                    value={character.race.main}
                    onChange={updateCharacter}
                />
                
                {
                    character.race.main !== '' &&
                    
                    races[character.race.main].type === "General" && 
                    <div>
                        <Select 
                            label={questions.subrace.label}
                            name={questions.subrace.name}
                            options={subraces}
                            value={character.race.sub}
                            onChange={updateCharacter}
                        />
                            
                    </div>
                    
                    
                }
              


                {
                    character.race.main.length > 1 &&
                    <div>
                    <Input 
                        label={subquestions.adventuring_race.label}
                        type={subquestions.adventuring_race.type}
                        name={subquestions.adventuring_race.name}
                        options={raceOptions.adventuring}
                        onChange={updateCharacter}
                    />

                    <Input 
                        label={subquestions.roleplaying_race.label}
                        type={subquestions.roleplaying_race.type}
                        name={subquestions.roleplaying_race.name}
                        options={raceOptions.roleplaying}
                        onChange={updateCharacter}
                    />
                            
                    <Input 
                        label={subquestions.combat_race.label}
                        type={subquestions.combat_race.type}
                        name={subquestions.combat_race.name}
                        options={raceOptions.combat}
                        onChange={updateCharacter}
                    />
                        </div>
                        
                        
                }
              


            </div>

            <h3>Personality Traits</h3>

            <div className='form'>
                <Input 
                    label={questions.trademark.label}
                    type={questions.trademark.type}
                    placeholder={questions.trademark.placeholder}
                    name={questions.trademark.name}
                    value={character.trademark}
                    onChange={updateCharacter}
                    />
                <Input 
                    label={questions.quirk.label}
                    type={questions.quirk.type}
                    placeholder={questions.quirk.placeholder}
                    name={questions.quirk.name}
                    value={character.quirk}
                    onChange={updateCharacter}
                    />
            </div>

            


        </form>
    )
}
                                                                        // useEffect(() => {
                                                                        //     const newSubraces = []
                                                                        //     const currentRace = character.race
                                                                        //     const currentSubrace = character.subrace
                                                                        //     const newOptions = {
                                                                        //         adventuring:[],
                                                                        //         roleplaying:[],
                                                                        //         combat:[]
                                                                        //     }
                                                                            
                                                                        //     if(currentRace !== ''){
                                                                        //         setRaceOptions(raceBonuses)
                                                                        //         races[currentRace].Adventuring.map(bonus => {
                                                                        //             newOptions.adventuring.push(bonus)
                                                                        //         })
                                                                        //         races[currentRace].Roleplaying.map(bonus => {
                                                                        //             newOptions.roleplaying.push(bonus)
                                                                    
                                                                        //         })
                                                                        //         races[currentRace].Combat.map(bonus => {
                                                                        //             newOptions.combat.push(bonus)
                                                                    
                                                                        //         })
                                                                    
                                                                        //         if(currentSubrace !== ''){
                                                                    
                                                                        //             races[currentSubrace].Adventuring.map(bonus => {
                                                                        //                 newOptions.adventuring.push(bonus)
                                                                        //             })
                                                                        //             races[currentSubrace].Roleplaying.map(bonus => {
                                                                        //                 newOptions.roleplaying.push(bonus)
                                                                        
                                                                        //             })
                                                                        //             races[currentSubrace].Combat.map(bonus => {
                                                                        //                 newOptions.combat.push(bonus)
                                                                        
                                                                        //             })
                                                                                    
                                                                        //         }
                                                                    
                                                                    
                                                                        //         setRaceOptions(newOptions)
                                                                        //     }
                                                                    
                                                                            
                                                                    
                                                                        //     for(let race in races){
                                                                                
                                                                        //         if(races[race].Type === currentRace){
                                                                        //             newSubraces.push(race)
                                                                        //         }
                                                                        //     }
                                                                    
                                                                    
                                                                        //     setSubraces(newSubraces)
                                                                        // },[character.race,character.subrace])