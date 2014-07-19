import unittest
from mock import patch
import primeFactorsLib

@patch('cgi.FieldStorage')
class TestPowerOfTwo(unittest.TestCase):
    class ChampTest(object):
        def __init__(self, value):
            self.value = value

    NUMBER16 = { "number" : ChampTest("16")}

    def test_lireParamsCgi_16(self, MockClass):
        instance = MockClass.return_value
        instance.__getitem__ = lambda s, key: TestPowerOfTwo.NUMBER16[key]
        instance.__contains__ = lambda s, key: key in TestPowerOfTwo.NUMBER16
        paramNumero = primeFactorsLib.lireParamsCgi()
        self.assertEqual(paramNumero, 16)

    def test_decomposer_numero_2(self, MockClass):
        decomposition = primeFactorsLib.decomposerNumero(2)
        self.assertEqual(decomposition, [2])

    def test_decomposer_numero_64(self, MockClass):
        decomposition = primeFactorsLib.decomposerNumero(64)
        self.assertEqual(decomposition, [2,2,2,2,2,2])
        
if __name__ == "__main__":
    unittest.main(module="powersOfTwoTests")

