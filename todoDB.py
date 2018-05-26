import sqlite3


class tododb(object):
    def __init__(self):
        self.conn = sqlite3.connect('todolist.db')
        self.cursor = self.conn.cursor()
        # self.cursor.execute('drop table if exists warn1')
        # self.cursor.execute('create table user (id INTEGER primary key not null, username varchar(16),password varchar(16))')
        # self.cursor.execute('create table warn (id INTEGER primary key not null, log varchar(200))')

    def add(self, text):
        self.cursor.execute("select count(1) from warn")
        rs = self.cursor.fetchall()
        res_index = rs[0][0]
        self.cursor.execute("insert into warn(id,log) values ('%d','%s')" % (res_index,text))
        print("增加一条提醒，成功 ")
        # self.todo_id += 1
        # self.cursor.close()
        # self.conn.commit()
        # self.conn.close()


    def findAll(self):
        self.cursor.execute("select * from warn")
        print('查找全部提醒数据：')
        rs = self.cursor.fetchall()

        if not rs:
            print('当前没有提醒记录，请添加')
        else:
            print(rs)
        self.cursor.close()
        self.conn.commit()
        self.conn.close()

    def findOne(self, index):
        self.cursor.execute("select * from warn where id=%d" % index)
        print('查找id= %s的提醒数据' % index)
        rs = self.cursor.fetchall()
        print(rs)
        self.cursor.close()
        self.conn.commit()
        self.conn.close()

    def update(self, str, index):
        self.cursor.execute("update warn set log='%s' where id=%d " % (str, index))
        print('通过id更新数据')
        self.cursor.close()
        self.conn.commit()
        self.conn.close()

    def delete_todo(self, index):
        self.cursor.execute("delete from warn where id=%d" % index)
        # print('删除id=%s的提醒成功'%index)
        # self.cursor.close()
        # self.conn.commit()
        # self.conn.close()


if __name__ == "__main__":
    todo = tododb()
    todo.add('asa1111')
    # todo.update('dsdsds',211)
    # todo.delete_todo(5)
    todo.findAll()
    # todo.findOne(2)
