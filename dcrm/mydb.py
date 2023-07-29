# install mysql on your computer
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'root'
  
)

# Prepare a cursor object
cursorObject = dataBase.cursor()


# Create a Database
cursorObject.execute('CREATE DATABASE elderco')

print('All Done!')