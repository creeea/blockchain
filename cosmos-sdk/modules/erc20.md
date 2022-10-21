# get token address 
    query --> https://api.evmos.org/#/Query/TokenPairs
    "erc20_address": "0xFA3C22C069B9556A4B2f7EcE1Ee3B467909f4864",
    "denom": "ibc/ED07A3391A112B175915CD8FAF43A2DA8E4790EDE12566649D0C2F97716B8518",
#  convert erc20<>ibc
    export receiver="0x0286fFC971136854cccCb6Bbb4B5AD023C43bf48"
    export ibc_denom="ibc/ED07A3391A112B175915CD8FAF43A2DA8E4790EDE12566649D0C2F97716B8518"
    export chain_id="evmos_9001-2"
    ./evmosd tx erc20 convert-coin 500000$ibc_denom $receiver --from test --gas auto --fees 100000000000000000aevmos --gas 3500000 --chain-id=$chain_id -y

    ./evmosd tx erc20 convert-erc20 0x5FD55A1B9FC24967C4dB09C513C3BA0DFa7FF687 222222 evmos177ggk979ag3cjyt6vevzep2spl3xyfdtsq0937 --from vg --gas auto --fees 100000000000000000aevmos --gas 3500000 -y


# madUSDC
    ./evmosd tx erc20 convert-erc20 0xD2bF8E3aF44465d26aED67414e2E65c34c66c23f 1000000 evmos1vgfhjk8te9nqd6h688qk5cx0lqu3zzxtazqn5v --from test --gas auto --fees 100000000000000000atevmos --gas 3500000 -y

    evmosd tx ibc-transfer transfer transfer channel-13 osmo12h5fxwh49w87mx88t2kyv4ecmmq5u3n84fc752 "2000000erc20/0xD2bF8E3aF44465d26aED67414e2E65c34c66c23f" --chain-id evmos_9000-4 -y --from test --gas auto --fees 100000000000000000atevmos --gas 3500000

    convert to ibc -> 8C72D7C1871F6D232EC82B61ABC6BED8569A6B550A56A868841C6D4E79B5AC0B
    ibc to osmo -> 788F0BF06D073610E13AB61313CBDB0FA672EADBC84357AED98E62083B6AFB27


    https://testnet.mintscan.io/evmos-testnet/txs/6FA3E70527F14CB18459C51E9ADA99582186C93BAE1F6822A29CBA49B90AB976
    
    https://testnet.mintscan.io/osmosis-testnet/txs/C6C907D3D5D9127A4A004B87F0DE033079565976F019320EEB35D2181E575BA5