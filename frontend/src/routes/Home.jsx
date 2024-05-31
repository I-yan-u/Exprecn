import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import style from './css/Home.module.css';
import Header from '../layout/Header';
import Footer from '../layout/Footer';
import Blob1 from '../assets/blob2.svg';
import DNA1 from '../assets/dna2.svg';
import Molecule from '../assets/molecule2.svg';

function Home() {
    const [displayText, setDisplayText] = useState('');

    useEffect(() => {
        const texts = ['Expression', 'Transcription', 'Translation'];
        let i = 0;
        let j = 0;
        let currentText = '';
        const interval = setInterval(() => {
            if (j < texts[i].length) {
                currentText += texts[i][j];
                setDisplayText(currentText);
                j++;
            } else {
                j = 0;
                currentText = '';
                i = (i + 1) % texts.length;
            }
        }, 200);

        return () => clearInterval(interval);
    }, []);

    return (
        <>
            <Header />
            <section id='Home'>
                <div className={style.container}>
                    <div className={style.left}>
                        <h2>Explore the Intricacies of <span>Genetic <span>{displayText}</span></span></h2>
                        <p>
                            Exprecn is your go-to web application for simulating the fundamental
                            processes of transcription and translation, essential for understanding
                            gene expression. Whether you are a student, researcher, or enthusiast,
                            Exprecn offers an intuitive and powerful platform to delve into the
                            world of molecular biology.
                        </p>
                        <Link to='/exprecn'>
                        <button className={style.link}>
                            <p>Get Started</p>
                            <svg
                                xmlns="http://www.w3.org/2000/svg"
                                className="h-6 w-6"
                                fill="none"
                                viewBox="0 0 24 24"
                                stroke="currentColor"
                                strokeWidth="4"
                            >
                                <path
                                strokeLinecap="round"
                                strokeLinejoin="round"
                                d="M14 5l7 7m0 0l-7 7m7-7H3"
                                ></path>
                            </svg>
                            </button>
                        </Link>
                    </div>
                    <div className={style.right}>
                        <img className={style.blob} src={Blob1} alt="blob" />
                        <img className={style.image_gene} src={DNA1} alt="gene" />
                        <img className={style.image_molecule} src={Molecule} alt="molecule" />
                    </div>
                </div>
                <section className={style.block}>
                    Block
                </section>
            </section>
            <Footer />
        </>
    );
}

export default Home;
