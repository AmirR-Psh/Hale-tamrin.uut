libarary = {}



def add_book(subject,name_book):
    libarary[subject].append(name_book)

def show_book(subject):
    if subject in libarary:
        print(libarary[subject])
    else:
        print('subject not found!!!')

def search_book(subject,name_book):
    value = libarary[subject]
    if name_book in value:
        return True
    else:
        return False





start = str(input('Do you want to start? (y=yes , n=no)'))
while start == 'y':
    
    print('\n1- add subject and book \n2- show books of subject \n3- search \n')
    optoin=int(input('Enter option?'))
    if optoin==1:
        subject = str(input('\nEnter subject?')) 
        add = str(input('add book? (y=yes , n=no)'))
        while add == 'y':
            name_book = str(input('name of book?'))
            if subject in libarary:
                add_book(subject,name_book)
            elif subject not in libarary:
                libarary[subject] = [name_book]
            add = str(input('add book again (y=yes , n=no)?'))
    elif optoin == 2:
        subject = str(input('Enter subject?'))
        show_book(subject)
    elif optoin == 3:
        subject = str(input('Enter subject?'))
        name_book = str(input('name of book?'))
        if search_book(subject,name_book):
            print('book found.')
        else:
            print('this book whith this',name_book,'name ,whith this',subject,' subject , not found!!!')


    
    start = str(input('Do you want to start again? (y=yes , n=no)')) 

print(libarary)