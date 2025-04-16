// src/App.js

import React from 'react';
import './App.css';
import Keypad from './components/Keypad';
import EyesOnMe from './components/EyesOnMe';

function App() {
  return (
    <div className="App">
      <h1>Keypad Component</h1>
      <Keypad />
      <h1>EyesOn Me Component</h1>
      <EyesOnMe />
    </div>
  );
}
export default App;
