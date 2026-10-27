import sqlite3

def search_dealer(dealer_id):
    conn = sqlite3.connect("dealers.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM dealers WHERE id = ?", (dealer_id,))
    dealer = cursor.fetchone()

    conn.close()
    return dealer


result = search_dealer(101)

if result is not None:
    print(f"ID: {result[0]}")
    print(f"Nama: {result[1]}")
    print(f"Kota: {result[2]}")
else:
    print("Dealer tidak ditemukan.")

search_dealer(101)