// import axios from 'axios';
import axiosConf from '../../fe.config';
import {useEffect, useState} from 'react';

function useFetchUser() {
    const [user, setUser] = useState(null);
    const [gToken, setGToken] = useState(null);

    useEffect(() => {
        let token = localStorage.getItem('user');
        token = JSON.parse(token);
        if (token) {
            axiosConf.defaults.headers.common['Authorization'] = `Bearer ${token.token}`;
            axiosConf.get('/user')
                .then(response => {
                    setUser(response.data);
                    setGToken(token)
                })
                .catch(error => {
                    console.error(error);
                });
        }
    }, []);
  return [user, gToken]
}

export default useFetchUser;