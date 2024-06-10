import style from './css/Exprecn.module.css'
// import { useContext } from 'react'
import {Header, Footer} from '../layout'
import NewQueryLogo from '../assets/newquery.svg'
import { InputSequence, SeqConfig } from '../components'

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
            <InputSequence />
          </section>
          <section className={style.output}>
            
          </section>
          <section className={style.config}>
            <SeqConfig />
          </section>
          <section className={style.visualize}>
            
          </section>
        </div>
      <Footer />
    </>
  )
}

export default Exprecn;