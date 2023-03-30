import csv
import sqlite3


#exporting tools data to a csv in case of database loss
conn = sqlite3.connect('Database.db')
cursor = conn.cursor()
cursor.execute("select * from Tools;")
with open("ToolsData.csv", 'w',newline='') as csv_file: 
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow([i[0] for i in cursor.description]) 
    csv_writer.writerows(cursor)

#exporting user data to a csv in case of database loss
cursor.execute("select * from Users;")
with open("UserNames.csv", 'w',newline='') as csv_file: 
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow([i[0] for i in cursor.description]) 
    csv_writer.writerows(cursor)

#exporting booking data to a csv in case of database loss
    cursor.execute("select * from Bookings;")
with open("BookingData.csv", 'w',newline='') as csv_file: 
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow([i[0] for i in cursor.description]) 
    csv_writer.writerows(cursor)
conn.close()
