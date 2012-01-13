import sys, os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../basecalc'))

from basecalc import BaseCalc

class BaseCalcTest(unittest.TestCase):
    """Unit tests for basecalc."""

    def test_constructor(self):
        """Test basecalc constructor."""

        self.assertRaises(ValueError, BaseCalc, None)
        self.assertRaises(KeyError, BaseCalc, 'unknown')

    def test_to_base(self):
        """Test basecalc to_base()."""

        calc = BaseCalc('bin')
        self.assertEquals(calc.to_base(13), '1101')

        calc.digits('01', digit_type=str)
        self.assertEquals(calc.to_base(13), '1101')

        calc.digits('hex')
        self.assertEquals(calc.to_base(46), '2e')
        self.assertEquals(calc.to_base(-17), '-11')

        calc.digits('iamverypunk', digit_type=str)
        self.assertEquals(calc.to_base(13933), 'krap')

    def test_from_base(self):
        """Test basecalc from_base()."""

        calc = BaseCalc('bin')
        self.assertEquals(calc.from_base('1101'), 13)
        self.assertEquals(calc.from_base('001101'), 13)

        calc.digits('hex')
        self.assertEquals(calc.from_base('-11'), -17)
        self.assertEquals(calc.from_base('-11.05'), -17.01953125)

        calc.digits(tuple(range(7)))
        self.assertEquals(calc.from_base('0.1'), 1.0/7)

        calc.digits('bin')
        b1 = calc.from_base('1110111')
        b2 = calc.from_base('1010110')
        n3 = calc.to_base(b1 * b2)
        self.assertEquals(n3, '10011111111010')


        calc.digits('abc', digit_type=str)
        self.assertEquals(calc.from_base('-bba'), -12)

        calc.digits('ab-', digit_type=str)
        self.assertEquals(calc.from_base('-bba'), 2*27+9+3)

    def test_large_numbers(self):
        """Test large numbers."""

        calc = BaseCalc('hex')
        large_number = 2 ** 30 + 5
        b = calc.to_base(large_number)
        n = calc.from_base(b)
        self.assertEquals(n, large_number)

if __name__ == '__main__':
    unittest.main()

