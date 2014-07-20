import unittest
from mock import patch
import primeFactorsLib
import json

@patch('cgi.FieldStorage')
class TestPrimeFactors(unittest.TestCase):
    class ChampTest(object):
        def __init__(self, value):
            self.value = value

    NUMBER16 = { "number" : ChampTest("16")}
    NUMBERHELLO = { "number" : ChampTest("Hello")}

    def test_lireParamsCgi_16(self, MockClass):
        instance = MockClass.return_value
        instance.__getitem__ = lambda s, key: TestPrimeFactors.NUMBER16[key]
        instance.__contains__ = lambda s, key: key in TestPrimeFactors.NUMBER16
        paramString = primeFactorsLib.lireParamsCgi()
        paramNumero = primeFactorsLib.transformerEnNombre(paramString)
        self.assertEqual(paramNumero, 16)

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

    def test_deocmposer_300(self, MockClass):
        decomposition = primeFactorsLib.decomposerNumero(300)
        self.assertEqual(decomposition, [2,2,3,5,5])
        
if __name__ == "__main__":
    unittest.main(module="powersOfTwoTests")

