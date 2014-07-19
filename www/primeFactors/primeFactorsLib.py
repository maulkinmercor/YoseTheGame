import json
import cgi

def lireParamsCgi():
    params = cgi.FieldStorage()
    try:
# ne marche pas       number = int(params.getvalue('number'))
        number = int(params["number"].value)
    except:
        number = 32
    return number

def decomposerNumero(numero):
    decomposition = []
    temp = numero
    while temp % 2 == 0:
        decomposition.append(2)
        temp /= 2
    return decomposition

def envoyerReponseJson(number, decomposition):
    data = {'number':number, 'decomposition':decomposition}
    json_encoded = json.dumps(data)
    print "Content-type: application/json\n"
    print json_encoded
