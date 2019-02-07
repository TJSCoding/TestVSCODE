import os, sys, sqlite3



#def userTempWert_db_anlegen():
   # CREATE TABLE employee (staff number INT NOT NULL AUTO_INCREMENT, fname VARCHAR(20), lname VARCHAR(30), gender CHAR(1), joining DATE, birth_date DATE, PRIMARY KEY (stuff_number));


if not os.path.exists("D:/vscode/company.db"):
    print("DB nicht vorhanden")
    #userTempWert_db_anlegen()
    connection = sqlite3.connect("D:/vscode/company.db")
    print("DB angelegt")
    dbcursor = connection.cursor()
    dbcursor.execute('''create table if not exists running (date text, distance real, time real, shoe text)''')
    dbcursor.execute('''insert into running values('01.01.2010',15.3,61,'Brooks Adrenaline')''')
    dbcursor.execute('''insert into running values('01.01.2011',16.4,62,'Brooks Adrenalina')''')
    connection.commit()
    query = '''SELECT * FROM running order by distance'''
    dbcursor.execute(query)
    ausgabe = dbcursor.fetchall()
    print (ausgabe)aa

    connection.close()
else:
    print("DB vorhanden")





