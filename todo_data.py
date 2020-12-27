# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 16:14:54 2020

@author: dhan
"""

import datetime
import sqlite3


class Todo:
    id = None
    priority = None
    begin_date = None
    end_date = None
    group_id = None
    title = None
    contents = None
    
    def __init__(self, id, priority, beg_date, end_date, gid, title, contents):
        self.id = id
        self.priority = priority
        self.begin_date = beg_date
        self.end_date = end_date
        self.group_id = gid
        self.title = title
        self.contents = contents

    def __str__(self):
        return '(' + str(self.id) + ',' + str(self.priority) + ',' + str(self.begin_date) + ',' + str(self.end_date) + ',' + self.group_id + ',' + self.title + ',' + self.contents + ')'
    

def adapt_todo(todo):
    return ("%d;%d;%s;%s;%s;%s;%s" % (todo.id, todo.priority, todo.begin_date, todo.end_date, todo.group_id, todo.title, todo.contents)).encode('utf-8')


def convert_todo(s):
    data = s.split(b";")
    id = int(data[0])
    priority = int(data[1])
    beg_date = datetime.datetime(data[2])
    end_date = datetime.datetime(data[3])
    gid = data[4]
    title = data[5]
    contents = data[6]
    return Todo(id, priority, beg_date, end_date, gid, title, contents)


# Register the adapter
sqlite3.register_adapter(Todo, adapt_todo)

# Register the converter
sqlite3.register_converter("Todo", convert_todo)
