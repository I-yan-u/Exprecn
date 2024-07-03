import { useContext, useState, useEffect } from 'react';
import { formDataContext } from './FormDataContext';

function SeqOutput() {
    const { resultData } = useContext(formDataContext);
    const [result, setResult] = useState();
    
    useEffect(() => {
        setResult(resultData);
        console.log('Result to render', resultData);
    }, [resultData]); // Only depend on resultData

    return (
        <>
            {result ? (
                <div>
                    <h3>Output</h3>
                    <pre>{JSON.stringify(result, null, 2)}</pre>
                </div>
            ) : (
                <p>No result to display</p>
            )}
        </>
    );

}

export default SeqOutput;
