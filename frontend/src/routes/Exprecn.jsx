import style from './css/Exprecn.module.css'
import {Header, Footer} from '../layout'
import NewQueryLogo from '../assets/newquery.svg'

function Exprecn() {
  return (
    <>
      <Header bg={true} />
        <div className={style.container}>
          <section className={style.side_pane}>
            <div className={style.top}>
              <div>New Query <img src={NewQueryLogo} /></div>
              <div>Codon Dictionary</div>
            </div>
            <div className={style.bottom}>
              <h3>Recent</h3>
              <ul>
                <li></li>
              </ul>
            </div>
          </section>
          <section className={style.input_area}>
            <div className={style.template}>
              <h3>Template Strand</h3>
              <textarea name="inTemplate" rows='5' className={style.inTemplate}></textarea>
              <div className={style.tempButtons}>
                <button className={style.tempbut1}>Add</button>
                <button className={style.tempbut2}>Run</button>
              </div>
            </div>
          </section>
          <section className={style.output}>
            
          </section>
          <section className={style.config}>
            
          </section>
          <section className={style.visualize}>
            
          </section>
        </div>
      <Footer />
    </>
  )
}

export default Exprecn;