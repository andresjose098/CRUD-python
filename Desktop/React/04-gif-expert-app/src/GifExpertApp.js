import React, { useState } from 'react'
import { AddCategory } from './components/AddCategory'
import { GifGrid } from './components/GifGrid'


export const GifExpertApp = () => {
    
  //  const categories = ['One punch','samurai x','Dragon ball']
    
     const [categories, setcategories] = useState(['Dragon ball z'])
        

        // const handleAdd = () =>{
        //    setcategories([...categories,'andres'])
        //   // console.log(handleAdd)
        // }

     

    return (
    <>
        <h2>GifExpertApp</h2>
        <AddCategory setcategories={setcategories}/>
        <hr/>

        


        <ol>
                {    
                    categories.map((category)=>(
                
                    <GifGrid 
                    key={category}
                    category={category}/>
                    
                ))
            }
               
            
        </ol>
        
    </>
  )
}
