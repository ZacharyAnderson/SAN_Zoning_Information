from flask import Flask, render_template, jsonify
import configparser, urllib3
import brocade_functions

'''
This is where we will set up all api calls to output 
requested information from reactJS front-end
'''
#Global Variables are initiated and defined
config = configparser.ConfigParser()
config.read('config.ini')
BROCADE_USERNAME = config['BROCADE']['CMCNE_USERNAME']
BROCADE_PASSWORD = config['BROCADE']['CMCNE_PASSWORD']
FABRIC_KEY = [config['BROCADE']['LYNDHURST_REDFABRIC'], config['BROCADE']['LYNDHURST_BLUEFABRIC']]
base_url = 'https://vsesgplconman/rest/'
app = Flask(__name__)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#Creating the first zoneDB
zoneDB = brocade_functions.createZoneDB(FABRIC_KEY, base_url, brocade_functions.brocadeAPILogin(BROCADE_USERNAME, BROCADE_PASSWORD, base_url))

@app.route('/')
def backend_splashscreen():
    return ('Welcome to the back-end splash screen. \n You should not be here.')

@app.route('/saninfo/api/v1.0/hostname/<host>', methods =['GET'])
def get_hostname_info(host):
    return jsonify(brocade_functions.queryZoneDB(host, zoneDB))

if __name__ == "__main__":
    app.run()
