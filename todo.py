import todoDB
from todoDB import tododb


class todolistteamA(object):
    def __init__(self):
        self.list_todo = []
        self.db = tododb()
        pass

    def delete(self, index):
        self.db.delete_todo(index)

    def readOne(self,index):
        return self.db.findOne(index)

    def readAll(self):
        return self.db.findAll()

    def update(self,str, index):
        self.db.update(str, index)

    def add1(self, main_text, text, warn_time):

        self.db.add(main_text, text, warn_time)

#
# if __name__ == "__main__":
#     a =todolistteamA()
#     a.add1('watch','kandianshikandhai','111')
#     b = a.readAll()
#     print(b)