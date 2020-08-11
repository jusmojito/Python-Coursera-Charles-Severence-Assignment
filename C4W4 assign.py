import json
import sqlite3

conn=sqlite3.connect('rosterassign.sqlite')
cur=conn.cursor()

#Making Required Tables
cur.executescript('''
drop table if exists User;
drop table if exists Member;
drop table if exists Course;

create table User(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

create table Course(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE
);

create table Member(
    user_id INTEGER,
    course_id INTEGER,
    role INTEGER,
    PRIMARY KEY(user_id,course_id)
);
''')

fname=input("Enter File Name:")
if (len(fname)<1):
    fname='roster_data.json'

str_data=open(fname).read()
json_data=json.loads(str_data)

for entry in json_data:
    name=entry[0]
    title=entry[1]
    role=entry[2]

    print(name,title,role)

    cur.execute('INSERT OR IGNORE INTO User(name) values(?)',(name,))
    cur.execute('select id from User where name=?',(name,))
    user_id=cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Course(title) values(?)',(title,))
    cur.execute('select id from Course where title=?',(title,))
    course_id=cur.fetchone()[0]

    cur.execute('INSERT INTO Member(user_id,course_id,role) values(?,?,?)',(user_id,course_id,role))

    conn.commit()
