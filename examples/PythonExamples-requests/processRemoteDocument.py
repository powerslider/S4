# Copyright  2013, 2014, Ontotext AD
#
# This file is free software; you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation; either version 2.1 of the License, or (at your option)
# any later version.
# This library is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
# details.
# You should have received a copy of the GNU Lesser General Public License
# along with this library; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA

# IMPORTANT!!! Please install the packages below, needed for this example

import requests
import json

endpoint = "https://text.s4.ontotext.com/v1"
service = "/twitie"
key = '<api-key>'
secret = '<api-secret>'
data = {
    "documentUrl":
    "http://www.bbc.com/future/story/20130630-super-shrinking-the-city-car",
    "documentType": "text/html",
}
jsonData = json.dumps(data)
headers = {
    'Accept': "application/json",
    'Content-type': "application/json",
    'Accept-Encoding': "gzip",
}

req = requests.post(
    endpoint + service, headers=headers,
    data=jsonData, auth=(key, secret))

response = json.loads(req.content.decode('utf-8'))
print(response)

# Response status code
print ('Request Code: {}\n'.format(req.status_code))

# Response Headers
head = dict(req.headers)
print ('Headers: ')
for each in head:
    print (each.capitalize(), ": ", head[each])
