import axios from "axios";

const axiosConf = axios.create({
    baseURL: 'http://localhost:5000/exprecn',
    timeout: 50000
});

export default axiosConf;