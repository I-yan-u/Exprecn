// import React from 'react'
import style from './css/ResultListView.module.css';
import PropTypes from 'prop-types';

function ResultListView({result}) {
  return (
    <div className={style.listView}>
        {
            result.obj ?
            <>
                <li><span>Action: </span>{result.action}</li>
                <li><span>Type: </span>{result.obj._Exprecn__NucleicAcid}</li>
                <li><span>Strands: </span>{result.obj._Exprecn__strands}</li>
                <li><span>Template: </span>{result.obj.template}</li>
                <li><span>Coding: </span>{result.obj.coding}</li>
                <li><span>Options: </span>{
                    Object.keys(result.options).length > 1 ? 
                        Object.keys(result.options).map((key, index) => {
                            return <li key={index}><span>{key}: </span>{result.options[key]}</li>
                        }) : <li><span>: </span></li>
                }
                </li>
                <li><span>Result: </span>{result.result}</li>
            </>
            :
            <>
                <li><span>Action: </span>None</li>
                <li><span>Type: </span>None</li>
                <li><span>Strands: </span>0</li>
                <li><span>Template: </span>None</li>
                <li><span>Coding: </span>None</li>
                <li><span>Options: </span>{`{}`}</li>
                <li><span>Result: </span>None</li>
            </>
        }
    </div>
  )
}

ResultListView.propTypes = {
    result: PropTypes.object.isRequired,
}

export default ResultListView;