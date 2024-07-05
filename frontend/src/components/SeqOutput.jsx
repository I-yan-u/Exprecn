import { useContext, useState, useEffect } from 'react';
import { formDataContext } from './FormDataContext';
import style from './css/SeqOutput.module.css'

function SeqOutput() {
    const { resultData } = useContext(formDataContext);
    const [result, setResult] = useState({});
    
    useEffect(() => {
        setResult(resultData);
        console.log('Result to render', resultData);
    }, [resultData]); // Only depend on resultData

    return (
        <section className={style.container}>
            {Object.keys(result).length >= 0 ? (
                <div>
                    <h3>Output</h3>
                    <pre>{JSON.stringify(result, null, 2)}</pre>
                </div>
            ) : (
                <p>Run Query</p>
            )}
        </section>
    );

}

export default SeqOutput;
