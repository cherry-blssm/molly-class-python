import random

class Character:
    def __init__(self, name: str, age: int, villain: bool, happy_ending: bool ):
        self.name = name
        self.age = age
        self.villain = villain
        self.happy_ending = happy_ending

    def generate_ending(self):

        r = random.randint(1, 6)

        if r == 1 or r == 3 or r == 5:
            self.happy_ending = not self.happy_ending
        if self.happy_ending:
            # this is your happy ending ...
            return f'{self.name} lives happily ever after!! :3'
        else:
            # this is your villian arc ...
            return f'{self.name} meets an unfortunate demise.. :[]'


if __name__ == '__main__':
    bill_cipher = Character('Bill Cipher', 3000, True, False)
    print(bill_cipher.generate_ending())

    mabel_pines = Character('Mabel Pines', 12, False, True)
    print(mabel_pines.generate_ending())



