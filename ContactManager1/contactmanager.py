import json
import os

FILE_NAME = "contacts.json"

# Load contacts from file
def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save contacts to file
def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

# Add new contact
def add_contact(contacts):
    print("\n=== Add Contact ===")
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    save_contacts(contacts)
    print("Contact added successfully!")

# View contact list
def view_contacts(contacts):
    print("\n=== Contact List ===")
    if not contacts:
        print("No contacts found.")
        return

    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} - {contact['phone']}")

# Search contact
def search_contact(contacts):
    search = input("\nEnter name or phone to search: ").lower()
    found = False

    for contact in contacts:
        if search in contact["name"].lower() or search in contact["phone"]:
            print("\nContact Found:")
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            print("Address:", contact["address"])
            found = True

    if not found:
        print("No matching contact found.")

# Update contact
def update_contact(contacts):
    view_contacts(contacts)

    try:
        choice = int(input("\nEnter contact number to update: ")) - 1

        if 0 <= choice < len(contacts):
            print("Leave blank to keep current value.")

            name = input("New Name: ")
            phone = input("New Phone: ")
            email = input("New Email: ")
            address = input("New Address: ")

            if name:
                contacts[choice]["name"] = name
            if phone:
                contacts[choice]["phone"] = phone
            if email:
                contacts[choice]["email"] = email
            if address:
                contacts[choice]["address"] = address

            save_contacts(contacts)
            print("Contact updated successfully!")

        else:
            print("Invalid contact number.")

    except ValueError:
        print("Invalid input.")

# Delete contact
def delete_contact(contacts):
    view_contacts(contacts)

    try:
        choice = int(input("\nEnter contact number to delete: ")) - 1

        if 0 <= choice < len(contacts):
            removed = contacts.pop(choice)
            save_contacts(contacts)
            print(f"{removed['name']} deleted successfully!")

        else:
            print("Invalid contact number.")

    except ValueError:
        print("Invalid input.")

# Main menu (User Interface)
def main():
    contacts = load_contacts()

    while True:
        print("\n===== Contact Management System =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_contact(contacts)

        elif choice == "2":
            view_contacts(contacts)

        elif choice == "3":
            search_contact(contacts)

        elif choice == "4":
            update_contact(contacts)

        elif choice == "5":
            delete_contact(contacts)

        elif choice == "6":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()