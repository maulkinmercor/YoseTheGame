#!/usr/bin/python
#
import json

alive = True
data = { 'alive' : alive }
json_encoded = json.dumps(data)

print "Content-type: application/json\n"
print json_encoded
