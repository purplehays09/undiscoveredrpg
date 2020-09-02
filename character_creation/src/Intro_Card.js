import React, {useState,useEffect} from 'react'
import Input from './Input'
import Select from './Select'
import {races} from './data/races'

const baseRaces = []
let subraceList = []
const raceBonuses = {
    adventuring:[],
    roleplaying:[],
    combat:[]
}

for(let race in races){
    if(races[race].Type === "General" || races[race].Type === "Standard"){
        baseRaces.push(race)
    }
}




export default function Intro_Card(props){
    const [subraces,setSubraces] = useState(subraceList)
    const [raceOptions, setRaceOptions] = useState(raceBonuses)
    const {questions,subquestions,updateCharacter,character} = props

    useEffect(() => {
        const newSubraces = []
        debugger

        if(character.race !== ''){
            races[character.race].Adventuring.map(bonus => {
                setRaceOptions({
                    adventuring:[...raceOptions.adventuring,bonus]
                })
                return raceOptions
            })
            races[character.race].Roleplaying.map(bonus => {
                setRaceOptions({
                    roleplaying:[...raceOptions.roleplaying,bonus]
                })
                return raceOptions
            })
            races[character.race].Combat.map(bonus => {
                setRaceOptions({
                    combat:[...raceOptions.combat,bonus]
                })
                return raceOptions
            })
        }

        

        for(let race in races){
            
            if(races[race].Type === character.race){
                newSubraces.push(race)
            }
        }

        setSubraces(newSubraces)
    },[character.race])

    

    return(
        <form>
            <Input 
                label={questions.name.label}
                type={questions.name.type}
                placeholder={questions.name.placeholder}
                name={questions.name.name}
                value={character.name}
                onChange={updateCharacter}
            />

            <form>
                <h3>Fantasy Race</h3>
                <Select 
                    label={questions.race.label}
                    name={questions.race.name}
                    options={baseRaces}
                    value={character.race}
                    onChange={updateCharacter}
                />

                {
                    character.race !== '' &&
                    
                    races[character.race].Type === "General" && 
                    <Select 
                        label={questions.subrace.label}
                        name={questions.subrace.name}
                        options={subraces}
                        value={character.subrace}
                        onChange={updateCharacter}
                    />

                }
              


                {
                    character.race !== '' &&

                    <Input 
                        label={subquestions.adventuring_race.label}
                        type={subquestions.adventuring_race.type}
                        name={subquestions.adventuring_race.name}
                        options={raceOptions.adventuring}
                        onChange={updateCharacter}
                    />
                }
              


            </form>

            


        </form>
    )
}