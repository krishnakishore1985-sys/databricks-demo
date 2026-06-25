-------File Automation__________________________________________________________________________

import os
print(os.getcwd())

----------------------------------------
import os

# Change directory
os.chdir("D:\\Projects")

# Show current directory
print(os.getcwd())

-------------------------------------------------------------------
with open("sample.txt", "r") as file:

    for line in file:
        print(line.strip())
		
-------------------------------------------------------------------

with open("sample.txt", "w") as file:

file.write("Hello Python Automation")

-----------------------------------------------------------------------------------
import os

os.mkdir("Reports")

---------------------------------------------------------------------------------

import os

files = os.listdir(".")

print(files)

------------------------------------------------------------------

import os

folder = "kishore"

for count, filename in enumerate(os.listdir(folder)):

    old_path = os.path.join(folder, filename)

    new_name = f"photo_{count}.jpg"

    new_path = os.path.join(folder, new_name)

    os.rename(old_path, new_path)

print("Renaming completed")

----------------------------------------------------

import os

folder = r"C:\Users\DELL\Desktop"

for count, filename in enumerate(os.listdir(folder)):
    print(count, filename)
	
Breakdown
os.listdir(folder)

Returns a list of all files and folders inside the directory.

Example result:

['a.txt', 'b.jpg', 'notes.pdf']
enumerate(...)

Adds a counter/index to each item.

Example:

enumerate(['a.txt', 'b.jpg', 'notes.pdf'])

Produces:

(0, 'a.txt')
(1, 'b.jpg')
(2, 'notes.pdf')

-------------------python---------------------------------------------------------------------------------
import csv

with open("sales.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
		
-----------------------------pandas--------------------------------------------------------------------------------

import pandas as pd

df = pd.read_csv("sales.csv")

print(df.head())

----------------------------------------------------------------------------------------------------------------

import pandas as pd

data = [("Ravi",10000,"Hyd"),("Kishore",20000,"Vskp")]
columns= ["Name","Salary","Location"]

df = pd.DataFrame(data,columns=columns)

df.to_csv(
    "output1.csv",
    index=False
)
-------------------------------------------------------------------------------

with open("sales.csv","r") as file:
    line =csv.reader(file)
    for line in file:
        print(line)
		
['Name', 'Salary', 'Location']
['Ravi', '10000', 'Hyd']
['Kishore', '20000', 'Vskp']
		
------------------------------------------------------------------------------------------

with open("sales.csv","r") as file:
   print(file.read())
   
Year,Region,Sales
2000,Ahmedabad,2000
2001,Bangalore,3000
2002,Hyderabad,4000
2003,Delhi,5000
2004,Mumbai,6000
2005,Bhopal,1500
   
------------------------------------------------------------------------------------
   Simple analogy
📄 file.read()

👉 Like reading a book as a single long paragraph

📊 csv.reader()

👉 Like reading a table row by row

-------------------------------------------------------------------------
Best Practices
Use try-except
try:
    with open("data.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("File not found")
	
	
--------------API Ingestion---------------------------------------------------------------------------------------------------------------


import requests
import pandas as pd

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

data = response.json()

df = pd.DataFrame(data)

print(df.head())



---Database Automation-------------------------------------------------------------------------------------------------------------------
1. Connect to Database (MySQL / PostgreSQL)
MySQL connection automation
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="testdb"
)

cursor = conn.cursor()
print("Connected to MySQL")
PostgreSQL connection automation
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="testdb",
    user="postgres",
    password="password"
)

cursor = conn.cursor()
print("Connected to PostgreSQL")
2. Read Data from Database → Pandas (very common automation)
import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="testdb"
)

query = "SELECT * FROM employees"

df = pd.read_sql(query, conn)

print(df.head())

👉 Used in:

Reporting automation
ETL pipelines
Data extraction jobs
3. Insert Data into Database (Bulk Automation)
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="testdb"
)

