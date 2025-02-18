id='0'
password='0'
no_of_bed=500

def log_in (self,id,password):
    login=input('insert your log in id: ')
    pin=input('enter your log in passowrd: ')
    if login==id:
        if pin==password:
            print('log in complete')
            print('1.add new patient')
            print('2.see available no of bed')
            print('3.see doctor list')
            print('4.search patient')
            choice=int(input())
            
log_in(None,id,password)

def add_new_patient(self):
    patient_name=input('enter patient name: ')
    patient_address=input('enter patient address: ')
    patient_contact=input('enter patient contact: ')
    patient_age=int(input('enter patient age: '))

def search(self):
    id=int(input('enter patient id: '))
