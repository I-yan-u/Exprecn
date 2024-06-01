// import React from 'react'
import axiosConf from '../../fe.config';
import { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import style from './css/login.module.css';
import Loading from '../components/Loading';

function Login() {
    // const [user, setUser] = useState({});
    const [email, setEmail] = useState('');
    const [pass, setPass] = useState('');
    const [Load, setLoading] = useState(false);
    const history = useNavigate();

    const handleClick = async (e) => {
        e.preventDefault();
        setLoading(true);
        const b64Data = btoa(`${email}:${pass}`);
        const data = `Basic ${b64Data}`;
        console.log(data);
        try {
            const response = await axiosConf.get('/login', {
                headers: {
                    'Authorization': data
                }
            });
            if (response.status === 200) {
                // setUser(response.data);
                localStorage.removeItem('user');
                localStorage.setItem('user', JSON.stringify(response.data));
                setLoading(false);
                history('/exprecn'); // Using React Router for navigation
            } else {
                throw new Error('Failed to login');
            }
        } catch (error) {
            setLoading(false);
            console.error(error);
            // Provide feedback to the user
            // alert('Login failed: ' + error.message);
        }
    };

  return (
    <section className={style.bg}>
        <div className={style.container}>
            <div className={style.left}>
                Image
                {Load ? <Loading /> : ''}
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