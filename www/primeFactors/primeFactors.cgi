#!/usr/bin/python
#
import primeFactorsLib

chaine = primeFactorsLib.lireParamsCgi()
numero = primeFactorsLib.transformerEnNombre(chaine)
decomposition = primeFactorsLib.decomposerNumero(numero)
reponseJson = primeFactorsLib.preparerReponseJson(numero, decomposition)
primeFactorsLib.envoyerReponseJson(reponseJson)
