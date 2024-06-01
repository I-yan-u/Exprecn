// import React from 'react'
import style from './css/Header.module.css'
import logo from '../assets/genelogo2.svg'
import PageHeight from '../components/ScrollHandler';
import { Link } from 'react-router-dom';
import {  useContext } from 'react';
import useFetchUser from '../components/useFetchUser';

function Header() {
  const [user] = useFetchUser();
  const height = useContext(PageHeight);
  height > 50 ? console.log('scrolled') : console.log('not scrolled');

  return (
    <nav className={`${style.navbar} ${height > 70 ? style.set_bg : ''}`}>
      <div className={style.brand}>
        <img className={style.logo} src={logo} alt='logo' />
        <h2>Exprecn</h2>
      </div>
      <ul className={style.links}>
        {
          user ? (
            <>
              <li><Link className={style.link} to="/">Home</Link></li>
              <li><Link className={style.link} to="/exprecn">Exprecn</Link></li>
              <li><Link className={style.link} to="/profile">Profile</Link></li>
              <li><Link className={style.link} to="/history">History</Link></li>
            </>
          ) : (
            <>
              <li><Link className={style.link} to="/">Home</Link></li>
              <li><Link className={style.link} to="/exprecn">Exprecn</Link></li>
              <li><Link className={style.link} to="/login">Login</Link></li>
              <li><Link className={style.link} to="/signup">Signup</Link></li>
            </>
          )
        }
      </ul>
    </nav>
  )
}

export default Header;