import sqlite3

conn = sqlite3.connect("dealers.db")
cursor = conn.cursor()

# Periksa data dummy
condition = """
    id BETWEEN 1 AND 10
    AND name = 'Dealer ' || id
    AND city = 'City ' || id
"""

cursor.execute(f"SELECT * FROM dealers WHERE {condition}")
print("Data yang akan dihapus:")
print(cursor.fetchall())

# Konfirmasi sebelum menghapus
confirm = input("Hapus data tersebut? (y/n): ")

if confirm.lower() == "y":
    cursor.execute(f"DELETE FROM dealers WHERE {condition}")
    deleted = cursor.rowcount
    conn.commit()
    print(f"{deleted} dealer berhasil dihapus.")

conn.close()