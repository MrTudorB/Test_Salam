import '@rainbow-me/rainbowkit/styles.css';
import {
  getDefaultConfig,
  RainbowKitProvider,
} from '@rainbow-me/rainbowkit';
import { WagmiConfig } from 'wagmi';
import { mainnet } from 'wagmi/chains';

const projectId = '1aabac2429577bd99b8cee0f5fad2dc7';

const config = getDefaultConfig({
  appName: 'Bulwark Clone',
  projectId,
  chains: [mainnet],
});

export { config, RainbowKitProvider, WagmiConfig, mainnet as chains }; 