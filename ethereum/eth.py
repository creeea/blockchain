import json
import sys
import logging
from terra_sdk.client.lcd import LCDClient

#LOGGING
logging.basicConfig(format='%(asctime)s- %(levelname)s- %(message)s', stream=sys.stdout, level=logging.INFO)
log = logging.getLogger(':')
log.setLevel(logging.INFO)
sys.tracebacklimit = 0

from web3 import Web3
w3 = Web3(Web3.HTTPProvider('https://evmos-rpc2.binary.host'))
#log.info(w3.eth.get_block('latest'))
log.info(w3.eth.get_balance('0x0286fFC971136854cccCb6Bbb4B5AD023C43bf48'))
