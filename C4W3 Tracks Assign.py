import xml.etree.ElementTree as ET
import sqlite3

conn=sqlite3.connect('tracksassign.sqlite')
cur=conn.cursor()

#Making required tables
cur.executescript('''
drop table if exists Artist;
drop table if exists Album;
drop table if exists Track;
drop table if exists Genre;

create table Artist(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

create table Album(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id INTEGER,
    title TEXT UNIQUE
);

create table Genre(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

create table Track(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id INTEGER,
    genre_id INTEGER
);
''')

fname=input('Enter File Name:')
if(len(fname)<1): fname='Library.xml'

def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key:
            found = True
    return None

stuff=ET.parse(fname)
all=stuff.findall('dict/dict/dict')
print('Dict Count:',len(all))

for entry in all:
    if(lookup(entry,'Track ID') is None): continue

    name=lookup(entry,'Name')#title of track
    artist=lookup(entry,'Artist')#Name of artist
    album=lookup(entry,'Album')#Title of Album
    genre=lookup(entry,'Genre')#Genre name

    if name is None or artist is None or album is None or genre is None:
        continue

    print(name,artist,album,genre)

    cur.execute('''INSERT OR IGNORE INTO Artist(name)
        VALUES(?)''',(artist,))
    cur.execute('SELECT id FROM Artist Where name=?',(artist,))
    artist_id=cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album(title,artist_id)
        VALUES(?,?)''',(album,artist_id))
    cur.execute('SELECT id FROM Album WHERE title=?',(album,))
    album_id=cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Genre(name)
        VALUES(?)''',(genre,))
    cur.execute('SELECT id FROM Genre WHERE name=?',(genre,))
    genre_id=cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id,  genre_id) 
        VALUES ( ?, ?, ? )''', 
        ( name, album_id, genre_id ) )

    conn.commit()

    
    
    
