import requests
from requests.auth import HTTPBasicAuth
import json

    
payload ={"site":"default","guid":"guid_xxxx"}

# Use verify=False if your root CA can't be verified.
# Or you can specify verify = '../mycert.pem'

r = requests.post('https://your_url',auth=('admin','notchangeme'),data=payload,verify =False)
    
print r.text