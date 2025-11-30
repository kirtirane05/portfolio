# Contact Management System
# Made using Python

contacts = []  # List to store contact dictionaries


# Function to add a new contact
def add_contact():
    print("\n=== Add New Contact ===")
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
    print(f"\n✅ Contact '{name}' added successfully!")


# Function to view all contacts
def view_contacts():
    print("\n=== Contact List ===")
    if not contacts:
        print("No contacts available.")
        return

    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} - {contact['phone']}")


# Function to search for a contact
def search_contact():
    print("\n=== Search Contact ===")
    query = input("Enter name or phone number to search: ")

    found = False
    for contact in contacts:
        if query.lower() in contact['name'].lower() or query in contact['phone']:
            print("\n--- Contact Found ---")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            found = True
            break

    if not found:
        print("⚠ No contact found with that name or number.")


# Function to update a contact
def update_contact():
    print("\n=== Update Contact ===")
    name = input("Enter the name of the contact to update: ")

    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print(f"\nEditing contact: {contact['name']}")
            contact['phone'] = input("Enter new phone number: ")
            contact['email'] = input("Enter new email: ")
            contact['address'] = input("Enter new address: ")
            print(f"\n✅ Contact '{name}' updated successfully!")
            return

    print("⚠ Contact not found.")


# Function to delete a contact
def delete_contact():
    print("\n=== Delete Contact ===")
    name = input("Enter the name of the contact to delete: ")

    for contact in contacts:
        if contact['name'].lower() == name.lower():
            contacts.remove(contact)
            print(f"\n🗑 Contact '{name}' deleted successfully!")
            return

    print("⚠ Contact not found.")


# Main menu function
def main():
    while True:
        print("\n===== CONTACT MANAGEMENT SYSTEM =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("\n👋 Exiting Contact Manager. Goodbye!")
            break
        else:
            print("⚠ Invalid choice! Please enter a number between 1 and 6.")


# Run the program
if __name__ == "__main__":
    main()
