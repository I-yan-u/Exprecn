// import React from 'react'
import style from './css/Header.module.css'
import logo from '../assets/genelogo2.svg'
import PageHeight from '../components/ScrollHandler';
import {  useContext } from 'react';

function Header() {
  const height = useContext(PageHeight);
  height > 50 ? console.log('scrolled') : console.log('not scrolled');

  return (
    <nav className={`${style.navbar}`}>
      <div className={style.brand} >
        <img className={style.logo} src={logo} alt='logo' />
        <h2>Exprecn</h2>
      </div>
      <ul className={style.links}>
        <li><a href="/">Home</a></li>
        <li><a href="/exprecn">Exprecn</a></li>
        <li><a href="/profile">Profile</a></li>
        <li><a href="/history">History</a></li>
      </ul>
    </nav>
  )
}

export default Header;