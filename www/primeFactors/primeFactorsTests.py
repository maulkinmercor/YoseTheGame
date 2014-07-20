import unittest
from mock import patch
import primeFactorsLib
import json

@patch('cgi.FieldStorage')
class TestPrimeFactors(unittest.TestCase):
    class ChampTest(object):
        def __init__(self, value):
            self.value = value

    NUMBER16 = { "number" : [ChampTest("16")]}
    NUMBERHELLO = { "number" : [ChampTest("Hello")]}
    NUMBER_16_32_HELLO = { "number" : [ChampTest("16"), ChampTest("32"), ChampTest("hello")]}

    def test_lireParamsCgi_16(self, MockClass):
        instance = MockClass.return_value
        instance.__getitem__ = lambda s, key: TestPrimeFactors.NUMBER16[key]
        instance.__contains__ = lambda s, key: key in TestPrimeFactors.NUMBER16
        paramString = primeFactorsLib.lireParamsCgi()
        paramNumero = primeFactorsLib.transformerEnNombre(paramString)
        self.assertEqual(paramNumero, 16)

    def test_lireListeParamsCgi_16(self, MockClass):
        instance = MockClass.return_value
        instance.__getitem__ = lambda s, key: TestPrimeFactors.NUMBER16[key]
        instance.__contains__ = lambda s, key: key in TestPrimeFactors.NUMBER16
        parametres = primeFactorsLib.lireListeParamsNumberCgi()
        for parametre in parametres:
            paramNumero = primeFactorsLib.transformerEnNombre(parametre.value)
        self.assertEqual(paramNumero, 16)

    def test_lireListeParams(self, MockClass):
        instance = MockClass.return_value
        instance.__getitem__ = lambda s, key: TestPrimeFactors.NUMBER_16_32_HELLO[key]
        instance.__contains__ = lambda s, key: key in TestPrimeFactors.NUMBER_16_32_HELLO
        parametres = primeFactorsLib.lireListeParamsNumberCgi()
        paramsNumeros = []
        for parametre in parametres:
            paramsNumeros.append(primeFactorsLib.transformerEnNombre(parametre.value))
        self.assertEqual(paramsNumeros, [16, 32, "hello"])
        
    def test_decomposer_numero_2(self, MockClass):
        decomposition = primeFactorsLib.decomposerNumero(2)
        self.assertEqual(decomposition, [2])

    def test_decomposer_numero_64(self, MockClass):
        decomposition = primeFactorsLib.decomposerNumero(64)
        self.assertEqual(decomposition, [2,2,2,2,2,2])

    def test_lireParamsCgi_hello(self, MockClass):
        instance = MockClass.return_value
        instance.__getitem__ = lambda s, key: TestPrimeFactors.NUMBERHELLO[key]
        instance.__contains__ = lambda s, key: key in TestPrimeFactors.NUMBERHELLO
        paramString = primeFactorsLib.lireParamsCgi()
        paramNumero = primeFactorsLib.transformerEnNombre(paramString)
        self.assertEqual(paramNumero, "Hello")

    def test_decomposer_hello(self, MockClass):
        decomposition = primeFactorsLib.decomposerNumero("Hello")
        self.assertEqual(decomposition, "not a number")

    def test_decomposer_1000001(self, MockClass):
        decomposition = primeFactorsLib.decomposerNumero(1000001)
        self.assertEqual(decomposition, "too big number (>1e6)")

    def test_json_response_number2(self, MockClass):
        retour = primeFactorsLib.preparerReponseJson(2, [2])
        data = {'decomposition':[2], 'number':2}
        decoded = json.loads(retour)
        self.assertEqual(decoded['decomposition'], [2])
        self.assertEqual(decoded['number'], 2)

    def test_json_response_hello(self, MockClass):
        retour = primeFactorsLib.preparerReponseJson("hello", "not a number")
        data = {'decomposition':"not a number", 'number':"hello"}
        decoded = json.loads(retour)
        self.assertEqual(decoded['error'], "not a number")
        self.assertEqual(decoded['number'], "hello")

    def test_json_response_1000001_too_big(self, MockClass):
        retour = primeFactorsLib.preparerReponseJson(1000001, "too big number (>1e6)")
        data = {'error':"too big number (>1e6)", 'number':1000001}
        decoded = json.loads(retour)
        self.assertEqual(decoded['error'], "too big number (>1e6)")
        self.assertEqual(decoded['number'], 1000001)
        
    def test_decomposer_300(self, MockClass):
        decomposition = primeFactorsLib.decomposerNumero(300)
        self.assertEqual(decomposition, [2,2,3,5,5])

    def test_decomposer_360(self, MockClass):
        decomposition = primeFactorsLib.decomposerNumero(360)
        self.assertEqual(decomposition, [2,2,2,3,3,5])

    def test_decomposer_1000000(self, MockClass):
        decomposition = primeFactorsLib.decomposerNumero(1000000)
        self.assertEqual(decomposition, [2,2,2,2,2,2,5,5,5,5,5,5])
        
if __name__ == "__main__":
    unittest.main(module="powersOfTwoTests")

