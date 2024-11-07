import random


class Caesar:
    @staticmethod
    def __shift(char, key):
        key %= 94
        num = ord(char) + key
        if num > 126:
            num -= 94
        return chr(num)

    @staticmethod
    def caesar(txt, keys=0, reverse = False):
        if type(keys) == int:
            keys = list(keys)
        result = []
        for i in range(len(txt)):
            result.append(Caesar.__shift(txt[i], keys[i % len(keys)]))
        return ''.join(result)

    @staticmethod
    def create_key(l):
        c = lambda: random.randint(0, 94)
        return [c() for i in range(l)]

    @staticmethod
    def get_compliment(keys):
        keys = list(keys) if type(keys) == int else keys
        result = []
        for i in keys:
            i %= 94
            result.append(94 - i)
        return result


class Encrypt(Caesar):
    @staticmethod
    def encrypt(txt, key):
        return Caesar.multi_key(txt, key)

    @staticmethod
    def decrypt(txt, key):
        return Caesar.caesar(txt, Caesar.get_compliment(key))

