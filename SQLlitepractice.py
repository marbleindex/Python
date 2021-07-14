# create sql database and populate with music information. Insert multiple records and modify records.

import sqlite3
def create_database():
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    # create a table
    cursor.execute("""CREATE TABLE albums
                          (title text, artist text, release_date text,
                           publisher text, media_type text)
                       """)
    # insert data
    cursor.execute("INSERT INTO albums VALUES "
                   "('Wheels', 'Joan Rhoades', '3/23/2011',"
                   "'Raz Records', 'MP3')")
    # save data to database
    conn.commit()
    # insert multiple records using the "?" method
    albums = [('Genesis', 'Octavio Roz', '6/8/2012',
               'Reaver Records', 'MP3'),
              ('Faces Unseen', 'Green', '3/1/2010',
               'Logic Records', 'MP3'),
              ('From Alpha to Omega', 'League of Sound',
               '6/6/2020', 'Turnmusic', 'MP3'),
              ('No One Can Heal My Love', 'Angels', '6/22/2015',
               'Hype Records', 'MP3')]
    cursor.executemany("INSERT INTO albums VALUES (?,?,?,?,?)",
                       albums)
    conn.commit()
def delete_artist(artist):
    
    # delete an artist from the database
    
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    sql = """
    DELETE FROM albums
    WHERE artist = ?
    """
    cursor.execute(sql, [(artist)])
    conn.commit()
    cursor.close()
    conn.close()
def update_artist(artist, new_name):
    
    # update the artist name

    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    sql = """
    UPDATE albums
    SET artist = ?
    WHERE artist = ?
    """
    cursor.execute(sql, (new_name, artist))
    conn.commit()
    cursor.close()
    conn.close()
def select_all_albums(artist):
    
    # query the database for all the albums by a particular artist
    
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    sql = "SELECT * FROM albums WHERE artist=?"
    cursor.execute(sql, [(artist)])
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result
if __name__ == '__main__':
    import os
    if not os.path.exists("mydatabase.db"):
        create_database()
    delete_artist('Joan Rhoades')
    update_artist('Green', 'Greenery')
    print(select_all_albums('Faces Unseen'))
