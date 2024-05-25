import {Routes, Route} from 'react-router-dom';
import { Home, Profile, History } from './routes';
import './App.css'

function App() {

  return (
    <Routes>
      <Route path='/' element={<Home />} />
      <Route path='/profile' element={<Profile />} />
      <Route path='/history' element={<History />} />
    </Routes>
  )
}

export default App
