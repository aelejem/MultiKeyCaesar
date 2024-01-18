import random


class MultiKeyCipher:
    def __init__(self):
        self.char = list('abcdefghijklmnopqrstuvwxyz')

    @staticmethod
    def __rotate(inpKey):
        output = list('abcdefghijklmnopqrstuvwxyz')
        for i in range(inpKey):
            inst = output[0]
            output.pop(0)
            output.append(inst)
        return output

    @staticmethod
    def __rotateBack(inpKey):
        output = list('abcdefghijklmnopqrstuvwxyz')
        for i in range(inpKey):
            inst = output[-1]
            output.pop()
            output.insert(0, inst)
        return output

    def cipher(self, strl, *keys):
        if not keys:
            print("no keys")
            exit()

        if len(keys) == 1 and isinstance(keys[0], str):
            strToNum = []
            for i in keys[0]:
                strToNum.append(self.char.index(i) + 1)
            keys = strToNum

        if isinstance(keys[0], str):
            keys = [random.randint(0, 25) for _ in range(int(keys[0]))]

        keyList = [self.__rotate(key) for key in keys]
        keyOrder = [i % len(keys) for i in range(len(strl))]

        output = []
        for index in range(len(strl)):
            if strl[index].islower() and strl[index].isalpha():
                output.append(keyList[keyOrder[index]][self.char.index(strl[index])])
            elif strl[index].isalpha():
                output.append(keyList[keyOrder[index]][self.char.index(strl[index].lower())].upper())
            else:
                output.append(strl[index])
        return ''.join(output)

    def decipher(self, strl: str, *keys):
        if not keys:
            print("no keys")
            exit()
        if len(keys) == 1 and isinstance(keys[0], str):
            strToNum = []
            for i in keys[0]:
                strToNum.append(self.char.index(i) + 1)
            keys = strToNum
            print(keys)

        keyList = [self.__rotateBack(key) for key in keys]
        keyOrder = [i % len(keys) for i in range(len(strl))]

        output = []
        for index in range(len(strl)):
            if strl[index].isalpha() and strl[index].islower():
                output.append(keyList[keyOrder[index]][self.char.index(strl[index])])
            elif strl[index].isalpha():
                output.append(keyList[keyOrder[index]][self.char.index(strl[index].lower())].upper())
            else:
                output.append(strl[index])
        return ''.join(output)

    @staticmethod
    def randint(n):
        return [random.randint(0, 26) for _ in range(n)]

    def bruteWithKeyNum(self, encryptedStr, ans, keyNum):
        trial = 1
        for i in range(26 ** keyNum):  # 26 possibilities for each position (0-25)
            current_combination = []
            for j in range(keyNum):
                current_combination.append(i % 26)
                i //= 26  # Integer division to move to the next position
            inst = self.decipher(encryptedStr, *current_combination)
            print(trial, inst)
            if inst == ans:
                return trial, current_combination
            trial += 1
        return False

    def bruteWithoutKey(self, encryptedStr, ans, first=1, last=6):
        total = 0
        for i in range(first, last + 1):
            inst = self.bruteWithKeyNum(encryptedStr, ans, i)
            if inst:
                total += inst[0]
                return inst, total
            else:
                total += 26**i

    def iteration1(self, string, keyNum, iter):
        outp = []

        for _ in range(iter):
            a = self.bruteWithKeyNum(self.cipher(string, *self.randint(keyNum)),
                                   "abcdefghijklmnopqrstuvwxyz", i)
            outp.append(a[0])
        print("\n\n\n")
        for i in range(20):
            print(outp[i])


def choose(name):
    user_input2 = input(f"\nThis is the {name} section.\n"
                        "To get out, press QUIT\n"
                        "To go back to choosing e or d or brute, press BACK\n"
                        "To proceed, press any other key\n"
                        "----------------------------------------------------------------\n"
                        "\nWhat do you want to do?\n> ").lower()
    if user_input2 == 'quit':
        exit()
    if user_input2 == 'back':
        main()
    return True


def main():
    mk = MultiKeyCipher()

    user_input = input("----------------------------------------------------------------\n"
                       "This is an advanced version of Caesar Cipher.\n\n"
                       "The options are:\n"
                       "'c' or 'cipher' for cipher\n"
                       "'d' or 'decipher' for decipher\n"
                       "'brute' for brute force attack with knowing the number of the keys\n"
                       "'brute w/o' for brute force attack without knowing the number of the keys\n"
                       "----------------------------------------------------------------\n\n"
                       "What do you want to do?\n> ").lower()

    if user_input == 'c' or user_input == 'cipher':
        choose("cipher")

        stri = input("\nwrite the string/words/sentences you want to cipher/encrypt\n> ")
        key = input("\ninput the key as:\n"
                    "ex) 1 6 3 2 5 or\n"
                    "ex) hello\n"
                    "or you can put rand to get randomized keys to test for the brute force\n"
                    "> ").lower()
        if key == 'rand':
            n = int(input("\nhow many keys?\n>"))
            keys = mk.randint(n)
        else:
            try:
                keys = list(key.split(" "))
                keys = [int(a) for a in keys]

            except:
                if ' ' in key:
                    print('wrong key')
                    exit()

                keys = key

        print(keys)

        print(mk.cipher(stri, *keys))

    elif user_input == 'd' or user_input == 'decipher':
        choose("decipher")

        stri = input("\nwrite the string/words/sentences you want to decipher/decrypt\n> ")
        key = input("\ninput the key as:\n"
                    "ex) 1 6 3 2 5 or\n"
                    "ex) hello\n"
                    "(the key should be the same number(s) as the encrypt, so if you were to put 1, it goes 1 back)\n"
                    "> ")
        try:
            keys = list(key.split(" "))
            keys = [int(a) for a in keys]

        except:
            if ' ' in key:
                print('wrong key')
                exit()

            keys = key

        print(keys)

        print(mk.decipher(stri, *keys))

    elif user_input == 'brute':
        choose("brute force with key")
        stri = input("\nwrite the encrypted string/words/sentences you want to try to check the brute-force attack\n"
                     "> ")
        ans = input("\nput the right answer for the encryption you put before\n"
                    "> ")
        key_num = int(input("\nput the numbers of keys\n"
                            "ex) 1, 2, 3 -> 3 keys, so you put 3\n"
                            "> "))
        i = mk.bruteWithKeyNum(stri, ans, key_num)
        print(f"The brute-force attack took {i[0]} tries, and the combination is {''.join([f"{a} " for a in i[1]])}")

    elif user_input == 'brute w/o':
        choose("brute force without key")
        stri = input("\nwrite the encrypted string/words/sentences you want to try to check the brute-force attack\n"
                     "> ")
        ans = input("\nput the right answer for the encryption you put before\n"
                    "> ")
        key_range1 = int(input("from what num of keys do you want to start from?\n>"))
        key_range2 = int(input("to what num of keys do you want to end with?\n>"))
        i = mk.bruteWithoutKey(stri, ans, key_range1, key_range2)

        print(f"The brute-force attack took {i[1]} total tries, "
              f"and it took {i[0][0]} tries in the correct numbers of keys.\n"
              f"The combination is {''.join([f"{a} " for a in i[0][1]])}\nThe number of keys is {len(i[0][1])}.")

if __name__ == "__main__":
    main()
