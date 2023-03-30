import React, { useState, useEffect } from 'react';
import axios from 'axios';

function BotOverview() {
  const [bots, setBots] = useState([]);

  useEffect(() => {
    // Fetch bots data from backend
    axios.get('/api/bots')
      .then(res => {
        setBots(res.data);
      })
      .catch(err => {
        console.log(err);
      });
  }, []);

  return (
    <div className="BotOverview">
      <ul>
        {bots.map(bot => (
          <li key={bot.id}>
            <h3>{bot.name}</h3>
            <p>Intents: {bot.intents}</p>
            <p>Entities: {bot.entities}</p>
            <p>Actions: {bot.actions}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default BotOverview;
