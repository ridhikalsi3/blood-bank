"""
import mysql.connector as ms
mydb=ms.connect(host='localhost', user='root', passwd='1234')

def create_donor():
    query_donor='''create table donor
    (donor_id varchar(10) NOT NULL PRIMARY KEY,
    name varchar(20),
    blood_group varchar(20),
    contact_number int,
    DOB date,
    medical_history varchar(20),
    last_donated varhcar(20),
    bloodbank_id varchar(20)
    '''
    cur.execute(query_donor)
def add_donor_data():
    cursor=mydb.cursor()
    donor_id=input("enter donor_id\t") 
    name=input("Enter name\t")
   
def create_blood_bank():
    query_ blood_bank='''create table blood_bank
'''   

    
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
def display_donor_data():
    cursor=cnx.cursor()
    query=("select * from donor_data")
    cursor.execute(query)
    record=cursor.fetchall()
    #print("Displaying record in formatted way\n",record)
    for row in record:
        #print("__________________________________________")
        print("donor_id = \t", row[0])
        print("name = \t", row[1])
        print("blood_group = \t", row[2])
        print("contact_number = \t", row[3])
        print("DOB = \t", row[4])
        print("medical_history varchar = \t", row[5])
        print("last_donated varhcar = \t", row[6])
        print("bloodbank_id = \t", row[7])
        print("__________________________________________")
print("Displaying data in tabular form")
#Simple Search
#input bno and display all the records
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
          
def insert_donor():
    b="insert into donor('D01','steve','A+','9956418237','1993-03-21','migraine','B001')"
    c="insert into donor('D02','adam','B-','9236448637','1990-04-20', NULL, 'B002')"
    d="insert into donor('D03', 'david', 'O+', '9139598637', '2000-03-03', NULL, 'B003')"
    e="insert into donor('D04', 'prince','AB+','')"



def update_donor(donorid):
    cursor=cnx.cursor(buffered=True)
    cursor.execute("select * from donor record where donorid='%s'")
    print("Enter the new data")
    name=input("Enter name\t")
    blood_group=input("Enter blood_group\t")
    contact_number=int(input("Enter contact number\t"))
    DOB=input("Enter dob\t")
    medical_history=input("Enter medical history\t")
    last_donated=input("Enter last donated (day) \t")
    bloodbank_id=int(input("Enter blood bank ID\t"))
    cursor.execute("update donorid set name='%s', blood_group=%s, contact_number='%d', DOB='%s'\
                   medical_history='%s', last_donated='%s', bloodbank_id='%d'\
                   where %(name,blood_group,contact_number,DOB,medical_history,last_donated,)


    cnx.commit()
    cursor.close()


"""
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
    
