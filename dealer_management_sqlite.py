import sqlite3


def list_dealers():
    conn = sqlite3.connect("dealers.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM dealers")
    dealers = cursor.fetchall()

    conn.close()
    return dealers


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


def search_dealer(dealer_id):
    conn = sqlite3.connect("dealers.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM dealers WHERE id = ?", (dealer_id,))
    dealer = cursor.fetchone()

    conn.close()
    return dealer


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

def get_dealer_id():
    while True:
        try:
            return int(input("Enter Dealer ID: "))
        except ValueError:
            print("Dealer ID must be a number.")

while True:
    print("\n=== DEALER MANAGEMENT SYSTEM ===")
    print("1. List Dealers")
    print("2. Create Dealer")
    print("3. Search Dealer")
    print("4. Update Dealer")
    print("5. Delete Dealer")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        dealers = list_dealers()
        if dealers:
            for dealer in dealers:
                print(f"ID: {dealer[0]}, Name: {dealer[1]}, City: {dealer[2]}")
        else:
            print("No dealers found.")  

    elif choice == "2":
        dealer_id = get_dealer_id()
        name = input("Enter Dealer Name: ")
        city = input("Enter Dealer City: ")
        result = create_dealer(dealer_id, name, city)
        if result:
            print("Dealer created successfully.")
        else:
            print("Failed to create dealer.")

    elif choice == "3":
        dealer_id = get_dealer_id()
        dealer = search_dealer(dealer_id)
        if dealer:
            print(f"ID: {dealer[0]}, Name: {dealer[1]}, City: {dealer[2]}")
        else:
            print(f"No dealer found with ID {dealer_id}.")

    elif choice == "4":
        dealer_id = get_dealer_id()
        name = input("Enter new Dealer Name: ")
        city = input("Enter new Dealer City: ")
        if name.strip() == "" or city.strip() == "":
            print("Name and City cannot be empty.")
        else:
            update_dealer(dealer_id, name, city)

    elif choice == "5":
        dealer_id = get_dealer_id()
        delete_dealer(dealer_id)

    elif choice == "6":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")