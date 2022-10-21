import requests
import logging
import time
import sys
import json 

#LOGGING
logging.basicConfig(format='%(asctime)s- %(levelname)s- %(message)s', stream=sys.stdout, level=logging.INFO)
log = logging.getLogger(':')
log.setLevel(logging.INFO)

#PARAMS
max_items=300
partial_claim_records_length = 300
#claim_records = {}
offset = "0"

r = requests.get(f"https://rest.bd.evmos.org:1317/evmos/claims/v1/claims_records?pagination.limit={max_items}&offset=0")
r= r.json()
claim_records = r["claims"]
claim_records_length = len(claim_records)


next_key = r['pagination']['next_key']

counter = 1

while partial_claim_records_length == 300 and counter < 7000:
    try: 
        
        logging.info(f"round {counter}")
        counter = counter+1

        r = requests.get(f"https://rest.bd.evmos.org:1317/evmos/claims/v1/claims_records?&pagination.limit={max_items}&offset={claim_records_length}")
        logging.info(f"https://rest.bd.evmos.org:1317/evmos/claims/v1/claims_records?&pagination.limit={max_items}&offset={claim_records_length}")
        logging.info(r.status_code) 
        r.raise_for_status()
        r = r.json()
        partial_claim_records = r["claims"]
        print(partial_claim_records)
        partial_claim_records_length = len(partial_claim_records)
        next_key = r['pagination']['next_key']

        logging.info(f"response length is {partial_claim_records_length}")
        claim_records.extend(partial_claim_records)
        claim_records_length = len(claim_records)
        logging.info(f"claim_record length is {claim_records_length}")
        logging.info("=======================")
        time.sleep(0.125)
    except requests.exceptions.HTTPError as err:
        log.error(f"https://rest.bd.evmos.org:1317/evmos/claims/v1/claims_records?&pagination.limit={max_items}&offset={claim_records_length}")
        raise SystemExit(err)


with open(f'export.json', 'w') as f:
        json.dump(claim_records, f)





