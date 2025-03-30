import React from 'react';

interface StrategyCardProps {
  title: string;
  description: string;
  apy: string;
  protocols: string[];
  iconPath: string;
}

const StrategyCard: React.FC<StrategyCardProps> = ({
  title,
  description,
  apy,
  protocols,
  iconPath
}) => {
  return (
    <div 
      className="relative w-full transition-transform duration-300 hover:-translate-y-2 cursor-pointer"
      style={{ aspectRatio: '3/4' }}
    >
      {/* Card background */}
      <img 
        src={iconPath} 
        alt={title} 
        className="w-full h-full object-contain"
      />
      
      {/* Content overlay */}
      <div className="absolute inset-0 flex flex-col items-center text-center" style={{ padding: '1.25rem' }}>
        {/* Top content */}
        <div className="flex flex-col items-center w-full">
          <h3 
            className="text-[1.75rem] font-bold mb-1" 
            style={{ color: '#ff6b4a' }}
          >
            {title}
          </h3>
          <p className="text-[0.875rem] text-gray-300 mb-3 max-w-[90%]">{description}</p>
          
          <ul className="space-y-1 w-full flex flex-col items-center">
            {protocols.map((protocol, index) => (
              <li key={index} className="text-gray-300 text-[0.8rem] flex items-center justify-center">
                <span className="mr-1.5 opacity-50">•</span>
                {protocol}
              </li>
            ))}
          </ul>

          {/* APY text */}
          <div 
            className="mt-auto mb-[20%] w-full"
            style={{ marginTop: '2rem' }}
          >
            <div 
              className="text-[2.25rem] font-bold italic leading-none" 
              style={{ 
                color: '#ffffff',
                textShadow: '0 0 20px rgba(255,255,255,0.1)'
              }}
            >
              {apy}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

const StrategyCards = () => {
  const strategies = [
    {
      title: "Anchor",
      description: "Steady growth over time",
      apy: "4.5% APY",
      protocols: ["Aave", "Compound", "Rho markets"],
      iconPath: "/assets/icons/anchor-coin.svg"
    },
    {
      title: "Wildcard",
      description: "For risk-takers & degens",
      apy: "39% APY",
      protocols: ["Nuri", "Tempest", "SyncSwap"],
      iconPath: "/assets/icons/wildcard-dice.svg"
    },
    {
      title: "Zenith",
      description: "Balanced performance",
      apy: "11% APY",
      protocols: ["Mitosis", "Ambient", "Aave"],
      iconPath: "/assets/icons/zenith-gear.svg"
    }
  ];

  return (
    <div className="grid grid-cols-3 gap-8 p-8">
      {strategies.map((strategy, index) => (
        <StrategyCard key={index} {...strategy} />
      ))}
    </div>
  );
};

export default StrategyCards; 