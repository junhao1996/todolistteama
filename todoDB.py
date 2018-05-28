import sqlite3
import time
import tkinter as tk
from tkinter import *


class tododb(object):
    def __init__(self):
        conn = sqlite3.connect('todolist.db')
        cursor = conn.cursor()
        # self.cursor.execute('drop table if exists warn1')
        # self.cursor.execute('create table user (id INTEGER primary key not null, username varchar(16),password varchar(16))')
        # self.cursor.execute('create table warn (id INTEGER primary key not null, log varchar(200))')
        # self.cursor.execute("create table warn1( id integer primary key, theme varchar(100),log varchar(200), date timestamp not null default (datetime('now','localtime')),warndate varchar(200))")

    def add(self, main_text, text, warn_time):
        conn = sqlite3.connect('todolist.db')
        cursor = conn.cursor()
        cursor.execute("select count(1) from warn")
        rs = cursor.fetchall()
        res_index = rs[0][0]
        cursor.execute("insert into warn1(theme,log,warndate) values ('%s','%s','%s')" % (main_text, text,warn_time))
        print("增加一条提醒，成功 ")
        # todo_id += 1
        cursor.close()
        conn.commit()
        conn.close()

    def findAll(self):
        conn = sqlite3.connect('todolist.db')
        cursor = conn.cursor()
        cursor.execute("select * from warn1 order by id desc")
        print('查找全部提醒数据：')
        rs = cursor.fetchall()

        if not rs:
            print('当前没有提醒记录，请添加')
        else:
            print(rs)
            return([{'id': c[0], 'theme': c[1], 'log': c[2], 'localtime': c[3], 'warntime': c[4]} for c in rs])
        cursor.close()
        conn.commit()
        conn.close()

    def findOne(self, index):
        conn = sqlite3.connect('todolist.db')
        cursor = conn.cursor()
        cursor.execute("select * from warn1 where id=%d" % index)
        print('查找id= %s的提醒数据' % index)
        rs = cursor.fetchall()
        print(rs)
        cursor.close()
        conn.commit()
        conn.close()
        return  rs

    def update(self, str, index):
        conn = sqlite3.connect('todolist.db')
        cursor = conn.cursor()
        cursor.execute("update warn1 set log='%s' where id=%d " % (str, index))
        print('通过id更新数据')
        cursor.close()
        conn.commit()
        conn.close()

    def delete_todo(self, index):
        conn = sqlite3.connect('todolist.db')
        cursor = conn.cursor()
        cursor.execute("delete from warn1 where id=%d" % index)
        print('删除id=%s的提醒成功' % index)
        cursor.close()
        conn.commit()
        conn.close()

    def create_one(self, main_text, text, warn_time):
        conn = sqlite3.connect('todolist.db')
        cursor = conn.cursor()
        cursor.execute("select count(*) from warn1")
        rs = cursor.fetchall()
        res_index = rs[0][0]
        # print(rs)
        # print(res_index)
        print("增加一条提醒，成功 ")

        cursor.execute(
            "insert into warn1(id,theme,log) values ('%d','%s','%s')" % (res_index, main_text, text))

        cursor.execute("select datetime('now','localtime','+%d seconds')" % (warn_time))

        r = cursor.fetchall()
        warntime = r[0][0]
        print(warntime)
        cursor.execute(
            "update warn1 set warndate='%s' where id=%d " % (warntime, res_index))

        print(type(warntime))
        while True:
            local_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            # print(local_time)
            if warntime == local_time:
                print('*' * 20 + "该吃饭了" + "*" * 20)
                a = tk.Tk()
                a.mainloop()
                break

        # self.cursor.execute("select * from warn1 where id=%d" % 1)
        cursor.execute("select * from warn1 ")
        r = cursor.fetchall()
        print(r)
        cursor.close()
        conn.commit()
        conn.close()


# if __name__ == "__main__":
#     todo = tododb()
#     # todo.add('asa1111')
#     # todo.update('dsdsds',211)
#     # todo.delete_todo(5)
#     # todo.findAll()
#     # todo.findOne(2)
#
#     todo.create_one('eat','eat food hahahahhahhaahhahah',5)
