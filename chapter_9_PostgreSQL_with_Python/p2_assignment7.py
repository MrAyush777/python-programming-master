import psycopg2 as ps

def table():
        
    conn = ps.connect(host="localhost", dbname="postgres",port=5432, user="postgres", password = "Ayush@777")

    cursor = conn.cursor()
    cursor.execute(''' create table employee(Eid int, Ename text, Eage int, Esalary int); ''')

    print("table created successfully...")

    conn.commit()
    conn.close()

def insert_data():
    conn = ps.connect(host="localhost", dbname="postgres",port=5432, user="postgres", password = "Ayush@777")
    
    cursor = conn.cursor()   
    cursor.execute(''' insert into employee values(101, 'Ayush', 24, 1000000); ''')
    cursor.execute(''' insert into employee values(102, 'Mohan', 29, 200000); ''')

    print("data inserted successfully...")
    
    conn.commit()
    conn.close()

def fetch_data():
    conn = ps.connect(host="localhost", dbname="postgres", port=5432, user="postgres", password = "Ayush@777")
        
    cursor = conn.cursor()
    cursor.execute(''' select * from employee; ''')

    print(cursor.fetchall())

    conn.commit()
    conn.close()

def input_data():
    conn = ps.connect(host="localhost", dbname="postgres", port=5432, user="postgres", password = "Ayush@777")
            
    cursor = conn.cursor()
    
    Eid = input("Enter your id : ")
    Ename = input("Enter your name : ")
    Eage = input("Enter your age : ")
    Esalary = input("Enter your salary : ")
    
    query = ''' insert into employee values(%s, %s, %s, %s); '''
    cursor.execute(query,(Eid, Ename, Eage, Esalary))
    
    print("Data inserted successfully...")
       
    conn.commit()
    conn.close()
    


table()
insert_data()
fetch_data()
input_data()