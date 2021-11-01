console.log("On app.js")

import detectEthereumProvider from '@metamask/detect-provider';

const provider = await detectEthereumProvider();

console.log("Imported Successfully")
if (provider) {
  // From now on, this should always be true:
  // provider === window.ethereum
  startApp(provider); // initialize your app
} else {
  console.log('Please install MetaMask!');
}