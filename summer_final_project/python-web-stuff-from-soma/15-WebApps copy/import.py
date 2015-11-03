import csv, sqlite3

conn = sqlite3.connect( "detainees.db" )
cur = conn.cursor()

# Remove everything in detainees
cur.execute('DELETE FROM detainees')

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
  cur.execute('INSERT INTO detainees (name, isn, nationality, iso, arrival_date, transfer_reason, capture_details) VALUES (?,?,?,?,?,?,?)', unicode_fields)
