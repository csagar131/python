#!/usr/bin/python3

# Import modules for CGI handling 
import cgi, cgitb 

#mysql database connectivity

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="demouser",
  passwd="sagar*123",
  database="project"
)

mycursor = mydb.cursor()

#mycursor.execute("SHOW TABLES")


mycursor.execute("select * from login")

myresult = mycursor.fetchall() # it gives the list




# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
username = form.getvalue('email')
password  = form.getvalue('pass')

if (username == myresult[0][0]) and (password == myresult[0][1]):
    print("Content-type:text/html\n")
    print("<html>")
    print("<head>")
    print("<title>Hello - Second CGI Program</title>")
    print("</head>")
    print("<body>")
    print("<h2>Hello "+myresult[0][0]+"</h2>")
    print("</body>")
    print("</html>")
else:
    print("Content-type:text/html\n")
    print("<html>")
    print("<head>")
    print("<title>Hello - Second CGI Program</title>")
    print("</head>")
    print("<body>")
    print("<h2>username and password incorrect </h2>")
    print("</body>")
    print("</html>")

