import axiosConf from '../../fe.config';
import { useRef, useContext, useState, useEffect } from 'react';
import style from './css/InputSequence.module.css'
import { formDataContext } from './FormDataContext';
import useFetchUser from './useFetchUser';
import PropTypes from 'prop-types'

function InputSequence({clear, onClearComplete}) {
    const codingRef = useRef();
    const removeCodingBut = useRef();
    const { formData, setResultData } = useContext(formDataContext);
    const [query, setTemplate] = useState('');
    const [coding, setCoding] = useState('');
    const [user] = useFetchUser();

    useEffect(() => {
        if (clear) {
            setTemplate('');
            setCoding('');
            if (codingRef.current) codingRef.current.value = '';
            if (removeCodingBut.current) removeCodingBut.current.disabled = true;
            onClearComplete();
        }
    }, [clear, onClearComplete]);

    const handleSubmit = async () => {
        const be_Data = {...formData, query, coding};
        console.log(be_Data);
        let token = localStorage.getItem('user');
        token = JSON.parse(token);
        let url;
        user ? url = '/user/run' : url = '/run';
        axiosConf.defaults.headers.common['Authorization'] = `Bearer ${token.token}`; // Fix line
        axiosConf.post(url, be_Data, {
            "headers": {
                "Authorization": `Bearer ${token.token}`,
            }
        })
        .then(response => {
            // console.log(response.data);
            setResultData(response.data);
        })
        .catch(error => {
            console.error(error);
        });
    }

    const showCoding = () => {
        if (codingRef.current && removeCodingBut.current) {
            codingRef.current.style.display = 'flex';
            removeCodingBut.current.removeAttribute('disabled');
            removeCodingBut.current.style.opacity = '1';
        }
    };

    const hideCoding = () => {
        if (codingRef.current && removeCodingBut.current) {
            codingRef.current.style.display = 'none';
            removeCodingBut.current.style.opacity = '0.5';
        }
        removeCodingBut.current.setAttribute('disabled', 'true');
    };

  return (
    <>
        <div className={style.container}>
            <div className={style.template}>
                <h3>Template Strand</h3>
                <textarea name="inTemplate" rows='5' className={style.inTemplate} onChange={e => setTemplate(e.target.value)}></textarea>
            </div>
            <div className={style.coding} ref={codingRef}>
                <h3>Coding Strand</h3>
                <textarea name="inTemplate" rows='5' className={style.inCoding} onChange={e => setCoding(e.target.value)}></textarea>
            </div>
            <div className={style.input_button}>
                <button onClick={showCoding}><span>Coding strand</span></button>
                <button onClick={hideCoding} ref={removeCodingBut} className={style.removeCoding}><span>Remove coding</span></button>
                <button onClick={handleSubmit}><span>Run</span></button>
            </div>
        </div>
    </>
  )
}

InputSequence.propTypes = {
    clear: PropTypes.bool,
    onClearComplete: PropTypes.func
}

export default InputSequence;