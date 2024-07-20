import { useContext, useState, useEffect } from 'react';
import { formDataContext } from './FormDataContext';
import style from './css/SeqOutput.module.css'
import ResultListView from './ResultListView';

function SeqOutput() {
    const { resultData } = useContext(formDataContext);
    const [result, setResult] = useState({});
    const [navState, setNavState] = useState('raw');
    
    useEffect(() => {
        setResult(resultData);
        console.log('Result to render', resultData);
    }, [resultData]); // Only depend on resultData

    const renderSwitch = (navState) => {
        switch (navState) {
            case 'list':
                console.log('test: \n', result)
                return <ResultListView result={result} />
            case 'table':
                return <div>Table View</div>; // Replace with your actual table view component
            default:
                return (
                    <div>
                        <pre>{JSON.stringify(result, null, 2)}</pre>
                    </div>
                );
        }
    };

    const getNavClass = () => {
        switch (navState) {
            case 'list':
                return style.navList;
            case 'table':
                return style.navTable;
            default:
                return '';
        }
    };

    return (
        <section className={style.container}>
            {Object.keys(resultData).length >= 1 ? (
                <>
                    <nav className={`${style.navbar} ${getNavClass()}`}>
                        <li onClick={() => setNavState('raw')}>Raw</li>
                        <li onClick={() => setNavState('list')}>List</li>
                        <li onClick={() => setNavState('table')}>Table</li>
                    </nav>
                    {renderSwitch(navState)}
                </>
            ) : (
                <p>Run Query</p>
            )}
        </section>
    );

}

export default SeqOutput;
