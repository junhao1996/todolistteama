import sqlite3


class User_db(object):
    def __init__(self):
        self.conn = sqlite3.connect('todolist.db')
        self.cursor = self.conn.cursor()

        # self.cursor.execute('create table user (id INTEGER primary key not null, username varchar(50),password varchar(50))' )
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

    def add(self, index, username, password):
        # self.todo_id = 2
        self.cursor.execute("insert into user(id,username,password) values (1,'%s','%s')" % (index, username, password))
        print("insert into bad_behaviors (devid, date) select " + ",date('now','localtime')")
        self.todo_id += 1
        self.cursor.close()
        self.conn.commit()
        self.conn.close()

    def findAll(self):
        self.cursor.execute("select * from user")
        rs = self.cursor.fetchall()
        print(rs)
        self.cursor.close()
        self.conn.commit()
        self.conn.close()

    def findOne(self, index):
        self.cursor.execute("select * from user where id=%d" % (index))
        rs = self.cursor.fetchall()
        print(rs)
        self.cursor.close()
        self.conn.commit()
        self.conn.close()

    def update(self, str, index):
        self.cursor.execute("update user set username='%s' where id=%d " % (str, index))
        self.cursor.close()
        self.conn.commit()
        self.conn.close()

    def delete_todo(self, index):
        self.cursor.execute("delete from user where id=%d" % index)


if __name__ == "__main__":
    user = User_db()
    # user.add('asa')
    # user.findAll()
    user.findOne(2)
