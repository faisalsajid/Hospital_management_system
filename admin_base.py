import mysql.connector

conn = mysql.connector.connect(host='localhost', user='root', password='SU92-BSCSM-F23-495', database='Hospital_management_system')

if conn.is_connected():
    print("Connection is established")


id='0'
password='0'


def add_new_patient():
        patient_name=input('enter patient name: ')
        patient_address=input('enter patient address: ')
        patient_contact=input('enter patient contact: ')
        patient_age=int(input('enter patient age: '))

        cursor=conn.cursor()
        insert_in_table="""insert into patient_info(name,address,contact,age) 
            values (%s,%s,%s,%s)"""
        data=(patient_name,patient_address,patient_contact,patient_age)
        
        try:
            cursor.execute(insert_in_table, data)
            conn.commit()
            print("Data inserted successfully")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        cursor.close()


def search():
    patient_name=input('enter patient Name: ')
    

def log_in (id,password):
    login=input('insert your log in id: ')
    pin=input('enter your log in passowrd: ')
    
    if login==id and pin==password:
        print('log in complete')
        print('1.add new patient')
        print('2.see doctor list')
        print('3.search patient')
        choice=int(input())
        if choice==1:
            add_new_patient()
        elif choice==3:
            search()
        else:
            print("error")

log_in(id,password)

conn.close()