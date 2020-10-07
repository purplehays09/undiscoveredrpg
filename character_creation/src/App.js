import React from 'react';
import logo from './logo.svg';
import './App.css';
import Header from './components/Header'
import {races} from './data/races'
import Dashboard from './components/Dashboard'

function App() {
  return (
    <div className="App">
      <Header/>

      <Dashboard/>
    </div>
  );
}

export default App;
