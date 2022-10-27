import pyodbc 

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-CMG3OIG\SQLEXPRESS;'
                      'Database=TSQL;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute("SELECT sc.companyname, country city FROM Sales.Customers as sc WHERE sc.country = 'Mexico'")

for i in cursor:
    print(i)

print("hoi")

print("hoi")

print("hoi")

print("hoi")
