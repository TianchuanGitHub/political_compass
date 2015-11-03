import csv, sqlite3

db = sqlite3.connect( "./detainees.db" )
cursor = db.cursor()

# Remove everything in detainees
cursor.execute('DELETE FROM detainees')

# CREATE TABLE detainees (
#   name CHAR,
#   isn CHAR,
#   nationality CHAR,
#   iso CHAR,
#   arrival_date CHAR,
#   transfer_reason CHAR,
#   capture_details CHAR
# );

reader = csv.reader(open("gitmo.csv", "rb"))
for fields in reader:
  unicode_fields = [unicode(field, errors='ignore') for field in fields]
  cursor.execute('INSERT INTO detainees (name, isn, nationality, iso, arrival_date, transfer_reason, capture_details) VALUES (?,?,?,?,?,?,?)', unicode_fields)
db.commit()
db.close()