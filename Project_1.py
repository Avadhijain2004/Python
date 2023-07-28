print("                   STUDENT DATABASE                        ")
mydict={
    1 : ["Avadhi",'18'],
    2 : ["Samriddhi",'13'],
    3 : ["Ram",'16']
}
def display():
    print(mydict)

def search():
    n=int(input("Enter roll no. of student to get his/her information  : "))
    if n in mydict :
        a = print("Information of student present on this roll no. is ", mydict.get(n))
    else :
        print("Roll number not found")

def update():
    r = int(input("Enter roll no. of student which you want to update : "))
    name = input("Enter name :")
    age = int(input("Enter age : "))
    mydict.update({r: [name, age]})
    print("Updated database " ,mydict)

def delete():
    print("Database Elements : ",mydict)
    p= int(input("Enter roll no. of student which you want to delete : "))
    if p in mydict :
        mydict.pop(p)
        print("Updated : ", mydict)
    else :
        print("Entered roll no. is not present in database")

def option():
    choice = int(input('''Enter the operation detail: \n \
    1: Display the information of every student : \n \
    2: Search student by his/her roll no. :  \n \
    3: Update information of a particular student : \n \
    4: Delete information of a particular student :\n \
    5: Exit \n  \                 
    Option: '''))

    if choice==1:
        display()
        print('Want to perform some other operation??? Y or N: ')
        inp = input()
        if inp == 'Y':
            option()

        # exit function call
        exit()

    elif choice == 2:
        search()
        print('Want to perform some other operation??? Y or N: ')

        inp = input()
        if inp == 'Y':
            option()
        exit()

    elif choice == 3:
        update()
        print('Want to perform some other operation??? Y or N: ')

        inp = input()
        if inp == 'Y':
            option()
        exit()

    elif choice == 4:
        delete()
        print('Want to perform some other operation??? Y or N: ')

        inp = input()
        if inp == 'Y':
            option()
        exit()

    elif choice == 5:
        search_by_name()
        print('Want to perform some other operation??? Y or N: ')

        inp = input()
        if inp == 'Y':
            option()
        exit()

    else:
        print('Thanks for executing me!!!!')
        exit()

option()

