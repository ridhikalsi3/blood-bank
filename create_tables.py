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
