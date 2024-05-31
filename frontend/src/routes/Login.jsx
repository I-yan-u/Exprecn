// import React from 'react'
import axios from 'axios';
import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import style from './css/login.module.css';

function Login() {
    const [user, setUser] = useState({});

    useEffect(() => {

    }, [])
  return (
    <section className={style.bg}>
        <div className={style.container}>
            <div className={style.left}>
            </div>
            <div className={style.right}>
                <div className={style.form}>
                    <h2>Login</h2>
                    <form>
                        <div className={style.inputBox}>
                            <input type="text" name="" required="required" />
                            <label>Username</label>
                        </div>
                        <div className={style.inputBox}>
                            <input type="password" name="" required="required" />
                            <label>Password</label>
                        </div>
                        <input type="submit" name="" value="Login" />
                        <p className={style.forget}>Forget Password?</p>
                        <p className={style.register}>Don&apos;t have an account? <Link to='/signin'>Register</Link></p>
                    </form>
                </div>
            </div>
        </div>
    </section>
  )
}

export default Login;