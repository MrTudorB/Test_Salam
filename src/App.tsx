import React from 'react';
import Sidebar from './components/Sidebar';
import Header from './components/Header';
import StrategyCards from './components/StrategyCards';

function App() {
  return (
    <div className="flex h-screen bg-main-bg text-white">
      <Sidebar />
      <div className="flex-1">
        <Header />
        <main className="p-6">
          <div className="mb-4">
            <h2 className="text-2xl font-semibold">Overview</h2>
          </div>
          <StrategyCards />
          <div className="mt-6 flex gap-4">
            <input
              type="text"
              placeholder="Amount..."
              className="flex-1 bg-sidebar rounded-lg px-4 py-2 text-white"
            />
            <button className="bg-accent-orange px-8 py-2 rounded-lg text-white">
              deploy
            </button>
          </div>
        </main>
      </div>
    </div>
  );
}

export default App; 