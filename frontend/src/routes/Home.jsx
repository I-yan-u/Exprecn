// import React from 'react'
import style from './css/Home.module.css'
import Dna1 from '../assets/logo.svg'

function Home() {
  return (
    <div className={style.container} >
        <div className={style.left}>
            <h1>Exprecn</h1>
        </div>
        <div className={style.right}>
            <img src={Dna1} alt="DNA1" />
        </div>
    </div>
  )
}

export default Home;