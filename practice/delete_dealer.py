import sqlite3

def delete_dealer(dealer_id):
    conn = sqlite3.connect("dealers.db")
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM dealers WHERE id = ?", (dealer_id,))
        deleted_rows = cursor.rowcount
        conn.commit()
        if deleted_rows == 0:
            print(f"No dealer found with ID {dealer_id}.")
        else:
            print(f"Dealer with ID {dealer_id} deleted successfully.")

    except sqlite3.Error as e:
        print(f"Error occurred: {e}")
        
    finally:
        conn.close()

