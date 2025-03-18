import mysql.connector
from prettytable import PrettyTable
conn = mysql.connector.connect(host='localhost', user='root', password='SU92-BSCSM-F23-495', database='Hospital_management_system')

if conn.is_connected():
    print("Connection is established")

print("Thank You")
print("Please select one from below")
print("1.Book an appoipent")
print("2.Medical store")
print("3.Lab")
print("4.Shutdown")
choice=int(input("which one you prefer: "))

def doc__app (self):

    print("Available doctors")
    print("1. Afzal(skin specalist)")
    print("2. Muawar(bone specalist)")
    print("3. Hasseb (ear specalist)")
    print("4. Adnan (eye specalist)")
    d1=('Afzal(skin specalist)')
    d2=('Muawar(bone specalist)')
    d3=('Hasseb (ear specalist)')
    d4=('Adnan (eye specalist)')
    choice=int(input("Enter your choice of doc: "))

    patient_name=input("please enter patient name: ")
    patient_contact=int(input("please enter your contact number: "))
    patient_address=input("please enter your address: ")
    patient_age=int(input("please enter patient age: "))
    if choice==1:
        data_insertion(patient_name,patient_address,patient_contact,patient_age,d1)
    if choice==2:
        data_insertion(patient_name,patient_address,patient_contact,patient_age,d2)
    if choice==3:
            data_insertion(patient_name,patient_address,patient_contact,patient_age,d3)
    if choice==4:
            data_insertion(patient_name,patient_address,patient_contact,patient_age,d4)


def data_insertion(patient_name,patient_address,patient_contact,patient_age,doc_name):
    cursor=conn.cursor()
    insert_in_table="""insert into appointment(patient_name,patient_address,patient_contact,patient_age,doc_name) 
            values (%s,%s,%s,%s)"""
    data=(patient_name,patient_address,patient_contact,patient_age,doc_name)
        
    try:
        cursor.execute(insert_in_table, data)
        conn.commit()
        print("Data inserted successfully")
    except mysql.connector.Error as err:
            print(f"Error: {err}")
    cursor.close()

def medical_store(self):

    customer_name=input("please enter your name: ")
    address=input("Please enter your address: ")
    order=True

    if order==True :
        name=input("please enter the name of mediciene: ")
    cursor=conn.cursor()
    searching = f"SELECT * FROM medical_store WHERE patient_name='{name}'"

    try:
        cursor.execute(searching)
        records = cursor.fetchall()
        if records:
            table = PrettyTable()
            table.field_names = [desc[0] for desc in cursor.description]
        
            for row in records:
                table.add_row(row)
            
            print(table)
        else:
            print("No records found.")
    except  mysql.connector.Error as err:
            print(f"Error: {err}")
    cursor.close()

def lab(self):
    test_name=input('please enter the name of test: ')
    cursor=conn.cursor()
    cursor=conn.cursor()
    searching = f"SELECT * FROM test_details WHERE patient_name='{test_name}'"

    try:
        cursor.execute(searching)
        records = cursor.fetchall()
        if records:
            table = PrettyTable()
            table.field_names = [desc[0] for desc in cursor.description]
        
            for row in records:
                table.add_row(row)
            
            print(table)
            choice=input(bool('are you sure: '))
            if choice==True :
                test_apply(test_name)
        else:
            print("No records found.")
    except  mysql.connector.Error as err:
            print(f"Error: {err}")
    cursor.close()
    
def test_apply(test_name):
    patient_name=input("please enter patient name: ")
    patient_contact=int(input("please enter your contact number: "))
    patient_address=input("please enter your address: ")
    patient_age=int(input("please enter patient age: "))

    cursor=conn.cursor()
    insert_in_table="""insert into test_applicants(patient_name,patient_address,patient_contact,patient_age) 
            values (%s,%s,%s,%s)"""
    data=(patient_name,patient_address,patient_contact,patient_age)
        
    try:
        cursor.execute(insert_in_table, data)
        conn.commit()
        print("Data inserted successfully")
    except mysql.connector.Error as err:
            print(f"Error: {err}")
    cursor.close()
 
if choice==1 :
    doc__app(None)    
elif choice==2:
    medical_store(None)
elif choice==3 :
    lab(None)
elif choice==4 :
    exit()