import { useState, useEffect } from 'react';
import style from './css/Profile.module.css';
import ProfileImage from '../assets/profile-circle.svg';
import { Header, Footer } from '../layout';
import axiosConf from '../../fe.config';

function Profile() {
  const [image, setImage] = useState(null);
  const [user, setUser] = useState({ firstName: '', lastName: '', email: '', website: '', Bio: '', id: '' });

  useEffect(() => {
    let token = localStorage.getItem('user');
    token = JSON.parse(token);
    if (token) {
      axiosConf.defaults.headers.common['Authorization'] = `Bearer ${token.token}`;
      axiosConf.get('/user')
        .then(response => {
          setUser({
            firstName: response.data.first_name,
            lastName: response.data.last_name,
            email: response.data.email,
            website: response.data.website,
            Bio: response.data.Bio,
            id: response.data.id
          });
        })
        .catch(error => {
          console.error(error);
        });
      
      axiosConf.get('/user/image', { responseType: 'blob' })
        .then(response => {
          const imageUrl = URL.createObjectURL(response.data);
          setImage(imageUrl);
        })
        .catch(error => {
          console.error(error);
        });
    }
  }, []);

  const handleUpdate = () => {
    let token = localStorage.getItem('user');
    token = JSON.parse(token);
    if (token) {
      axiosConf.defaults.headers.common['Authorization'] = `Bearer ${token.token}`;
      axiosConf.put('/user', user)
        .then(response => console.log(response))
        .catch(error => console.log(error))
    }
  }

  return (
    <>
      <Header bg={true} />
      <section className={style.profile}>
        <div className={style.left}>
          <img src={image || ProfileImage} className={style.image} alt="Profile" />
          <p>{user.firstName || 'Firstname'} {user.lastName || 'Lastname'}</p>
          <p>{user.Bio || 'Description'}</p>
          <button>Update Image</button>
        </div>
        <div className={style.right}>
        <input
            type="text"
            value={user.firstName}
            placeholder='First name'
            onChange={e => setUser(u => ({...u, firstName: e.target.value}))}
          />
          <input
            type="text"
            value={user.lastName}
            placeholder='Last name'
            onChange={e => setUser(u => ({...u, lastName: e.target.value}))}
          />
          <input
            type="email"
            value={user.email}
            placeholder='Email'
            onChange={e => setUser(u => ({...u, email: e.target.value}))}
          />
          <input
            type="text"
            value={user.website}
            placeholder='Website'
            onChange={e => setUser(u => ({...u, website: e.target.value}))}
          />
          <input
            type="text"
            value={user.Bio}
            placeholder='Bio'
            onChange={e => setUser(u => ({...u, Bio: e.target.value}))}
          />
          <button onClick={handleUpdate}>Update</button>
        </div>
      </section>
      <Footer />
    </>
  );
}

export default Profile;
