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

    evmosd tx ibc-transfer transfer transfer channel-13 osmo184r9xhk0xuju9f9efkee3jqqrtn37a5pw4knx5 "500000erc20/0xD2bF8E3aF44465d26aED67414e2E65c34c66c23f" --chain-id evmos_9000-4 -y --from test --gas auto --fees 100000000000000000atevmos --gas 3500000
