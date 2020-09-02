import React from 'react'


export default function Input(props){
    const {label,type,name,placeholder,value,onChange,options} = props


    return(
        <div>
            <label>
                {label}


                {
                    type === 'text'

                    ?<input
                    type={type}
                    name={name}
                    placeholder={placeholder}
                    value={value}
                    onChange={onChange}
                    />

                    :<input 
                    type={type}
                    name={name}
                    onChange={onChange}
                    >
                        {
                            options.map(option =>{
                                return(
                                    <option key={option} value={option}>
                                        {option}
                                    </option>
                                )
                            })
                        }
                    </input>
                }
                
            </label>

        </div>
    )
}