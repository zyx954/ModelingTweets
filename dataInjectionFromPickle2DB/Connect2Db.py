import MySQLdb
def connect_db():
    db = MySQLdb.connect(host="localhost", user='root', passwd='0000',
                         db='TweetsDB')
    cursor = db.cursor();
    return db, cursor;


    # db, cursor = connect_db()
    # cursor.execute("SELECT * FROM Tweets ;")
    # data = cursor.fetchone()

