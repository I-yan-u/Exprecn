import {Routes, Route} from 'react-router-dom';
import { Home, Profile, History, Exprecn, Login, Signin } from './routes';
import { ScrollHandler } from './components/ScrollHandler';
import { FormDataContext } from './components';
import './App.css'

function App() {

  return (
    <ScrollHandler>
      <FormDataContext>
      <Routes>
        <Route path='/' element={<Home />} />
        <Route path='/exprecn' element={<Exprecn />} />
        <Route path='/profile' element={<Profile />} />
        <Route path='/history' element={<History />} />
        <Route path='/login' element={<Login />} />
        <Route path='/signup' element={<Signin />} />
      </Routes>
      </FormDataContext>
    </ScrollHandler>
  )
}

export default App
