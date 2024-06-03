import axiosConf from '../../fe.config';
import { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import style from './css/Signin.module.css';
import Loading from '../components/Loading';
import Modal from '../layout/Modal';
import GeneImage from '../assets/DNA2.png';
import Warn from '../assets/warning.svg'

function Signin() {
    const [fname, setFname] = useState('');
    const [lname, setLname] = useState('');
    const [email, setEmail] = useState('');
    const [pass, setPass] = useState('');
    const [Load, setLoading] = useState(false);
    const [modal, setModalState] = useState(false);
    const [errorMessage, setErrorMessage] = useState(null);
    const history = useNavigate();

    const startWithCapital = (str) => {
        return str.charAt(0).toUpperCase() + str.slice(1);
    }

    const confirmPostData = (data) => {
        const passwordPattern = /^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[^\w\d\s:])([^\s]){8,16}$/gm;
        data.first_name = startWithCapital(data.first_name)
        data.last_name = startWithCapital(data.last_name)
        if (data.password !== data.confirm_password) {
            setErrorMessage(null);
            setErrorMessage(<><h2>Password Mismatch</h2><div>Passwords do not match</div></>);
            return;
        } else if (!passwordPattern.test(data.password)) {
            setErrorMessage(null);
            setErrorMessage(<>
                <h2>Invalid Pattern</h2>
                <div>Password must be between 8 to 16 characters and contain at least one lowercase letter,
                one uppercase letter,one numeric digit, and one special character</div>
            </>);
            return;
        } else {
            setErrorMessage(null);
            return data;
        }
    }

    const handleOpenModal = () => {
        setModalState(true);
    };

    const handleCloseModal = () => {
        setModalState(false);
    };

    const handleClick = async (e) => {
        e.preventDefault();
        handleOpenModal();
        setErrorMessage(null); 
        setLoading(true);

        const data = confirmPostData({
            first_name: fname,
            last_name: lname,
            email: email,
            password: pass,
            confirm_password: pass
        });
        delete data.confirm_password;
        console.log(data);
        if (!data) {
            return;
        }
        try {
            const response = await axiosConf.post('/users', data);
            if (response.status === 201) {
                setLoading(false);
                history('/login');
            } else {
                throw new Error('Failed to Sign In');
            }
        } catch (error) {
            setLoading(false);
            console.error(error);
            setErrorMessage(
                <>
                <h2>Sign In failed</h2> 
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
            errorMessage ?
            (
                modal && 
                <Modal onClose={handleCloseModal}>
                    <img src={Warn} alt="" />
                    {errorMessage}
                </Modal> ): ''
        }
    <div className={style.container}>
        <div className={style.left}>
            <img src={GeneImage} alt="Gene image" />
        </div>
        <div className={style.right}>
            <div className={style.form}>
                <h2>Sign In</h2>
                <form>
                    <div className={`${style.inputBox} ${style.inName1}`}>
                        <input type="text" name="" placeholder='First Name' required="required" onChange={e => setFname(e.target.value)}/>
                        <label>First Name</label>
                    </div>
                    <div className={`${style.inputBox} ${style.inName2}`}>
                        <input type="text" name="" placeholder='Last Name' required="required" onChange={e => setLname(e.target.value)}/>
                        <label>Last Name</label>
                    </div>
                    <div className={`${style.inputBox} ${style.inEmail}`}>
                        <input type="email" name="" placeholder='Email address' required="required" onChange={e => setEmail(e.target.value)}/>
                        <label>Email address</label>
                    </div>
                    <div className={`${style.inputBox} ${style.inPass1}`}>
                        <input type="password" name="" placeholder='Password' required="required" onChange={e => setPass(e.target.value)}/>
                        <label>Password</label>
                    </div>
                    <div className={`${style.inputBox} ${style.inPass2}`}>
                        <input type="password" name="" placeholder='Confirm Password' required="required" onChange={e => setPass(e.target.value)}/>
                        <label>Confirm Password</label>
                    </div>
                    <button className={style.submit} onClick={e => handleClick(e)}><span>Register</span></button>
                    <p className={style.forget}>Forget Password?</p>
                    <p className={style.register}>Already have an account? <Link to='/login'>Log In</Link></p>
                </form>
            </div>
        </div>
    </div>
</section>
  )
}

export default Signin;