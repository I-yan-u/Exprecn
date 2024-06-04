// import React from 'react'
import style from './css/Header.module.css'
import logo from '../assets/genelogo2.svg'
import PageHeight from '../components/ScrollHandler';
import { Link } from 'react-router-dom';
import { useState, useEffect, useContext } from 'react';
import useFetchUser from '../components/useFetchUser';
import Profilelogo from '../assets/profile-circle.svg';
import PropTypes from 'prop-types'

function Header({bg}) {
  const [user] = useFetchUser();
  const height = useContext(PageHeight);
  const [isLogged, setIsLogged] = useState(false);

  const logOut = () => {
    if (isLogged === true) {
      localStorage.removeItem('user');
      window.location.href =  '/';
    }
  }

  const dropDown = () => {
    const drop = document.querySelector(`.${style.dropdown}`);
    if(drop.style.display === 'flex') {
      drop.style.display = 'none';
    } else {
      drop.style.display = 'flex';
    }
  }

  useEffect(() => {
    if (user) {
      setIsLogged(true);
    } else {
      setIsLogged(false);
    }
  }, [user]);

  return (
    <nav className={`${style.navbar} ${height > 70 ? style.set_bg : ''}`}>
      <div className={style.brand}>
        <img className={style.logo} src={logo} alt='logo' />
        <h2 className={!bg ? '' : style.bg_h2}>Exprecn</h2>
      </div>
      <ul className={style.links}>
        {
          isLogged ? (
            <>
              <li><Link className={`${style.link} ${bg ? style.darkFnt : ''}`} to="/">Home</Link></li>
              <li><Link className={`${style.link} ${bg ? style.darkFnt : ''}`} to="/exprecn">Exprecn</Link></li>
              <li><Link className={`${style.link} ${bg ? style.darkFnt : ''}`} to="/#About">About</Link></li>
              <li><Link className={`${style.link} ${bg ? style.darkFnt : ''}`} to="/#Contacts">Contacts</Link></li>
              <li className={style.dropd}>
                <img src={Profilelogo} alt='Profile logo' onClick={dropDown}/>
                <div className={style.dropdown}>
                  <Link className={style.dlink} to="/profile">Profile</Link>
                  <Link className={style.dlink} to="/history">History</Link>
                  <span className={style.dlink} onClick={logOut}>Log Out</span>
                </div>
              </li>
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

Header.propTypes = {
  bg: PropTypes.bool
}

export default Header;