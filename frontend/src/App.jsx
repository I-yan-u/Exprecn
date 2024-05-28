import {Routes, Route} from 'react-router-dom';
import { Home, Profile, History, Exprecn } from './routes';
import { ScrollHandler } from './components/ScrollHandler';
import './App.css'

function App() {

  return (
    <ScrollHandler>
      <Routes>
        <Route path='/' element={<Home />} />
        <Route path='/exprecn' element={<Exprecn />} />
        <Route path='/profile' element={<Profile />} />
        <Route path='/history' element={<History />} />
      </Routes>
    </ScrollHandler>
  )
}

export default App
