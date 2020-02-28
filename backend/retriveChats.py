import sqlite3
connection = sqlite3.connect('msgstore.db')
cursor = connection.cursor()
cursor.execute("SELECT data from available_message_view WHERE from_me = 1")
results = cursor.fetchall()
fileManager = open('data1.txt', 'w')
for r in results:
    print(r[0])
    try:
        fileManager.write(r[0] + '\n')
    except TypeError:
        pass
fileManager.close()
cursor.close()
connection.close()
#from_me = 1, data available_message_view, availabe_messages_view