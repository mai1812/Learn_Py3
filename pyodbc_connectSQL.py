import pyodbc 

#connect public database
def read(cnxn):
    print(read)
    cursor = cnxn.cursor()
    cursor.execute(f"select top 10 * from {db_table}")
    for row in cursor:
         print('row = %r' % (row,))

driver = 'SQL Server'
server = 'DESKTOP-KLPOHE4\rSQLEXPRESS'
db1 = 'AdventureWorks2014'
tcon = 'yes'
db_table='AdventureWorks2014.HumanResources.Department'

cnxn = pyodbc.connect(driver='{SQL Server}'
                    , host=server, database=db1,
                      trusted_connection=tcon
                      )
read(cnxn)

#conect database use password
driver= 'SQL Server'
server= '192.168.2.23'
db1= 'Mogi2019'
user_name= 'mogi.dev'
psw= 'JRrDh5WT3lyezBhMuWlL'
db_table= 'Mogi2019.dbo.City'

cnxn = pyodbc.connect(driver='{SQL Server}'
                    , host=server, database=db1
                    , user=user_name
                    , password=psw
                    )

read(cnxn)
