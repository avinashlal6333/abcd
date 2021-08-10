import sqlite3

conn=sqlite3.connect('Mllab.db')
conn.execute('''CREATE TABLE company(
		ID INT PRIMARY KEY  NOT NULL,
		NAME TEXT NOT NULL ,
		AGE INT NOT NULL,
		ADDRESS CHAR(50),
		SALARY REAL);''');
print ("table creatred")
conn.execute("INSERT INTO company VALUES(1,'ABHI',18,'HYD',2000)")
print("Values inserted ")
conn.commit()
for x in conn.execute ("select * from company"):
	print (x)

