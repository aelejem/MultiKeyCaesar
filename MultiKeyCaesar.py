import random

class MultiKeyCipher:
    def __init__(self):
        self.char = list('abcdefghijklmnopqrstuvwxyz')

    def rotate(self, inpKey: int):
        output = list('abcdefghijklmnopqrstuvwxyz')
        for i in range(inpKey):
            inst = output[0]
            output.pop(0)
            output.append(inst)
        return output

    def rotateBack(self, inpKey: int):
        output = list('abcdefghijklmnopqrstuvwxyz')
        for i in range(inpKey):
            inst = output[-1]
            output.pop()
            output.insert(0, inst)
        return output

    def cipher(self, strl: str, *keys):
        if not keys:
            print("no keys")
            exit()

        if isinstance(keys[0], str):
            keys = [random.randint(0, 25) for _ in range(int(keys[0]))]

        keyList = [self.rotate(key) for key in keys]
        keyOrder = [i % len(keys) for i in range(len(strl))]

        output = []
        for index in range(len(strl)):
            if strl[index].isalpha():
                output.append(keyList[keyOrder[index]][self.char.index(strl[index])])
            else:
                output.append(strl[index])
        return ''.join(output)

    def decipher(self, strl: str, *keys):
        if not keys:
            print("no keys")
            exit()

        keyList = [self.rotateBack(key) for key in keys]
        keyOrder = [i % len(keys) for i in range(len(strl))]

        output = []
        for index in range(len(strl)):
            if strl[index].isalpha():
                output.append(keyList[keyOrder[index]][self.char.index(strl[index])])
            else:
                output.append(strl[index])
        return ''.join(output)

    def bruteForce(self, encryptedCode: str, answer: str, keyNum: int, limit: int = 100000000):
        iter = 0
        for i in range(limit):
            keyList = tuple(random.randint(0, 25) for _ in range(keyNum))
            outp = self.decipher(encryptedCode, *keyList)
            print(f"{iter}: {outp}")
            if outp == answer:
                return iter
            iter += 1
        return False

    def generate_list(self, n):
        result_list = []

        for i in range(26 ** n):  # 26 possibilities for each position (0-25)
            current_combination = []

            for j in range(n):
                current_combination.append(i % 26)
                i //= 26  # Integer division to move to the next position

            result_list.append(current_combination)

        return result_list

    def listBruteForce(self, encryptedStr: str, ans: str, keyNum: int):
        trial = 0
        list_list = self.generate_list(keyNum)
        while list_list:
            inst = self.decipher(encryptedStr, *list_list[0])
            print(trial, inst)
            list_list.pop(0)
            if inst == ans:
                return trial
            trial += 1

a = MultiKeyCipher()
b = a.listBruteForce('', '', 3)
print(a.cipher("", 1, 2, 3))
