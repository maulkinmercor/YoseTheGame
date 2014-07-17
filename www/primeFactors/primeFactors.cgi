#!/usr/bin/python
#
import json
import cgi

formulaire = cgi.FieldStorage()
try:
    number = int(formulaire.getvalue('number'))
except:
    number = 32

decomposition = []

temp = number
while temp % 2 == 0:
    decomposition.append(2)
    temp /= 2

data = {'number':number, 'decomposition':decomposition}

json_encoded = json.dumps(data)

print "Content-type: application/json\n"
print json_encoded
