import psycopg2 as sql

conn = sql.connect(
    host='localhost',
    dbname='dvdrental',
    user='postgres',  # dbuser yerine user kullanın
    password='123',
    port='5434'       # Portunuzun doğru olduğundan emin olun
)
cursor = conn.cursor()

# Test için bir sorgu çalıştırabilirsiniz
cursor.execute("SELECT  * from film;")  # Basit bir test sorgusu
records = cursor.fetchall()     # Çıktıyı kontrol edin
tel = 0
for row in records:
    tel += 1
    print("\n", row)

# Bağlantıyı kapat
conn.commit()
cursor.close()
conn.close()
print("\n", tel)
