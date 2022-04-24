import React from 'react';
import './App.css';
import { BrowserRouter as Router, Routes, Route}
    from 'react-router-dom';
import Planning from './pages/Planning';
import Home from './pages/Home';
//import Flatpickr from "react-flatpickr";

function App() {


  return (
    <Router>
    <Routes>
        <Route path='/' element={<Home />} />
        <Route path='/planning' element={<Planning/>} />
    </Routes>
    </Router>
  );
}

export default App;
