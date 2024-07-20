// import React from 'react'
import style from './css/Profile.module.css'
import ProfileImage from '../assets/profile-circle.svg'
import {Header, Footer} from '../layout'

function Profile() {
  return (
    <>
      <Header bg={true} />
        <section className={style.profile}>
          <div className={style.left}>
            <img src={ProfileImage} alt="Profile image place holder" />
            <p>Name</p>
            <p>Descriptive bio</p>
          </div>
          <div className={style.right}>
            <form>

            </form>
          </div>
        </section>
      <Footer />
    </>
  )
}

export default Profile;