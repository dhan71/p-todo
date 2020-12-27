import sqlite3
from todo_data import Todo


class TodoDbMgr:
    db_file = 'todo.db'
    create_sql_file = 'create_table.sql'
    con = None

    def __init__(self):
        self.con = sqlite3.connect(self.db_file)

    def create(self):
        create_sql = ''
        with open(self.create_sql_file, 'r') as f:
            create_sql = f.read()
        print('create_sql=', create_sql)
        
        cur = self.con.cursor()
        cur.execute(create_sql)
        self.con.commit()
    
    def select(self):
        select_sql = 'SELECT * FROM todo'
        cur = self.con.cursor()
        res = cur.execute(select_sql)
        rows = res.fetchall()
        return rows

    def insert(self, priority, beg_date, end_date, group_id, title, contents):
        insert_sql = "INSERT INTO todo(priority, begin_date, end_date, group_id, title, contents) VALUES(?, ?, ?, ?, ?, ?)"
        cur = self.con.cursor()
        cur.execute(insert_sql, (priority, beg_date, end_date, group_id, title, contents))
        self.con.commit()
            
    def update(self, id, priority, beg_date, end_date, group_id, title, contents):
        update_sql = "UPDATE todo SET priority = ?, begin_date = ?, end_date = ?, group_id = ?, title = ?, contents = ? WHERE id = ?"
        cur = self.con.cursor()
        cur.execute(update_sql, (priority, beg_date, end_date, group_id, title, contents, id))
        self.con.commit()
            
    def delete(self, id):
        delete_sql = "DELETE FROM todo WHERE id = ?"
        cur = self.con.cursor()
        cur.execute(delete_sql, (id))
        self.con.commit()

    def select_todo(self) -> [Todo]:
        todos = []
        rows = self.select()
        for row in rows:
            todos.append(Todo(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        return todos

    def insert_todo(self, t):
        self.insert(t.priority, t.begin_date, t.end_date, t.group_id, t.title, t.contents)


class TodoDbMgr2:
    db_file = 'todo.db'
    con = None

    def __init__(self):
        self.con = sqlite3.connect(self.db_file)

    def create(self):
        create_sql = "CREATE TABLE ptodo(p Todo)"
        print('create_sql=', create_sql)
        
        cur = self.con.cursor()
        cur.execute(create_sql)
        cur.close()
        self.con.commit()
    
    def select(self):
        select_sql = 'SELECT p FROM ptodo'
        cur = self.con.cursor()
        res = cur.execute(select_sql)
        rows = res.fetchall()
        cur.close()
        return rows

    def insert(self, todo):
        insert_sql = "INSERT INTO ptodo(p) VALUES(?)"
        cur = self.con.cursor()
        cur.execute(insert_sql, (todo, ))
        cur.close()
        self.con.commit()
            
    def update(self, todo):
        update_sql = "UPDATE todo SET priority = ?, begin_date = ?, end_date = ?, group_id = ?, title = ?, contents = ? WHERE id = ?"
        cur = self.con.cursor()
        cur.execute(update_sql, (todo, ))
        cur.close()
        cur.close()
        self.con.commit()
            
    def delete(self, id):
        delete_sql = "DELETE FROM todo WHERE id = ?"
        cur = self.con.cursor()
        cur.execute(delete_sql, (id))
        cur.close()
        self.con.commit()

"""
with sqlite3.connect('todo.db') as con:
    cur = con.cursor()
    cur.execute(create_sql)
    con.commit()

with sqlite3.connect('todo.db') as con:
    insert_sql = "INSERT INTO todo(priority, begin_date, end_date, group_id, title, contents) VALUES(?, ?, ?, ?, ?, ?)"
    cur = con.cursor()
    cur.execute(insert_sql, (5, '2020-12-19 12:37:01', '2020/12/19 12:37:01', '', 'Title', 'Contents'))
    con.commit()

with sqlite3.connect('todo.db') as con:
    select_sql = "SELECT * FROM todo"
    cur = con.cursor()
    res = cur.execute(select_sql)
    rows = res.fetchall()
    for row in rows:
        print(row)
"""

if __name__ == '__main__':
    db_mgr = TodoDbMgr()
    # db_mgr.create()
    # id, priority, begin_date, end_date, group_id, title, contents
    # todo = Todo(7, 5, '2020-12-26 17:01:02', '2020-12-26 17:01:02', 'group #1', '제목 7', '내용 7')
    # sdb_mgr.insert_todo(todo)
    todos = db_mgr.select_todo()
    for todo in todos:
        print(todo)
