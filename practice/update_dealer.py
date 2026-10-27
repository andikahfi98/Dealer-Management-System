import sqlite3

def update_dealer(dealer_id, name, city):
    conn = sqlite3.connect("dealers.db")
    try:

        cursor = conn.cursor()

        cursor.execute(
            "UPDATE dealers SET name = ?, city = ? WHERE id = ?",
            (name, city, dealer_id)
        )
        conn.commit()
        if cursor.rowcount == 0:
            print(f"No dealer found with ID {dealer_id}.")
        else:
            print(f"Dealer with ID {dealer_id} updated successfully.")

    except sqlite3.Error as e:
        print(f"Error occurred: {e}")
        
    finally:
        conn.close()

update_dealer(101, "Kirana Premium", "Bandung")
update_dealer(999, "Unknown Dealer", "Jakarta")
