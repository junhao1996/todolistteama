import sqlite3


# import omit


class tododb(object):
    def __init__(self):
        self.conn = sqlite3.connect('todolist.db')
        self.cursor = self.conn.cursor()

        # self.cursor.execute('create table warn1 (id INTEGER primary key not null, log varchar(200))' )
        # devid = 15
        #
        #
        # devid = 18
        # cursor.execute("insert into bad_behavio
        # rs (devid, date) select ?,datetime('now','localtime')", (devid, ))
        # cursor.execute("select * from bad_behaviors where devid=18")
        # rs = cursor.fetchall()
        # print (rs)
        # cursor.close()
        # conn.commit()
        # conn.close()

    def add(self, text):
        # self.todo_id = 2
        self.cursor.execute("insert into warn1(id,log) values (211,'%s')" % (text))
        print("insert into bad_behaviors (devid, date) select " + ",date('now','localtime')")
        self.todo_id += 1
        self.cursor.close()
        self.conn.commit()
        self.conn.close()

    def findAll(self):
        self.cursor.execute("select * from warn1")
        rs = self.cursor.fetchall()
        print(rs)
        self.cursor.close()
        self.conn.commit()
        self.conn.close()

    def findOne(self, index):
        self.cursor.execute("select * from warn1 where id=%d" % (index))
        rs = self.cursor.fetchall()
        print(rs)
        self.cursor.close()
        self.conn.commit()
        self.conn.close()

    def update(self):
        # self.cursor.execute("update warn1 set log=\‘texts\’where id=211 ")
        # self.cursor.close()
        # self.conn.commit()
        # self.conn.close()
        pass

    def deletes(self):
        # self.cursor.execute("delete from warn1 where id=211")
        # self.cursor.close()
        # self.conn.commit()
        # self.conn.close()
        pass


if __name__ == "__main__":
    todo = tododb()
    # todo.add('asa')
    # todo.findAll()
    todo.findOne(2)
