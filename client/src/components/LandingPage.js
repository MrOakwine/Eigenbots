import React from 'react';
import '../App.css';

function LandingPage() {
  return (
    <div className="LandingPage">
      <div className="hero">
        <h1>EigenBots</h1>
        <p>A platform to create custom chat and voice bots</p>
      </div>
      <div className="features">
        <h2>Key Features</h2>
        <ul>
          <li>Customizable chat and voice bots</li>
          <li>Easy integration with websites and apps</li>
          <li>No coding skills required</li>
        </ul>
      </div>
      <div className="newsletter">
        <h2>Get Updates</h2>
        <p>Enter your email address to receive updates and news about EigenBots</p>
        <form>
          <input type="email" placeholder="Email Address" />
          <button type="submit">Subscribe</button>
        </form>
      </div>
    </div>
  );
}

export default LandingPage;
