#!/usr/bin/env python
import sqlite3
import os

def makeDatabase():
    if(os.path.isfile("./pyfiles/image.db")):
        return
    else:
        db = open("./pyfiles/image.db", "w")
        db.close()
    return

def makeImageTable():
    connect = sqlite3.connect("./pyfiles/image.db")
    connect.execute("""
                    CREATE TABLE IF NOT EXISTS images
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    image_path TEXT NOT NULL UNIQUE);
                    """)
    connect.commit()
    connect.close()

"""
Run this to make the database and populate it with image paths. Please run this
before trying to tweet!

"""
def populateTable():
    makeDatabase()
    makeImageTable()
    paths = os.listdir("./media")
    connect = sqlite3.connect("./pyfiles/image.db")
    for image in paths:
        connect.execute("""
                        INSERT INTO images(id, image_path)
                        VALUES (?,?);
                        """, (None, image))
        connect.commit()
    connect.close()
    return

def randomImage():
    connect = sqlite3.connect("./pyfiles/image.db")
    image = connect.execute("""
        SELECT image_path FROM images
        ORDER BY RANDOM()
        LIMIT 1;
    """).fetchall()
    connect.commit()
    connect.close()
    return image[0][0]

def randomKeyWordImage(word):
    connect = sqlite3.connect("./pyfiles/image.db")
    word = "%"+word+"%"
    image = connect.execute("""
        SELECT image_path FROM images
        WHERE image_path LIKE ?
        ORDER BY RANDOM()
        LIMIT 1;
    """,(word,)).fetchall()
    connect.commit()
    connect.close()
    print(image[0][0])
    return image[0][0]
