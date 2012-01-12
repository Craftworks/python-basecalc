
class BaseCalc(object):

    digits = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJELMNOPQRSTUVWXYZ'

    def to_base(num, chars = digits):
        str = ''
        while num != 0:
        str = chars[ num % len(chars) ] + str
        num = num - num % len(chars)
        num = num / len(chars)
        return str

        def from_base(base, chars = digits):
            num = 0
            for char in base:
        num = num * len(chars)
            num = num + chars.index(char)
            return num

