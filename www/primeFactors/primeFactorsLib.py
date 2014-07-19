import json
import cgi

def lireParamsCgi():
    params = cgi.FieldStorage()
    try:
        number = params["number"].value
    except:
        number = "no param number"
    return number

def transformerEnNombre(chaine):
    try:
        nombre = int(chaine)
    except:
        nombre = chaine
    return nombre

def decomposerNumero(numero):
    if(isinstance(numero, int)):
        decomposition = []
        temp = numero
        while temp % 2 == 0:
            decomposition.append(2)
            temp /= 2
    else:
        decomposition = "not a number"
    return decomposition
    
def envoyerReponseJson(nombre, decomposition):
    data = {'number':nombre, 'decomposition':decomposition}
    errordata = {'number':nombre, 'error':"not a number"}
    json_encoded = json.dumps(data)
    print "Content-type: application/json\n"
    print json_encoded

def preparerReponseJson(nombre, decomposition):
    data = {'number':nombre, 'decomposition':decomposition}
    errordata = {'number':nombre, 'error':"not a number"}
    if (isinstance(nombre, str) and nombre == "not a number"):
        json_encoded = json.dumps(errordata)
    else:
        json_encoded = json.dumps(data)
    return json_encoded

def envoyerReponseJson(json_encoded_data):
    print "Content-type: application/json\n"
    print json_encoded_data
