#!/usr/bin/env python

class BaseCalc(object):

    """
    """

    _DIGIT = tuple([ str(i) for i in range(10) ])
    _LOWER = tuple([ chr(i) for i in range(ord('a'), ord('z') + 1) ])
    _UPPER = tuple([ chr(i) for i in range(ord('A'), ord('Z') + 1) ])

    _BIN   = _DIGIT[0:2]
    _OCT   = _DIGIT[0:9]
    _HEX   = _DIGIT + ('A', 'B', 'C', 'D', 'E', 'F')
    _B64   = _UPPER + _LOWER + _DIGIT + ('+', '/')
    _B62   = _DIGIT + _LOWER + _UPPER

    _DIGITSETS = {
        'bin': _BIN,
        'oct': _OCT,
        'hex': tuple(map((lambda x: x.lower()), _HEX)),
        'HEX': _HEX,
        '62':  _B62,
        '64':  _B64,
    }

    def __init__(self, *args, **kwargs):
        self.digits(*args, **kwargs)


    def digits(self, digits, digit_type=tuple):
        self._has_dash = False
        self._digits   = None
        self._length   = 0
        self._trans    = {}

        if digit_type == str:
            digits = tuple( i for i in digits )

        if isinstance(digits, tuple):
            if not len(digits):
                raise ValueError('digits tuple must be more than 0')

            self._digits = map(lambda x: str(x), digits)
        elif isinstance(digits, str):
            self._digits = self._DIGITSETS[digits]
        else:
            raise ValueError('digits must be tuple or str')

        if '-' in self._digits:
            self._has_dash = True

        self._length = len(self._digits)

        numbers = range(self._length)
        self._trans  = dict([ (self._digits[i], i) for i in numbers ])


    def to_base(self, num):
        str = ''

        '''handle negative numbers.'''
        if num < 0:
            return '-' + self.to_base(-1 * num)

        while num != 0:
            str = self._digits[ num % self._length ] + str
            num = num - num % self._length
            num = num / self._length

        return str

    def from_base(self, base):
        num = 0
        add_in = 0

        '''handle negative numbers.'''
        if not self._has_dash and base[0] == '-':
            return -1 * self.from_base(base[1:])

        '''handle decimal fraction'''
        if '.' in base:
            base, decimal_number = base.split('.')
            dn = self.from_base(decimal_number)
            add_in = float(dn) / self._length ** len(decimal_number)

        for char in base:
            try:
                num = int(num * self._length + self._trans[char])
            except KeyError:
                pass

        return num + add_in

