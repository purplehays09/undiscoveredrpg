import React from 'react'


export default function Select(props){
    const {label,name,options,onChange} = props



    return(
        <div>
            <label>
                {label}

                <select
                    name={name}
                    onChange={onChange}
                >
                    <option value=''>Select {name}</option>
                    {
                        options.map(option => {
                            return(
                                <option key={option} value={option}>
                                    {option}
                                </option>
                            )
                        })
                    }
                </select>
            </label>
        </div>
    )
}