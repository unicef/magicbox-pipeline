import psycopg2
try:
    conn = psycopg2.connect("dbname='all_countries_one_table' user='postgres' host='postgis' password='secure_password'")
except:
    print("I am unable to connect to the database")

cur = conn.cursor()
cur.execute("""select iso, ID_0, ID_1, ID_2, ID_3, ID_4, ID_5 from highest_level_admin WHERE ST_Within (ST_Transform (ST_GeomFromText ('POINT(-72.773438 3.261177)',4326),4326), highest_level_admin.geom); """)
rows = cur.fetchall()
print("\nRows: \n")
for row in rows:
    print(row)
