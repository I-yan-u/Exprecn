// import React from 'react'
import axios from 'axios';
import { useState } from 'react';
import { Link } from 'react-router-dom';
import style from './css/login.module.css';

function Login() {
    const [user, setUser] = useState({});
    const [email, setEmail] = useState('');
    const [pass, setPass] = useState('');

    const handleClick = async (e) => {
        e.preventDefault();
        axios.defaults.baseURL = 'http://localhost:5000/exprecn';
        axios.defaults.timeout = 50000;
        const b64Data = btoa(`${email}:${pass}`);
        const data = `Basic ${b64Data}`;
        console.log(data);
        try {
            const response = await axios.get('/login', {
                headers: {
                    'Authorization': data
                }
            });
            if (response.status === 200) {
                setUser(response.data);
                localStorage.setItem('user', JSON.stringify(user));
                window.location.href = '/exprecn';
            } else {
                throw new Error('Failed to login');
            }
        } catch (error) {
            console.error(error);
        }
    }

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
                            <input type="email" name="" required="required" onChange={e => setEmail(e.target.value)}/>
                            <label>Email address</label>
                        </div>
                        <div className={style.inputBox}>
                            <input type="password" name="" required="required" onChange={e => setPass(e.target.value)}/>
                            <label>Password</label>
                        </div>
                        <input type="submit" name="" value="Login" onClick={e => handleClick(e)}/>
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