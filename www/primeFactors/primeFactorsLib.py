import json
import cgi

def lireParamsCgi():
    params = cgi.FieldStorage()
    try:
        number = params["number"][0].value
    except:
        number = "no param number"
    return number

def lireListeParamsNumberCgi():
    params = cgi.FieldStorage()
    try:
        numbers = params["number"]
    except:
        numbers = "no param number"
    if not type(numbers) is list:
        numbers = [numbers]
    return numbers

def transformerEnNombre(chaine):
    try:
        nombre = int(chaine)
    except:
        nombre = chaine
    return nombre

def decomposerNumero(numero):
    if(isinstance(numero, int)):
        if(numero <= 1e6):
            decomposition = []
            temp = numero
            increment = 2
            while (increment <= temp):
                while (temp % increment == 0):
                    decomposition.append(increment)
                    temp /= increment
                increment += 1
        else:
            decomposition = "too big number (>1e6)"
    else:
        decomposition = "not a number"
    return decomposition
    
def preparerReponseJson(nombre, decomposition):
    data = {'number':nombre, 'decomposition':decomposition}
    errordata = {'number':nombre, 'error':"not a number"}
    if (isinstance(nombre, str)): # and nombre == "not a number"):
        json_encoded = json.dumps(errordata)
    else :
        if (decomposition == "too big number (>1e6)"):
            json_encoded = json.dumps({'number':nombre, 'error':decomposition})
        else:
            json_encoded = json.dumps(data)
    return json_encoded

def envoyerReponseJson(json_encoded_data_list):
    print "Content-type: application/json\n"
    if (len(json_encoded_data_list)==1):
        print json_encoded_data_list[0]
    else:
        print "["
        for reponse in json_encoded_data_list[0:-1]:
            print reponse
            print ","
        print json_encoded_data_list[-1]
        print "]"
    

