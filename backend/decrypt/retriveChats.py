import sqlite3
import os
connection = sqlite3.connect('msgstore.db')
cursor = connection.cursor()
cursor.execute("SELECT data from available_message_view WHERE from_me = 1")
results = cursor.fetchall()
fileManager = open('data1.txt', 'w')
for r in results:
    try:
        fileManager.write(r[0] + '\n')
    except TypeError:
        pass
fileManager.close()
cursor.close()
connection.close()
os.remove('msgstore.db')
#from_me = 1, data available_message_view, availabe_messages_view
