import todoDB
from todoDB import tododb


class todolistteamA(object):
    def __init__(self):
        self.list_todo = []
        pass

    def delete(self, index):
        pass

    def readOne(self):
        pass

    def readAll(self):
        pass

    def update(self):
        pass

    def add1(self, text):
        tt = tododb()
        tt.add(text)


if __name__ == "__main__":
    tt1 = todolistteamA()
    tt1.add1('aaa')
    print('add')
