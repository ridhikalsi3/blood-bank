"""
import mysql.connector as ms
mydb=ms.connect(host='localhost', user='root', passwd='1234')

def add_donor_data():
    cursor=mydb.cursor()
    donor_id=input("enter donor_id\t") 
    name=input("Enter name\t")

    