cursor = conn.cursor()

data = [
    ("Ravi", 10000),
    ("Kishore", 20000)
]

query = "INSERT INTO employees (name, salary) VALUES (%s, %s)"

cursor.executemany(query, data)

conn.commit()
print("Data inserted successfully")
4. CSV → Database Automation (ETL script)
import pandas as pd
import mysql.connector

df = pd.read_csv("employees.csv")

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="testdb"
)

cursor = conn.cursor()

for i, row in df.iterrows():
    cursor.execute(
        "INSERT INTO employees (name, salary) VALUES (%s, %s)",
        (row["name"], row["salary"])
    )

conn.commit()
print("CSV loaded into DB")
5. Database → CSV Export Automation
import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="testdb"
)

query = "SELECT * FROM employees"

df = pd.read_sql(query, conn)

df.to_csv("export.csv", index=False)

print("Data exported to CSV")
6. Automated Daily Backup Script
import mysql.connector
from datetime import datetime

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="testdb"
)

cursor = conn.cursor()

tables = ["employees", "departments"]

backup_file = f"backup_{datetime.now().strftime('%Y%m%d')}.sql"

with open(backup_file, "w") as f:
    for table in tables:
        cursor.execute(f"SELECT * FROM {table}")
        rows = cursor.fetchall()

        for row in rows:
            f.write(str(row) + "\n")

print("Backup completed")
7. Data Validation Automation (very important in real jobs)
import pandas as pd
import mysql.connector

df = pd.read_sql("SELECT * FROM employees", conn)

# validation rules
if df.isnull().sum().sum() > 0:
    print("❌ Missing values found")
else:
    print("✅ Data is clean")
8. Scheduled Automation Script (runs every day)
import time

def job():
    print("Running database task...")
    # your DB code here

while True:
    job()
    time.sleep(86400)  # 24 hours
9. Update Records Automation
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="testdb"
)

cursor = conn.cursor()

query = "UPDATE employees SET salary = salary + 1000 WHERE salary < 20000"

cursor.execute(query)
conn.commit()

print("Salary updated")
10. Delete Old Data Automation
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="testdb"
)

cursor = conn.cursor()

query = "DELETE FROM employees WHERE created_date < '2024-01-01'"

cursor.execute(query)
conn.commit()

print("Old data removed")

-----------------ETL JOB PYTHON AUTOMATION-------------------------------------------------------------------------------------------
Read CSV file
Insert data into SQLite database
Update salary automatically
Filter employees with salary > 15000

import sqlite3
import pandas as pd

# Step 1: Read CSV
df = pd.read_csv("employees.csv")
print("CSV Data:")
print(df)

# Step 2: Connect to SQLite database
conn = sqlite3.connect("company.db")
cursor = conn.cursor()

# Step 3: Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    salary INTEGER,
    department TEXT
)
""")

# Step 4: Insert CSV data into database
for _, row in df.iterrows():
    cursor.execute("""
    INSERT OR REPLACE INTO employees (id, name, salary, department)
    VALUES (?, ?, ?, ?)
    """, (row["id"], row["name"], row["salary"], row["department"]))

conn.commit()
print("\nData inserted into database successfully.")

# Step 5: Automatically update salary (example: 10% bonus for IT employees)
cursor.execute("""
UPDATE employees
SET salary = salary * 1.10
WHERE department = 'IT'
""")

conn.commit()
print("\nSalary updated for IT employees.")

# Step 6: Filter employees with salary > 15000
cursor.execute("""
SELECT * FROM employees
WHERE salary > 15000
""")

result = cursor.fetchall()

print("\nEmployees with salary > 15000:")
for row in result:
    print(row)

# Step 7: Close connection
conn.close()
🔥 Output Example
Employees with salary > 15000:
(2, 'Kiran', 18000, 'HR')
(3, 'Anil', 25000, 'Finance')
(1, 'Ravi', 13200, 'IT')