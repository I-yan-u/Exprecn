// import React from 'react'
import axiosConf from '../../fe.config';
import { useState, useRef } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import style from './css/login.module.css';
import Loading from '../components/Loading';
import Modal from '../layout/Modal';
import GeneImage from '../assets/DNA2.png';
import Warn from '../assets/warning.svg'
import Show from '../assets/show.svg'
import Hide from '../assets/hide.svg'

function Login() {
    const [email, setEmail] = useState('');
    const [pass, setPass] = useState('');
    const [Load, setLoading] = useState(false);
    const [modal, setModalState] = useState(false);
    const [message, setMessage] = useState(null);
    const [showPass, setShowPass] = useState(false);
    const passInRef = useRef();
    const history = useNavigate();

    const handleOpenModal = () => {
        setModalState(true);
    };

    const handleCloseModal = () => {
        setModalState(false);
    };

    const togglePassView = (e) => {
        const src = e.target.getAttribute('src');
        if(src === Show){
            setShowPass(true);
            e.target.setAttribute('src', Hide);
            passInRef.current.setAttribute('type', 'text');
        } else {
            setShowPass(false);
            e.target.setAttribute('src', Show);
            passInRef.current.setAttribute('type', 'password');
        }
    }

    const handleClick = async (e) => {
        e.preventDefault();
        handleOpenModal();
        setMessage(null); 
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
                localStorage.removeItem('user');
                localStorage.setItem('user', JSON.stringify(response.data));
                setLoading(false);
                history('/');
            } else {
                throw new Error('Failed to login');
            }
        } catch (error) {
            setLoading(false);
            handleOpenModal();
            console.error(error);
            setMessage(
            <>
            <h2>Login failed</h2> 
            <p>Code: {error.response.status}</p>
            <div>Datail: {error.response.data.message}</div>
            </>
        );
        }
    };

  return (
    <section className={style.bg}>
        {
            Load ? 
            (
                modal && 
                <Modal onClose={handleCloseModal}>
                    <Loading />
                </Modal> ) : ''
        }
        {
            message ?
            (
                modal && 
                <Modal onClose={handleCloseModal}>
                    <img src={Warn} alt="" />
                    {message}
                </Modal> ): ''
        }
        <div className={style.container}>
            <div className={style.left}>
                <img src={GeneImage} alt="Gene image" />
            </div>
            <div className={style.right}>
                <div className={style.form}>
                    <h2>Login</h2>
                    <form>
                        <div className={`${style.inputBox} ${style.inEmail}`}>
                            <input type="email" name="" required="required" placeholder='Email address' onChange={e => setEmail(e.target.value)}/>
                            <label>Email address</label>
                        </div>
                        <div className={`${style.inputBox} ${style.inPass} ${showPass ? style.showpass : ''}`}>
                            <input type="password" name="" ref={passInRef} required="required" placeholder='Password' onChange={e => setPass(e.target.value)}/>
                            <label>Password</label>
                            <img src={Show} onClick={e => togglePassView(e)} />
                        </div>
                        <button className={style.submit} onClick={e => handleClick(e)}><span>Login</span></button>
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