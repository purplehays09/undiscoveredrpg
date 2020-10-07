import React from 'react'


export default function Input(props){
    const {label,type,name,placeholder,value,onChange,options} = props


    return(
        <div>
                {
                    type === 'text'

                    ?
                    <label>
                        {label}
                        <input
                            type={type}
                            name={name}
                            placeholder={placeholder}
                            value={value}
                            onChange={onChange}
                        />
                    </label>

                    :
                    <div>
                        <p>{label}</p>
                        {
                            options.map(option => {
                                return(
                                    <div>

                                    <input
                                        type={type}
                                        name={name}
                                        onChange={onChange}
                                        value={option}
                                    />
                                    <label htmlFor={name}>{option}</label>
                                </div>

                                )
                                
                            })

                        }


                    </div>
                    
                    

                }      

        </div>
    )
}