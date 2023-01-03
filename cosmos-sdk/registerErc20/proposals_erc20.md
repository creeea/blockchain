# CoinRegisterProposal
    evmosd tx gov submit-proposal register-coin xxx --from=swiss-staking --deposit="1000000000000000000aevmos" --title="Register ERC20 for ATOM (Cosmos-Hub)" --description="## Author\nGV | Swiss Staking ([@swiss_staking](https://twitter.com/swiss_staking))\n## ERC20 representation for Cosmos Hub (ATOM)\nWhen a proposal is initiated for an existing native Cosmos Coin, the erc20 module will deploy a factory ERC20 contract, representing the ERC20 token for the token pair. This will give $ATOM access to DeFi protocols, NFT and new applications that are based on ERC-20 (like AAVE). \n## Before Voting \n- Please follow and discuss this proposal using the official [discussion on commonwealth](https://commonwealth.im/evmos/discussion/5989-this-proposal-creates-and-registers-an-erc20-representation-for-cosmos-atom)\n- For an in-depth explanation of the module, please refer to [Medium Blog](https://medium.com/evmos/introducing-evmos-erc20-module-f40a61e05273)\n- For technical details, please referer to the Evmos [Docs](https://docs.evmos.org/modules/erc20/)\n## Verify Metadata\nWe are applying the same ruleset as lastime. \n- We are primarily guided by the following [Cosmos Assetlist](https://github.com/osmosis-labs/assetlists/blob/main/osmosis-1/osmosis-1.assetlist.json#L50-L66) naming convention . \n- We do not specify a channel number to the symbol {NAME} as it is the first coin registration of ATOM.\n\nPlease double check the following metadata:\n- base: ibc/A4DB47A9D3CF9A068D454513891B526702455D3EF08FB9EB558C561F9DC2B701\n- display: atom\n- name: Cosmos Hub\n- symbol: ATOM" --chain-id=evmos_9001-2 --fees 10000000000000000aevmos --gas 800000

# deposit
 evmosd tx gov deposit 35 63000000000000000000aevmos --from test --chain-id=evmos_9001-2 --fees 16000000000000000000aevmos --gas 8000000

#####################################################
## Author
GV | Swiss Staking ([@swiss_staking](https://twitter.com/swiss_staking))
## ERC20 representation for Cosmos Hub (ATOM)
When a proposal is initiated for an existing native Cosmos Coin, the erc20 module will deploy a factory ERC20 contract, representing the ERC20 token for the token pair. This will give $ATOM access to DeFi protocols, NFT and new applications that are based on ERC-20 (like AAVE). 
## Before Voting 
- Please follow and discuss this proposal using the official [discussion on commonwealth](https://commonwealth.im/evmos/discussion/5989-this-proposal-creates-and-registers-an-erc20-representation-for-cosmos-atom)
- For an in-depth explanation of the module, please refer to [Medium Blog](https://medium.com/evmos/introducing-evmos-erc20-module-f40a61e05273)
- For technical details, please referer to the Evmos [Docs](https://docs.evmos.org/modules/erc20/)
## Verify Metadata
We are applying the same ruleset as lastime. 
- We are primarily guided by the following [Cosmos Assetlist](https://github.com/osmosis-labs/assetlists/blob/main/osmosis-1/osmosis-1.assetlist.json#L50-L66) naming convention . 
- We do not specify a channel number to the symbol {NAME} as it is the first coin registration of ATOM.

Please double check the following metadata:
- base: ibc/A4DB47A9D3CF9A068D454513891B526702455D3EF08FB9EB558C561F9DC2B701
- display: atom
- name: Cosmos Hub
- symbol: ATOM



#####################################################
## Author
GV | Swiss Staking ([@swiss_staking](https://twitter.com/swiss_staking))
## ERC20 representation for Osmosis
This proposal creates and registers an ERC20 representation for Osmosis. If proposal passes you can use Osmosis on DeFi protocols, NFT marketplaces and on new applications that are based on ERC-20.
## Before Voting 
- Please follow and discuss this proposal using the official [discussion on commonwealth](https://commonwealth.im/evmos/discussion/4969-this-proposal-creates-and-registers-an-erc20-representation-for-osmosis)
- For an in-depth explanation of the module, please refer to [Medium Blog](https://medium.com/evmos/introducing-evmos-erc20-module-f40a61e05273)
- For technical details, please referer to the Evmos [Docs](https://docs.evmos.org/modules/erc20/)
## Verify Metadata
We are primarily guided by the following [Osmosis Assetlist](https://github.com/osmosis-labs/assetlists/blob/main/osmosis-1/osmosis-1.assetlist.json#L5-L22) naming convention . Additionally, we shouldn't specify a channel number to the symbol {NAME} on the first coin registration. E.g. whatever is picked as the canonical channel should be symbol {NAME} and if a secondary representation of that IBC token is registered in the evm then a suffix to the symbol {NAME}-{channel-number} should be added. As it is the first Osmosis registration we used the following metadata and denomination:
- base: ibc/ED07A3391A112B175915CD8FAF43A2DA8E4790EDE12566649D0C2F97716B8518
- display: osmo
- name: Osmosis
- symbol: OSMO
## Testing on Testnet
With [proposal 29](https://testnet.mintscan.io/evmos-testnet/proposals/29) we registered testnet OSMO on the Evmos testnet as an ERC20. 

