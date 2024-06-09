import style from './css/SeqConfig.module.css'; 
// import { createContext, useRef } from "react";
// import PropTypes from 'prop-types'

// export const configData = createContext();

// export const seqConfigData = ({children}) => {
//     return (

//     )
// }

// seqConfigData.PropTypes = {
//     children: PropTypes.node
// }


function SeqConfig() {
  return (
    <div className={style.container}>
        <div className={style.left}>
            <div className={style.action}>
                <p className={style.headers} htmlFor="action">Select an action</p>
                <select name="action" id="action">
                    <option value="transcrition">Transcribe</option>
                    <option value="translation">Translate</option>
                </select>
            </div>
            <div className={style.revTranscribe}>
                <p className={style.headers}>Reverse transcribe RNA</p>
                <input type="radio" id="true" name="reverseTranscribe" value="true"/>
                <label className={style.labels} htmlFor="true">True</label><br />
                <input type="radio" id="false" name="reverseTranscribe" value="false"/>
                <label className={style.labels} htmlFor="false">False</label>
            </div>
        </div>
        <div className={style.right}>
            <div className={style.tranlateOptions}>
                <p className={style.headers}>Translation options</p>
                <input type="checkbox" id='methionine' name='methionine' value='true'/>
                <label className={style.labels} htmlFor="methionine">Methionine</label><br />
                <input type="checkbox" id='listView' name='listView' value='true'/>
                <label className={style.labels} htmlFor="listView">Return List</label>
            </div>
        </div>
    </div>
  )
}

export default SeqConfig;