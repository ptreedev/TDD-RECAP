from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # response = requests.get('callToExternalAPI')
    # This is what is patched into and mocked in the test.
    duties = get_duties()
    return [{
            'name':'duty1', 'description': 'Description of duty1'
            }, 
            {   
                'name':'duty2', 'description': 'Description of duty2'
            }, 
            {   
                'name':'duty3', 'description': 'Description of duty3'
            }, 
            {   
                'name':'duty4', 'description': 'Description of duty4'
            }]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
