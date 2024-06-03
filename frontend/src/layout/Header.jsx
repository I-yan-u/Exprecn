// import React from 'react'
import style from './css/Header.module.css'
import logo from '../assets/genelogo2.svg'
import PageHeight from '../components/ScrollHandler';
import { Link } from 'react-router-dom';
import { useState, useEffect, useContext } from 'react';
import useFetchUser from '../components/useFetchUser';
import Profilelogo from '../assets/profile-circle.svg';

function Header() {
  const [user] = useFetchUser();
  const height = useContext(PageHeight);
  const [isLogged, setIsLogged] = useState(false);

  const logOut = () => {
    if (isLogged === true) {
      localStorage.removeItem('user');
      window.location.href =  '/';
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
        <h2>Exprecn</h2>
      </div>
      <ul className={style.links}>
        {
          isLogged ? (
            <>
              <li><Link className={style.link} to="/">Home</Link></li>
              <li><Link className={style.link} to="/exprecn">Exprecn</Link></li>
              <li><Link className={style.link} to="/#About">About</Link></li>
              <li><Link className={style.link} to="/#Contacts">Contacts</Link></li>
              <li>
                <img src={Profilelogo} alt='Profile logo'/>
                <div className={style.dropdown}>
                  <li><Link className={style.dlink} to="/profile">Profile</Link></li>
                  <li><Link className={style.dlink} to="/history">History</Link></li>
                  <li><span className={style.dlink} onClick={logOut}>History</span></li>
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

export default Header;