curl -X POST 'https://alephzero.api.subscan.io/api/scan/staking/validator' \
  --header 'Content-Type: application/json' \
  --header 'X-API-Key: 25278bbcb470444b81a7e3c4dd36224b' \
  --data-raw '{
    "stash": "5FTsYv3dgJsjndE3ktF1Rp3rF6UjGybGW2mcYVuaFzfrC4Cv"
  }'


curl -X POST 'https://alephzero.api.subscan.io/api/scan/staking/nominators' \
  --header 'Content-Type: application/json' \
  --header 'X-API-Key: 25278bbcb470444b81a7e3c4dd36224b' \
  --data-raw '{
    "row": 20,
    "page": 0,
    "address": "5FTsYv3dgJsjndE3ktF1Rp3rF6UjGybGW2mcYVuaFzfrC4Cv"
  }'
