import { useContext } from 'react';
import style from './css/SeqConfig.module.css';
import { formDataContext } from './FormDataContext';

function SeqConfig() {
  const { formData, setFormData } = useContext(formDataContext);

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setFormData(formData => ({
      ...formData,
      [name]: type === 'checkbox' ? checked : value,
    }));
  };
  return (
    <form className={style.container}>
      <div className={style.left}>
        <div className={style.action}>
          <p className={style.headers} htmlFor="action">Select an action</p>
          <select name="action" id="action" value={formData.action} onChange={handleChange}>
            <option value="transcription">Transcribe</option>
            <option value="translation">Translate</option>
          </select>
        </div>
        <div className={style.revTranscribe}>
          <p className={style.headers}>Reverse transcribe RNA</p>
          <input
            type="radio"
            id="true"
            name="reverseTranscribe"
            value="true"
            checked={formData.reverseTranscribe === 'true'}
            onChange={handleChange}
          />
          <label className={style.labels} htmlFor="true">True</label><br />
          <input
            type="radio"
            id="false"
            name="reverseTranscribe"
            value="false"
            checked={formData.reverseTranscribe === 'false'}
            onChange={handleChange}
          />
          <label className={style.labels} htmlFor="false">False</label>
        </div>
      </div>
      <div className={style.right}>
        <div className={style.tranlateOptions}>
          <p className={style.headers}>Translation options</p>
          <input
            type="checkbox"
            id="methionine"
            name="methionine"
            checked={formData.methionine}
            onChange={handleChange}
          />
          <label className={style.labels} htmlFor="methionine">Methionine</label><br />
          <input
            type="checkbox"
            id="listView"
            name="listView"
            checked={formData.listView}
            onChange={handleChange}
          />
          <label className={style.labels} htmlFor="listView">Return List</label>
        </div>
      </div>
    </form>
  );
}

export default SeqConfig;
