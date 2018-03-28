import requests, json, configparser
from pprint import pprint

'''
The new few lines we will take information from our config.ini
and import them to global variables to be used throughout this 
file.
'''
def main():
    #Global Variables are initiated and defined
    config = configparser.ConfigParser()
    config.read('config.ini')
    BROCADE_USERNAME = config['BROCADE']['CMCNE_USERNAME']
    BROCADE_PASSWORD = config['BROCADE']['CMCNE_PASSWORD']
    FABRIC_KEY = [config['BROCADE']['LYNDHURST_REDFABRIC'], config['BROCADE']['LYNDHURST_BLUEFABRIC']]
    base_url = 'https://vsesgplconman/rest/'
   
    zoneDB = createZoneDB(FABRIC_KEY, base_url, brocadeAPILogin(BROCADE_USERNAME, BROCADE_PASSWORD, base_url))
    queryZoneDB('pipsweb4n', zoneDB)


def createZoneDB(FABRIC_KEY, base_url, WStoken):
    '''
        This function will be used to log in to all Fabrics in the organization
        and create a zoneDB that will be able to to show the data of all active zones
    '''
    zoneDB = {}
    for key in FABRIC_KEY:
        url = base_url + 'resourcegroups/All/fcfabrics/' + key + '/zones/'
        headers = {'WStoken':WStoken, 'Accept':'application/vnd.brocade.networkadvisor+json;version=v1'}
        req = requests.get(url = url, headers = headers, verify = False)
        zone_info = json.loads(req.text)
        for member in zone_info['zones']:
            zoneDB[member['name'].lower()] = member['memberNames']
    return (zoneDB)


def brocadeAPILogin(BROCADE_USERNAME, BROCADE_PASSWORD, base_url):
    '''
        This function is used to log into the brocade API and returns the WStoken 
        that is needed for all calls afterwards.

    '''
    request = requests.post(url = base_url + 'login', headers = {'WSUsername':BROCADE_USERNAME, 'WSPassword':BROCADE_PASSWORD}, verify = False)
    return (request.headers['WStoken'])

def queryZoneDB(hostname, zoneDB):
    '''
        queryZoneDB will take an input of a hostname and output the zones associated with the name
        if no zones are associated it will also let you know that the hostname has no zones associated.
        It will output the zones in JSON format.
    '''
    found_hosts = {}
    for key in zoneDB.keys():
        if hostname.lower() in key:
            found_hosts[key] = zoneDB[key]
    return found_hosts


if __name__ == '__main__':
    main()