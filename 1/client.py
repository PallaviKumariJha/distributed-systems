# Author: Pallavi
# Created on: 17-01-2017
# Modified on: 

# The program requests for a file from server

import requests

# Connect the socket to the port where the server is listening
res = requests.get('http://localhost:4446/test.txt')
res.status_code
print res.text
