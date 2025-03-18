import mysql.connector
from prettytable import PrettyTable
conn = mysql.connector.connect(host='localhost', user='root', password='SU92-BSCSM-F23-495', database='Hospital_management_system')

if conn.is_connected():
    print("Connection is established")
    
def doc__app (self):

    print("Available doctors")
    print("1. Afzal (Skin Specialist)")
    print("2. Muawar (Bone Specialist)")
    print("3. Hasseb (Ear Specialist)")
    print("4. Adnan (Eye Specialist)")

    doctors = {
        1: 'Afzal (Skin Specialist)',
        2: 'Muawar (Bone Specialist)',
        3: 'Hasseb (Ear Specialist)',
        4: 'Adnan (Eye Specialist)'
    }

    choice = int(input("Enter your choice of doctor (1-4): "))

    if choice not in doctors:
        print("Invalid choice!")
        return

    patient_name = input("Please enter patient name: ")
    patient_contact = input("Please enter your contact number (11 digits): ")
    patient_address = input("Please enter your address: ")
    patient_age = int(input("Please enter patient age: "))

    if len(patient_contact) != 11 or not patient_contact.isdigit():
        print("Invalid contact number. Must be 11 digits.")
        return

    doc_name = doctors[choice]

    data_insertion(patient_name, patient_address, patient_contact, patient_age, doc_name)


def data_insertion(patient_name, patient_address, patient_contact, patient_age, doc_name):
    cursor = conn.cursor()

    insert_in_table = """INSERT INTO appointment (patient_name, patient_address, patient_contact, patient_age, doc_name)
    VALUES (%s, %s, %s, %s, %s)"""

    data = (patient_name, patient_address, patient_contact, patient_age, doc_name)

    try:
        cursor.execute(insert_in_table, data)
        conn.commit()
        print("Data inserted successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

def medical_store():
    medicine_name=input("please enter the name of mediciene: ")
    cursor=conn.cursor()
    searching = f"SELECT * FROM medical_store WHERE medicine_name='{medicine_name}'"

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
    searching = f"SELECT * FROM test_details WHERE test_name='{test_name}'"

    try:
        cursor.execute(searching)
        records = cursor.fetchall()
        if records:
            table = PrettyTable()
            table.field_names = [desc[0] for desc in cursor.description]
        
            for row in records:
                table.add_row(row)
            
            print(table)
            choice = input("Are you sure? (yes/no): ").strip().lower()
            if choice == "yes":  
                test_apply(test_name)  # Call function if user is not sure

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
    insert_in_table="""insert into test_applicants(patient_name,patient_address,patient_contact,patient_age,test_name) 
            values (%s,%s,%s,%s,%s)"""
    data=(patient_name,patient_address,patient_contact,patient_age,test_name)
        
    try:
        cursor.execute(insert_in_table, data)
        conn.commit()
        print("Data inserted successfully")
    except mysql.connector.Error as err:
            print(f"Error: {err}")
    cursor.close()

choice=0
while(choice!=4):
    print("Thank You")
    print("Please select one from below")
    print("1.Book an appoipent")
    print("2.Medical store")
    print("3.Lab")
    print("4.Shutdown")
    choice=int(input("which one you prefer: "))


    if choice==1 :
        doc__app(None)    
    elif choice==2:
        medical_store()
    elif choice==3 :
        lab(None)
    elif choice==4 :
        exit()
    elif:
        print('error')