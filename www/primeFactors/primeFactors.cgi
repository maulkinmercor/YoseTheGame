#!/usr/bin/python
#
import primeFactorsLib

parametres = primeFactorsLib.lireListeParamsNumberCgi()
reponseJson = []
for parametre in parametres:
    numero = primeFactorsLib.transformerEnNombre(parametre.value)
    decomposition = primeFactorsLib.decomposerNumero(numero)
    reponseJson.append(primeFactorsLib.preparerReponseJson(numero, decomposition))
primeFactorsLib.envoyerReponseJson(reponseJson)