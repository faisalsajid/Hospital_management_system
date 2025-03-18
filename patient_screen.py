

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
    print("1. Hasseb (ear specalist)")
    print("1. Adnan (eye specalist)")
    choice=int(input("Enter your choice: "))

    patient_name=input("please enter patient name: ")
    patient_contact=int(input("please enter your contact number: "))
    patient_address=input("please enter your address: ")
    patient_age=int(input("please enter patient age: "))

     cursor=conn.cursor()
        insert_in_table="""insert into patient_info(patient_name,patient_address,patient_contact,patient_age) 
            values (%s,%s,%s,%s)"""
        data=(patient_name,patient_address,patient_contact,patient_age)
        
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

def lab(self):

    patient_name=input("please enter patient name: ")
    patient_contact=int(input("please enter your contact number: "))
    patient_address=input("please enter your address: ")
    patient_age=int(input("please enter patient age: "))

     cursor=conn.cursor()
        insert_in_table="""insert into patient_info(patient_name,patient_address,patient_contact,patient_age) 
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