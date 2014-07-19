#!/usr/bin/python
#
import primeFactorsLib

numero = primeFactorsLib.lireParamsCgi()
decomposition = primeFactorsLib.decomposerNumero(numero)
primeFactorsLib.envoyerReponseJson(numero, decomposition)

