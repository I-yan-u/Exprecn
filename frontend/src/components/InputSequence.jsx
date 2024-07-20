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
    const [user, gToken] = useFetchUser();

    useEffect(() => {
        if (clear) {
            setTemplate('');
            setCoding('');
            if (codingRef.current) codingRef.current.value = '';
            if (removeCodingBut.current) removeCodingBut.current.disabled = true;
            codingRef.current.style.display = 'none';
            removeCodingBut.current.style.opacity = '0.5';
            onClearComplete();
        }
    }, [clear, onClearComplete]);

    const handleSubmit = async () => {
        const be_Data = {...formData, query, coding};
        console.log(be_Data);
        let url;
        axiosConf.defaults.headers.common['Authorization'] = '';
        if (user && gToken){
            url = '/user/run' ;
            axiosConf.defaults.headers.common['Authorization'] = `Bearer ${gToken.token}`;
        } else {
            url = '/run';
        }
        axiosConf.post(url, be_Data)
        .then(response => {
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
                <textarea value={query} name="inTemplate" rows='5' className={style.inTemplate} onChange={e => setTemplate(e.target.value)}></textarea>
            </div>
            <div className={style.coding} ref={codingRef}>
                <h3>Coding Strand</h3>
                <textarea value={coding} name="inTemplate" rows='5' className={style.inCoding} onChange={e => setCoding(e.target.value)}></textarea>
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