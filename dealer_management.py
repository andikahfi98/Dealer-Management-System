import json

def save_dealers():
    with open("dealers.json", "w") as file:
        json.dump(dealers, file, indent=4)

def load_dealers():
    try:
        with open("dealers.json", "r") as file:
            data = json.load(file)
        return data

    except FileNotFoundError:
        # Return data dealer default
        return []  


dealers = load_dealers()

def list_dealers():
    print("Daftar Dealer:")
    for dealer in dealers:
        print(f"ID: {dealer['id']}, Nama: {dealer['name']}, Kota: {dealer['city']}")

def search_dealer(dealer_id):
    for dealer in dealers:
        if dealer["id"] == dealer_id:
            return dealer
    return None

def create_dealer(dealer_id, name, city):
    new_dealer = {
        "id": dealer_id,
        "name": name,
        "city": city
    }

    if search_dealer(dealer_id) is not None:
        print(f"Dealer dengan ID {dealer_id} sudah ada.")
        return None

    dealers.append(new_dealer)
    print(f"Dealer {name} berhasil ditambahkan.")
    return new_dealer



def update_dealer(dealer_id, new_name, new_city):
    search_result = search_dealer(dealer_id)
    if search_result is not None:
        search_result["name"] = new_name
        search_result["city"] = new_city
        print(f"Dealer dengan ID {dealer_id} berhasil diperbarui.")
        return search_result
    else:
        print(f"Dealer dengan ID {dealer_id} tidak ditemukan.")
        return None

def delete_dealer(dealer_id):
    search_result = search_dealer(dealer_id)
    if search_result is not None:
        dealers.remove(search_result)
        print(f"Dealer dengan ID {dealer_id} berhasil dihapus.")
        
        return search_result
    else:
        print(f"Dealer dengan ID {dealer_id} tidak ditemukan.")
        return None


def get_dealer_id():
    while True:
        try:
            input_id = int(input("Masukkan ID Dealer: "))
            return input_id

        except ValueError:
            print("ID harus berupa angka!")


while True:
    print("\n=== DEALER MANAGEMENT SYSTEM ===")
    print("1. Create Dealer")
    print("2. Search Dealer")
    print("3. Update Dealer")
    print("4. Delete Dealer")
    print("5. Exit")

    choice = input("Pilih menu (1-5): ")

    if choice == "1":
        list_dealers()
        dealer_id = get_dealer_id()
        input_name = input("Masukkan Nama Dealer: ")
        input_city = input("Masukkan Kota Dealer: ")
        result = create_dealer(dealer_id, input_name, input_city)
        if result is not None:
            save_dealers()  # Save the updated dealers list to the JSON file
        

    elif choice == "2":
        dealer_id = get_dealer_id()
        result = search_dealer(dealer_id)
        if result is not None:
            print(f"Dealer ditemukan: {result}")
        else:
            print(f"Dealer dengan ID {dealer_id} tidak ditemukan.")

    elif choice == "3":
        list_dealers()
        dealer_id = get_dealer_id()
        dealer  = search_dealer(dealer_id)           
        if dealer is not None:
            pilihan =  input("Pilih data yang ingin diperbarui (1. Nama, 2. Kota): ")
            if pilihan == "1":    
                new_name = input("Masukkan Nama Dealer baru: ")
                updated = update_dealer(dealer_id, new_name, dealer["city"])
            elif pilihan == "2":
                new_city = input("Masukkan Kota Dealer baru: ")
                updated = update_dealer(dealer_id, dealer["name"], new_city)
            else:
                print("Pilihan tidak valid. Silakan pilih 1 atau 2.")
                updated = None

            if updated is not None:
                save_dealers()  # Save the updated dealers list to the JSON file

        else:
            print(f"Dealer dengan ID {dealer_id} tidak ditemukan.")

    elif choice == "4":
        list_dealers()
        dealer_id = get_dealer_id()
        result = delete_dealer(dealer_id)   
        if result is not None:
            save_dealers()  # Save the updated dealers list to the JSON file

    elif choice == "5":
        print("Terima kasih telah menggunakan Dealer Management System.")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih menu 1-5.")


