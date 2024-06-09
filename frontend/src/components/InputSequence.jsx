import { useRef } from 'react';
import style from './css/InputSequence.module.css'

function InputSequence() {
    const codingRef = useRef();
    const removeCodingBut = useRef();

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
                <textarea name="inTemplate" rows='5' className={style.inTemplate}></textarea>
            </div>
            <div className={style.coding} ref={codingRef}>
                <h3>Coding Strand</h3>
                <textarea name="inTemplate" rows='5' className={style.inCoding}></textarea>
            </div>
            <div className={style.input_button}>
                <button onClick={showCoding}><span>Coding strand</span></button>
                <button onClick={hideCoding} ref={removeCodingBut} className={style.removeCoding}><span>Remove coding</span></button>
                <button><span>Run</span></button>
            </div>
        </div>
    </>
  )
}

export default InputSequence;