import cx_Oracle as orc
import getpass
# dsn_tns = cx_Oracle.makedsn('Host Name', 'Port Number', service_name='Service Name')
# conn = cx_Oracle.connect(user=r'User Name', password='Personal Password', dsn=dsn_tns)
#
# c = conn.cursor()
# c.execute('select * from database.table') # use triple quotes if you want to spread your query across multiple lines
# for row in c:
#     print (row[0], '-', row[1]) # this only shows the first two columns. To add an additional column you'll need to add , '-', row[2], etc.
# #conn.close()
print("Welcome enter the username and the passowrd to enter the system")
Admin_User=str(input('enter username database: '))
Admin_Pass=str(input('enter Password database: '))

conn=orc.connect(Admin_User + '/' + Admin_Pass + '@//localhost:1521/xe')
print("Connected successfully the versoin is : ",conn.version)

#op=input('Do you want to get all the tables : ')


#cursor
cur = conn.cursor()
cur.execute('SELECT COUNT (*) FROM user_tables')
rows=''
for row in cur:
    #print(row[0])
    rows=','.join([str(i) for i in row])
    #print(rows)

cur.execute('SELECT table_name FROM user_tables')
for rows in cur:
    print(rows)
#Count the rows : cur.execute('SELECT COUNT(*) FROM employees')
#Count the columns :select count(*) from user_tab_columns where table_name='EMPLOYEES';
print("1.Count Columns from spesifc table ")
print("2.Count Row from spesifc table ")
options=int(input("Choose an option: "))
if(options==1):
    tablestr=str(input('Enter the name of the table: '))

    cur.execute("select count(*) from user_tab_columns where table_name="+"'"+tablestr.upper()+"'")
    for row in cur:
        print(row[0])
    #print (row[0], '-', row[1],'-',row[2],'-',row[3],'-',row[4],'-',row[5],'-',row[6],'-',row[7],'-',row[8],'-',row[9],'-',row[10])
    # for i in range(11):
    #     print(row[i],'-',)
#'SELECT COUNT (*) FROM user_tables'
elif(options==2):
    table=input("Enter your table: ")
    cur.execute('SELECT COUNT (*) FROM '+table)
    for row in cur:
        print(row[0])

elif(options==3):
    table=input("Enter your table: ")
    cur.execute('SELECT * FROM '+table)
    for row in cur:
        print(row[0])

elif(options==4):

    query=str(input("Enter your opetoion: "))
    cur.execute("'"+query+"'")
    for row in cur:
        print(row[0])
