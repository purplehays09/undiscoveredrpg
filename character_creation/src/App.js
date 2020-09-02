import React from 'react';
import logo from './logo.svg';
import './App.css';
import Header from './Header'
import {races} from './data/races'
import Dashboard from './Dashboard'

function App() {
  return (
    <div className="App">
      <Header/>

      <Dashboard/>
    </div>
  );
}

export default App;
