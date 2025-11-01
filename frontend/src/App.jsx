import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [spend, setSpend] = useState('');
  const [prediction, setPrediction] = useState(null);
  const [error, setError] = useState(null);

  const handlePredict = () => {
    setPrediction(null);
    setError(null);

    fetch('http://localhost:8000/api/predict/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        spend: spend,
      }),
    })
      .then(response => {
        if (!response.ok) {
          return response.json().then(err => { throw new Error(err.error || 'Something went wrong'); });
        }
        return response.json();
      })

      .then(data => {
        console.log('Success:', data);
        setPrediction(data.predicted_sales);
      })

      .catch(error => {
        console.error('Error:', error);
        setError(error.message);
      });
  };

return (
  <div>
    <h1>Marketing AI Dashboard</h1>
    <p>Enter Ad Spend ($) to predict sales:</p>
    <div>
      <input type = "number" value = {spend} onChange = {e => setSpend(e.target.value)} />
      <button onClick = {handlePredict}>Predict</button>
    </div>
    {prediction !== null && (
      <div style = {{ marginTop: '20px' }}>
        <h2>Predicted Sales:
          <p style = {{ color: 'green'}}>
            ${prediction.toFixed(2)}
          </p>
        </h2>
      </div>
    )}
    {error && (
      <div style = {{ marginTop: '20px', color: 'red'}}>
        <h3 style = {{ color: 'red'}}>Error: {error}</h3>
      </div>
    )}
  </div>
);
}

export default App; 