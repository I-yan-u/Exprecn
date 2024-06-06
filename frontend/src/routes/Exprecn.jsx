import style from './css/Exprecn.module.css'
import {Header, Footer} from '../layout'

function Exprecn() {
  return (
    <>
      <Header bg={true} />
        <div className={style.container}>
          <section className={style.side_pane}>
            <div className={style.top}>
              <div>New Query</div>
              <div>Codon Dictionary</div>
            </div>
            <hr />
            <div className={style.bottom}>
              <div>Recent</div>
              <ul>
                <li>Query 1</li>
                <li>Query 2</li>
                <li>Query 3</li>
              </ul>
            </div>
          </section>
          <section className={style.input_area}>
            
          </section>
          <section className={style.output}>
            
          </section>
          <section className={style.config}>
            
          </section>
        </div>
      <Footer />
    </>
  )
}

export default Exprecn;