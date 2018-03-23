import requests, json, configparser
from pprint import pprint

'''
The new few lines we will take information from our config.ini
and import them to global variables to be used throughout this 
file.
'''
def main():
    FABRIC_KEY = {}
    config = configparser.ConfigParser()
    config.read('config.ini')
    BROCADE_USERNAME = config['BROCADE']['CMCNE_USERNAME']
    BROCADE_PASSWORD = config['BROCADE']['CMCNE_PASSWORD']
    FABRIC_KEY[0] = config['BROCADE']['LYNDHURST_REDFABRIC']
    FABRIC_KEY[1] = config['BROCADE']['LYNDHURST_BLUEFABRIC']

    base_url = 'https://vsesgplconman/rest/'

    request = requests.post(url = base_url + 'login', headers = {'WSUsername':BROCADE_USERNAME, 'WSPassword':BROCADE_PASSWORD}, verify = False)
    print (request.headers['WStoken'])

    req = requests.get(url = base_url + 'resourcegroups/All/fcfabrics/' + FABRIC_KEY[0] + '/zones/', headers = {'WStoken':request.headers['WStoken'], 'Accept':'application/vnd.brocade.networkadvisor+json;version=v1'}, verify = False)
    zone_info = json.loads(req.text)
    pprint(zone_info)
    


if __name__ == '__main__':
    main()