"""
import mysql.connector as ms
mydb=ms.connect(host='localhost', user='root', passwd='1234')

def add_blood_bank():
    location=input("Enter location\t")
    last_donationdrive=input('enter last donation drive')
    qty_a+=int(input('enter quatity of a+'))
    qty_a-=int(input('enter quatity of a-'))
    qty_b+=int(input('enter quantity of b+'))
    qty_b-==int(input('enter quantity of b-'))
    qty_o+=int(input('enter quantity of o+'))
    qty_o-=int(input('enter quantity of o-'))
    qty_ab+=int(input('enter quatity of ab+'))
    qty_ab-=int(input('enter quatity of ab-'))

def display_unformatted_bloodbank():
    cursor=cnx.cursor()
    cursor.execute("select * from blood_bank")
    data=cursor.fetchall()
    #print(data)

    for row in data:
        print(row)
#print("Displaying data in unformatted way\n", record)
display_unformatted_bloodbank()  #Calling function


def search_bloodbank_id(bloodbank_id):
    cursor=cnx.cursor()
    query=("select * from blood_bank where bloodbank_id=%s")
    cursor.execute(query,(bloodbank_id,))

    data=cursor.fetchall()
    for row in data:
        print(row)
    cnx.commit()
    cursor.close()

#print("Simple Search\n")
bloodbank_id=input("Enter blood bank id that you want to search")
search_bloodbank_id(bloodbank_id)

def bloodbank_update(bloodbank_id):


def bloodbank_delete(bloodbank_id):
    cursor=cnx.cursor()
    cursor.execute("select * from bloodbank_id where bloodbank_id='%s'"%bloodbank_id)
    record=cursor.fetchall()
    print("Displaying record for deletion")
    print(record)
    confirm=input("Do you want to delete this record")
    if confirm=='y':
        cursor.execute("delete from blood bank record where bloodbank_id='%s'"%bloodbank_id)
        cnx.commit()
        print(cursor.rowcount, "Record(s) deleted successfully")
    else:
        print("Delete operation cancelled")
        cursor.close()
    
