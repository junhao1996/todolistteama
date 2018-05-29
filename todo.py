import todoDB
from todoDB import tododb


class todolistteamA(object):
    def __init__(self):
        self.list_todo = []
        self.db = tododb()
        pass

    def delete(self, index):
        self.db.delete_todo(index)

    def read_one(self, index):
        return self.db.find_one(index)

    def read_all(self):
        return self.db.find_all()
    def read_id(self):
        return self.db.find_id()

    def read_maxone(self):
        return self.db.find_maxone()

    def update(self,str, index):
        self.db.update(str, index)

    def add1(self, main_text, text, warn_time):

        self.db.add(main_text, text, warn_time)


if __name__ == "__main__":

    a =todolistteamA()
    a.read_maxone()
#     a.add1('watch','kandianshikandhai','111')
#     b = a.readAll()
#     print(b)