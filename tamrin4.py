
patient_list=[]

def add_patient(patient_name):
    patient_list.append(patient_name)


def search_patient(patient_name):
    i = 0
    for x in patient_list:
        if x == patient_name:
            print('Patient found,', x)
            i = 1
            break
    if i == 0:
        print('Patient not found!')
    
def delete_patient(patient_name):
    i = 0
    for x in patient_list:
        if x == patient_name:
            ask_delete = str(input('Patient found, Do you want to delete this patient? (y = yes , n = no)/  '))
            if ask_delete == 'y':
                patient_list.remove(x)
                print('Deleting was successful')
            i = 1
            break
    if i == 0:
        print('Patient not found!')

def show_patient_list():
    print('\n',patient_list)

def input_info():
        first_name = str(input("\nWhat is patient's first name? "))
        last_name = str(input("What is patient's last name? "))
        patient_name = first_name +' '+ last_name
        return(patient_name)
        



start = str(input('Do you want to start? ( y = yes , n = no)/ '))

while start == 'y':
    print('\n 1- Add patient \n 2- Search patient \n 3- Delete patient \n 4- Show patients list')
    option = int(input('\n Please enter the number of option you want? '))

    if option == 1:
        add_patient(input_info())
        show_patient_list()
    
    elif option == 2:
        search_patient(input_info())

    elif option == 3:
        delete_patient(input_info())
    elif option == 4:
        show_patient_list()
    
    start = str(input('\nDo you want to start again? ( y = yes , n = no)/ '))
