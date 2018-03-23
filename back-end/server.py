from flask import Flask, render_template

'''
This is where we will set up all api calls to output 
requested information from reactJS front-end
'''


app = Flask(__name__)

@app.route('/hostname/')
def get_hostname_info():
    return "hostname_info"

if __name__ == "__main__":
    app.run()
