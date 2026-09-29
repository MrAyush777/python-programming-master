import psycopg2 as pg

# below function is used for connection to the database, and create a table in the PostgreSQL database
def table():    
    conn = pg.connect(host="localhost", dbname="postgres", user="postgres", port=5432, password="Ayush@777")

    cursor = conn.cursor()
    cursor.execute('''create table employees(name text, roll_no int, age int);''')

    print("table created succeffully")

    conn.commit()
    conn.close()
    

# below function is used to insert the data into an existing table in PostgreSQL.
def data():    
    conn = pg.connect(host="localhost", dbname="postgres", user="postgres", port=5432, password="Ayush@777")

    cursor = conn.cursor()
    cursor.execute(''' insert into employees values('Keshav', 48, 21); ''')
    cursor.execute(''' insert into employees values('shankar', 1, 10000); ''')

    print("data added succeffully")

    conn.commit()
    conn.close()
    

# below function is used to extract the data from the database. 
def extract():
    conn = pg.connect(host="localhost", dbname="postgres", user="postgres", port=5432, password="Ayush@777")
    
    cursor = conn.cursor()
    cursor.execute(''' select * from employees; ''')
    # print(cursor.fetchall()) # It will fetcb all records from the table.
    print(cursor.fetchone()) # It will fetch first one record from the table.
    
    # we also can fetch single field data from the table like this :
    name = cursor.fetchone() # if you use fetchone second time, now it will fetch second record from the table.
    print(name[0]) # Here we used index number to fetch data. It will return the data on the 0'th index.
         
    conn.commit() 
    conn.close()
         
def input_data():
    conn = pg.connect(host="localhost", dbname="postgres", user="postgres", port=5432, password="Ayush@777")
       
    cursor = conn.cursor()

    name = input("Enter name here : ")
    roll_no = input("Enter roll no here : ")
    age = input("Enter age here : ")
    
    # query = f'''insert into employees values({name},{roll_no},{age})'''    
    query = '''insert into employees values(%s,%s,%s);'''
    cursor.execute(query,(name,roll_no,age))
       
    print("table created succeffully")
       
    conn.commit()
    conn.close()
       

# table()
# data()
# extract()
input_data()