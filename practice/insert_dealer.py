import sqlite3

def create_dealer(dealer_id, name, city):
    conn = sqlite3.connect("dealers.db")
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO dealers (id, name, city) VALUES (?, ?, ?)",
            (dealer_id, name, city)
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError as e:
        print(f"Error occurred: {e}")
        return False    
    finally:
        conn.close()